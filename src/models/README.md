# Prerequisites

* Install lasagne: http://lasagne.readthedocs.io/en/latest/user/installation.html
* Install numpy, scipy
* Version information:

Python 2.7.5

Theano 0.9.0dev5

Lasagne 0.2.dev1

Cuda 8.0.44

Cudnn 5.1

# Loading data 

Load data from askubuntu.com

* Set "SITE_NAME=askubuntu.com" in ranking_clarification_questions/src/models/run_load_data.sh 
* cd ranking_clarification_questions; sh src/models/run_load_data.sh

Load data from unix.stackexchange.com

* Set "SITE_NAME=unix.stackexchange.com" in ranking_clarification_questions/src/models/run_load_data.sh 
* cd ranking_clarification_questions; sh src/models/run_load_data.sh

Load data from superuser.com

* Set "SITE_NAME=superuser.com" in ranking_clarification_questions/src/models/run_load_data.sh 
* cd ranking_clarification_questions; sh src/models/run_load_data.sh

Combine data from three domains

* cd ranking_clarification_questions; sh src/models/run_combine_domains.sh
* cat data/askubuntu.com/human_annotations data/unix.stackexchange.com/human_annotations data/superuser.com/human_annotations > askubuntu_unix_superuser/human_annotations

# Running neural baselines on the combined data

Neural(p,q)

* Set "MODEL=baseline_pq" in ranking_clarification_questions/src/models/run_main.sh
* cd ranking_clarification_questions; sh src/models/run_main.sh

Neural(p,a)

* Set "MODEL=baseline_pa" in ranking_clarification_questions/src/models/run_main.sh
* cd ranking_clarification_questions; sh src/models/run_main.sh

Neural(p,q,a)

* Set "MODEL=baseline_pqa" in ranking_clarification_questions/src/models/run_main.sh
* cd ranking_clarification_questions; sh src/models/run_main.sh

# Runing EVPI model on the combined data

* Set "MODEL=evpi" in ranking_clarification_questions/src/models/run_main.sh
* cd ranking_clarification_questions; sh src/models/run_main.sh

# Running evaluation

* cd ranking_clarification_questions; sh src/evaluation/run_evaluation.sh

# 先决条件

* 安装lasagne：http://lasagne.readthedocs.io/en/latest/user/installation.html
* 安装numpy，scipy
* 版本信息：

Python 2.7.5

Theano 0.9.0dev5

Lasagne 0.2.dev1

Cuda 8.0.44

Cudnn 5.1

# 加载数据 

从askubuntu.com加载数据

* 在ranking_clarification_questions/src/models/run_load_data.sh中设置 "SITE_NAME=askubuntu.com" 
* cd ranking_clarification_questions; sh src/models/run_load_data.sh

从unix.stackexchange.com加载数据

* 在ranking_clarification_questions/src/models/run_load_data.sh中设置 "SITE_NAME=unix.stackexchange.com" 
* cd ranking_clarification_questions; sh src/models/run_load_data.sh
// ; 是命令分隔符，用于在一行中运行多个命令。sh src/models/run_load_data.sh 是运行 run_load_data.sh 脚本的命令

从superuser.com加载数据

* 在ranking_clarification_questions/src/models/run_load_data.sh中设置 "SITE_NAME=superuser.com" 
* cd ranking_clarification_questions; sh src/models/run_load_data.sh

合并来自三个域的数据

* cd ranking_clarification_questions; sh src/models/run_combine_domains.sh
* cat data/askubuntu.com/human_annotations data/unix.stackexchange.com/human_annotations data/superuser.com/human_annotations > askubuntu_unix_superuser/human_annotations

# 在合并数据上运行神经基线

Neural(p,q)

* 在ranking_clarification_questions/src/models/run_main.sh中设置 "MODEL=baseline_pq"
* cd ranking_clarification_questions; sh src/models/run_main.sh

Neural(p,a)

* 在ranking_clarification_questions/src/models/run_main.sh中设置 "MODEL=baseline_pa"
* cd ranking_clarification_questions; sh src/models/run_main.sh

Neural(p,q,a)

* 在ranking_clarification_questions/src/models/run_main.sh中设置 "MODEL=baseline_pqa"
* cd ranking_clarification_questions; sh src/models/run_main.sh

# 在合并数据上运行EVPI模型

* 在ranking_clarification_questions/src/models/run_main.sh中设置 "MODEL=evpi"
* cd ranking_clarification_questions; sh src/models/run_main.sh

# 运行评估

* cd ranking_clarification_questions; sh src/evaluation/run_evaluation.sh