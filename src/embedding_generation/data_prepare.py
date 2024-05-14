# coding=utf-8
import json
import io  # 引入io模块来支持编码参数

# 定义文件路径
questions_file = "D:/KDiSE/EVPI/DATA/pre_questions.json"
comments_file = "D:/KDiSE/EVPI/DATA/pre_comments.json"
commentqs_file = "D:/KDiSE/EVPI/DATA/pre_commentqs.json"
histories_file = "D:/KDiSE/EVPI/DATA/pre_histories.json"
output_file = "D:/KDiSE/EVPI/ranking_clarification_questions/stackexchange/stackexchange_datadump.txt"

# 读取文件
with io.open(questions_file, 'r', encoding='utf-8') as f:
    questions = json.load(f)
with io.open(comments_file, 'r', encoding='utf-8') as f:
    comments = json.load(f)
with io.open(commentqs_file, 'r', encoding='utf-8') as f:
    commentqs = json.load(f)
with io.open(histories_file, 'r', encoding='utf-8') as f:
    histories = json.load(f)

# 写入新的文本文件
with io.open(output_file, 'w', encoding='utf-8') as f:
    for question_id in questions.keys():
        # 提取问题信息
        question_info = questions[question_id]
        f.write(u"{} {} {}\n".format(question_info['P-Title'], question_info['P-Body'], question_info['P-Tags']))

        # 提取评论信息
        if question_id in comments:
            for comment in comments[question_id]:
                f.write(u"{}\n".format(comment['P-Text']))

        # 提取评论问题信息
        if question_id in commentqs:
            for commentq in commentqs[question_id]:
                f.write(u"{}\n".format(commentq['P-CQ']))

        # 提取历史信息
        if question_id in histories:
            for edit in histories[question_id]['Edits']:
                f.write(u"{}\n".format(edit['Edit']))