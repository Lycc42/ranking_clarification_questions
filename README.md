# Repository information

This repository contains data and code for the paper below:

<i><a href="http://aclweb.org/anthology/P18-1255">
Learning to Ask Good Questions: Ranking Clarification Questions using Neural Expected Value of Perfect Information</a></i><br/>
Sudha Rao (raosudha@cs.umd.edu) and Hal Daumé III (hal@umiacs.umd.edu)<br/>
Proceedings of The 2018 Association of Computational Lingusitics (ACL 2018)

# Downloading data

* Download the clarification questions dataset from google drive here: https://go.umd.edu/clarification_questions_dataset
* cp clarification_questions_dataset/data ranking_clarification_questions/data

* Download word embeddings trained on stackexchange datadump here: https://go.umd.edu/stackexchange_embeddings
* cp stackexchange_embeddings/embeddings ranking_clarification_questions/embeddings

The above dataset contains clarification questions for these three sites of stackexchange: <br/>
1. askubuntu.com
2. unix.stackexchange.com
3. superuser.com

# Running model on data above

To run models on a combination of the three sites above, check ranking_clarification_questions/src/models/README

# Generating data for other sites

To generate clarification questions for a different site of stackexchange, check ranking_clarification_questions/src/data_generation/README

# Retrain stackexchange word embeddings 

To retrain word embeddings on a newer version of stackexchange datadump, check ranking_clarification_questions/src/embedding_generation/README

# Contact information

Please contact Sudha Rao (raosudha@cs.umd.edu) if you have any questions or any feedback.

存储库信息
此存储库包含以下论文的数据和代码：
学会提出好问题：使用完美信息的神经期望值对澄清问题进行排名 Sudha Rao （raosudha@cs.umd.edu） 和 Hal Daumé III （hal@umiacs.umd.edu）
2018 年计算语言学协会论文集 （ACL 2018）
下载数据
- 从谷歌云端硬盘下载澄清问题数据集：https://go.umd.edu/clarification_questions_dataset
- CP clarification_questions_dataset/data ranking_clarification_questions/data
- 在此处下载在 stackexchange datadump 上训练的词嵌入：https://go.umd.edu/stackexchange_embeddings
- cp stackexchange_embeddings/embeddings ranking_clarification_questions/embeddings
上面的数据集包含了 stackexchange 的这三个站点的澄清问题：
1. askubuntu.com
2. unix.stackexchange.com
3. superuser.com
根据上述数据运行模型
要在上述三个站点的组合上运行模型，请查看 ranking_clarification_questions/src/models/README
为其他站点生成数据
要为 stackexchange 的不同站点生成澄清问题，请查看 ranking_clarification_questions/src/data_generation/README
重新训练 stackexchange 词嵌入
要在较新版本的 stackexchange 数据转储上重新训练单词嵌入，请查看 ranking_clarification_questions/src/embedding_generation/README
联系方式
如果您有任何问题或任何反馈，请联系 Sudha Rao （raosudha@cs.umd.edu）。