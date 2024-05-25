# coding=utf-8
import sys
from helper import *
from collections import defaultdict
from difflib import SequenceMatcher
import pdb


class PostQuesAns:

    def __init__(self, post_title, post, post_sents, question_comment, answer):
        self.post_title = post_title
        self.post = post
        self.post_sents = post_sents
        self.question_comment = question_comment
        self.answer = answer


class PostQuesAnsGenerator:

    def __init__(self):
        self.post_ques_ans_dict = defaultdict(PostQuesAns)

    def get_diff(self, initial, final):
        s = SequenceMatcher(None, initial, final)
        diff = None
        for tag, i1, i2, j1, j2 in s.get_opcodes():
            if tag == 'insert':
                diff = final[j1:j2]
        if not diff:
            return None
        return diff

    def find_first_question(self, answer, question_comment_candidates, vocab, word_embeddings):
        first_question = None
        first_date = None
        for question_comment in question_comment_candidates:
            if first_question == None:
                first_question = question_comment
                first_date = question_comment.creation_date
            else:
                if question_comment.creation_date < first_date:
                    first_question = question_comment
                    first_date = question_comment.creation_date
        return first_question

    def find_answer_comment(self, all_comments, question_comment, post_userId):
        answer_comment, answer_comment_date = None, None
        for comment in all_comments:
            if comment.userId and comment.userId == post_userId:
                if comment.creation_date > question_comment.creation_date:
                    if not answer_comment or (comment.creation_date < answer_comment_date):
                        answer_comment = comment
                        answer_comment_date = comment.creation_date
        return answer_comment

    def generate_using_comments(self, posts, question_comments, all_comments, vocab, word_embeddings):
        for postId in posts.keys():
            if postId in self.post_ques_ans_dict.keys():
                continue
            if posts[postId].typeId != 1:  # is not a main post
                continue
            first_question = None
            first_date = None
            for question_comment in question_comments[postId]:
                if question_comment.userId and question_comment.userId == posts[postId].owner_userId:
                    continue  # Ignore comments by the original author of the post
                if first_question == None:
                    first_question = question_comment
                    first_date = question_comment.creation_date
                else:
                    if question_comment.creation_date < first_date:
                        first_question = question_comment
                        first_date = question_comment.creation_date
            question = first_question
            if not question:
                continue
            answer_comment = self.find_answer_comment(all_comments[postId], question, posts[postId].owner_userId)
            if not answer_comment:
                continue
            answer = answer_comment
            self.post_ques_ans_dict[postId] = PostQuesAns(posts[postId].title, posts[postId].body, \
                                                          posts[postId].sents, question.text, answer.text)

    # 从帖子的编辑历史和评论中提取出问题和答案。生成一个字典，其中键是帖子的ID，值是一个PostQuesAns对象，该对象包含帖子的标题、初始帖子、初始帖子的句子、第一个问题的文本和第一个答案。
    def generate(self, posts, question_comments, all_comments, posthistories, vocab, word_embeddings):
        # 遍历所有的帖子历史记录
        for postId, posthistory in posthistories.iteritems():
            # 如果帖子没有被编辑过，或者帖子不是主帖，或者没有初始帖子，那么就跳过这个帖子
            if not posthistory.edited_posts or posts[postId].typeId != 1 or not posthistory.initial_post:
                continue

            first_edit_date, first_question, first_answer = None, None, None

            # 对于每个帖子，遍历其所有的编辑历史
            for i in range(len(posthistory.edited_posts)):
                # 使用get_diff方法找出初始帖子和编辑后的帖子之间的差异，这个差异被视为答案
                answer = self.get_diff(posthistory.initial_post, posthistory.edited_posts[i])
                if not answer:
                    continue
                else:
                    answer = remove_urls(' '.join(answer))
                    answer = answer.split()
                    # 如果答案太短或太长，那么就跳过这次编辑
                    if is_too_short_or_long(answer):
                        continue

                question_comment_candidates = []

                # 对于每次有效的编辑，遍历所有的评论，找出在编辑之前由其他用户发表的评论，这些评论被视为可能的问题
                for comment in question_comments[postId]:
                    if comment.userId and comment.userId == posts[postId].owner_userId:
                        continue  # Ignore comments by the original author of the post
                    if comment.creation_date > posthistory.edit_dates[i]:
                        continue  # Ignore comments added after the edit
                    else:
                        question_comment_candidates.append(comment)

                # 使用find_first_question方法从这些可能的问题中找出第一个问题
                question = self.find_first_question(answer, question_comment_candidates, vocab, word_embeddings)
                if not question:
                    continue

                # 如果找到了第一个问题，那么就使用find_answer_comment方法找出帖子作者在问题之后发表的评论，这个评论被视为可能的答案
                answer_comment = self.find_answer_comment(all_comments[postId], question, posts[postId].owner_userId)
                if answer_comment and 'edit' not in answer_comment.text:  # prefer edit if comment points to the edit
                    question_indices = get_indices(question.text, vocab)
                    answer_indices = get_indices(answer, vocab)
                    answer_comment_indices = get_indices(answer_comment.text, vocab)
                    # 如果问题和评论的相似度更高，那么就将评论视为答案
                    if get_similarity(question_indices, answer_comment_indices, word_embeddings) > get_similarity(
                            question_indices, answer_indices, word_embeddings):
                        answer = answer_comment.text

                if first_edit_date == None or posthistory.edit_dates[i] < first_edit_date:
                    first_question, first_answer, first_edit_date = question, answer, posthistory.edit_dates[i]

            if not first_question:
                continue

            # 如果找到了第一个问题和对应的答案，那么就创建一个PostQuesAns对象，并将其添加到字典中
            self.post_ques_ans_dict[postId] = PostQuesAns(posts[postId].title, posthistory.initial_post, \
                                                          posthistory.initial_post_sents, first_question.text,
                                                          first_answer)

        # 在处理完所有的帖子历史记录后，使用generate_using_comments方法处理那些没有被编辑过，但是有评论的帖子
        self.generate_using_comments(posts, question_comments, all_comments, vocab, word_embeddings)

        # 最后，返回生成的字典
        return self.post_ques_ans_dict

    # def generate(self, posts, question_comments, all_comments, posthistories, vocab, word_embeddings):
    #     # 遍历所有的帖子历史记录
    #     for (postId, post), (question_comment, all_comment), posthistory in zip(posts, question_comments,
    #                                                                             posthistories):
    #         # 如果帖子没有被编辑过，或者帖子不是主帖，或者没有初始帖子，那么就跳过这个帖子
    #         if not posthistory.edited_posts or post.typeId != 1 or not posthistory.initial_post:
    #             continue
    #
    #         first_edit_date, first_question, first_answer = None, None, None
    #
    #         # 对于每个帖子，遍历其所有的编辑历史
    #         for i in range(len(posthistory.edited_posts)):
    #             # 使用get_diff方法找出初始帖子和编辑后的帖子之间的差异，这个差异被视为答案
    #             answer = self.get_diff(posthistory.initial_post, posthistory.edited_posts[i])
    #             if not answer:
    #                 continue
    #             else:
    #                 answer = remove_urls(' '.join(answer))
    #                 answer = answer.split()
    #                 # 如果答案太短或太长，那么就跳过这次编辑
    #                 if is_too_short_or_long(answer):
    #                     continue
    #
    #             question_comment_candidates = []
    #
    #             # 对于每次有效的编辑，遍历所有的评论，找出在编辑之前由其他用户发表的评论，这些评论被视为可能的问题
    #             for comment in question_comment:
    #                 if comment.userId and comment.userId == post.owner_userId:
    #                     continue  # Ignore comments by the original author of the post
    #                 if comment.creation_date > posthistory.edit_dates[i]:
    #                     continue  # Ignore comments added after the edit
    #                 else:
    #                     question_comment_candidates.append(comment)
    #
    #             # 使用find_first_question方法从这些可能的问题中找出第一个问题
    #             question = self.find_first_question(answer, question_comment_candidates, vocab, word_embeddings)
    #             if not question:
    #                 continue
    #
    #             # 如果找到了第一个问题，那么就使用find_answer_comment方法找出帖子作者在问题之后发表的评论，这个评论被视为可能的答案
    #             answer_comment = self.find_answer_comment(all_comment, question, post.owner_userId)
    #             if answer_comment and 'edit' not in answer_comment.text:  # prefer edit if comment points to the edit
    #                 question_indices = get_indices(question.text, vocab)
    #                 answer_indices = get_indices(answer, vocab)
    #                 answer_comment_indices = get_indices(answer_comment.text, vocab)
    #                 # 如果问题和评论的相似度更高，那么就将评论视为答案
    #                 if get_similarity(question_indices, answer_comment_indices, word_embeddings) > get_similarity(
    #                         question_indices, answer_indices, word_embeddings):
    #                     answer = answer_comment.text
    #
    #             if first_edit_date == None or posthistory.edit_dates[i] < first_edit_date:
    #                 first_question, first_answer, first_edit_date = question, answer, posthistory.edit_dates[i]
    #
    #         if not first_question:
    #             continue
    #
    #         # 如果找到了第一个问题和对应的答案，那么就创建一个PostQuesAns对象，并将其添加到字典中
    #         self.post_ques_ans_dict[postId] = PostQuesAns(post.title, posthistory.initial_post, \
    #                                                       posthistory.initial_post_sents, first_question.text,
    #                                                       first_answer)
    #
    #     # 在处理完所有的帖子历史记录后，使用generate_using_comments方法处理那些没有被编辑过，但是有评论的帖子
    #     self.generate_using_comments(posts, question_comments, all_comments, vocab, word_embeddings)
    #
    #     # 最后，返回生成的字典
    #     return self.post_ques_ans_dict

