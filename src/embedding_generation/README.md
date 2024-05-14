# Prerequisite

* Download and compile GLoVE code from: https://nlp.stanford.edu/projects/glove/

# NOTE

* Word embeddings pretrained on stackexchange datadump (version year 2017) can be found here: https://go.umd.edu/stackexchange_embeddings 

# Steps to retrain word embeddings

1. Download all domains of stackexchange from: https://archive.org/download/stackexchange
2. Extract text from all Posts.xml, Comments.xml and PostHistory.xml
3. Save the combined data under: stackexchange/stackexchange_datadump.txt
4. cd ranking_clarification_questions; sh src/embedding_generation/run_glove.sh
5. cd ranking_clarification_questions; sh src/embedding_generation/run_create_we_vocab.sh

# 先决条件

* 从以下链接下载并编译 GLoVE 代码：https://nlp.stanford.edu/projects/glove/

# 注意

* 在 stackexchange 数据转储（2017年版本）上预训练的词嵌入可以在这里找到：https://go.umd.edu/stackexchange_embeddings 

# 重新训练词嵌入的步骤

1. 从以下链接下载 stackexchange 的所有领域：https://archive.org/download/stackexchange
2. 从所有的 Posts.xml，Comments.xml 和 PostHistory.xml 中提取文本
3. 将合并的数据保存在：stackexchange/stackexchange_datadump.txt
4. cd ranking_clarification_questions; sh src/embedding_generation/run_glove.sh
5. cd ranking_clarification_questions; sh src/embedding_generation/run_create_we_vocab.sh