# Prerequisites

* Install numpy, nltk, BeautifulSoup 

# NOTE

* Data for the sites: askubuntu.com, unix.stackexchange.com & superuser.com can be found here: https://go.umd.edu/clarification_questions_dataset 

# Steps to generate data for any other site

1. Choose a sitename from the list of sites in https://archive.org/download/stackexchange. Let's say you chose 'academia.com'
2. Download the .7z file corresponding to the site i.e. academia.com.7z and unzip it under ranking_clarification_questions/stackexchange/
3. Set "SITENAME=academia.com" in ranking_clarification_questions/src/data_generation/run_data_generator.sh
4. cd ranking_clarification_questions; sh src/data_generation/run_data_generator.sh

This will create data/academia.com/post_data.tsv & data/academia.com/qa_data.tsv files

# 先决条件

* 安装 numpy, nltk, BeautifulSoup 

# 注意

* askubuntu.com, unix.stackexchange.com 和 superuser.com 网站的数据可以在这里找到：https://go.umd.edu/clarification_questions_dataset 

# 为任何其他网站生成数据的步骤

1. 从 https://archive.org/download/stackexchange 中的网站列表中选择一个网站名。假设你选择了 'academia.com'
2. 下载与该网站对应的 .7z 文件，即 academia.com.7z，并将其解压到 ranking_clarification_questions/stackexchange/ 下
3. 在 ranking_clarification_questions/src/data_generation/run_data_generator.sh 中设置 "SITENAME=academia.com"
4. cd ranking_clarification_questions; sh src/data_generation/run_data_generator.sh

这将会创建 data/academia.com/post_data.tsv 和 data/academia.com/qa_data.tsv 文件