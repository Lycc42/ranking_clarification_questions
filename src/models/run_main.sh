#!/bin/bash

#source /fs/clip-amr/gpu_virtualenv/bin/activate
#source source C:/Users/Student/.conda/envs/ranking_clarification_questions/bin/activate # activate the environment
#source C:/ProgramData/anaconda3/etc/profile.d/conda.sh
#source /cygdrive/c/ProgramData/anaconda3/etc/profile.d/conda.sh
#source /c/ProgramData/anaconda3/etc/profile.d/conda.sh
#conda activate ranking_clarification_questions

DATA_DIR=data
#EMB_DIR=embeddings
EMB_DIR=D:/KDiSE/EVPI/GloVe-1.2
#SITE_NAME=askubuntu.com
#SITE_NAME=unix.stackexchange.com
#SITE_NAME=superuser.com
SITE_NAME=askubuntu_unix_superuser

OUTPUT_DIR=output
SCRIPTS_DIR=src/models
#MODEL=baseline_pq
#MODEL=baseline_pa
#MODEL=baseline_pqa
MODEL=evpi

mkdir -p $OUTPUT_DIR



#module add cuda/8.0.4
#module add cudnn/v7.1.4

#THEANO_FLAGS=floatX=float32,device=gpu python $SCRIPTS_DIR/main.py \
# shellcheck disable=SC2125
THEANO_FLAGS=floatX=float32,device=gpu,optimizer=fast_compile python $SCRIPTS_DIR/main.py \
                                                --post_ids_train $DATA_DIR/$SITE_NAME/post_ids_train.p \
                                                --post_vectors_train $DATA_DIR/$SITE_NAME/post_vectors_train.p \
												--ques_list_vectors_train $DATA_DIR/$SITE_NAME/ques_list_vectors_train.p \
												--ans_list_vectors_train $DATA_DIR/$SITE_NAME/ans_list_vectors_train.p \
                                                --post_ids_test $DATA_DIR/$SITE_NAME/post_ids_test.p \
                                                --post_vectors_test $DATA_DIR/$SITE_NAME/post_vectors_test.p \
												--ques_list_vectors_test $DATA_DIR/$SITE_NAME/ques_list_vectors_test.p \
												--ans_list_vectors_test $DATA_DIR/$SITE_NAME/ans_list_vectors_test.p \
												--word_embeddings $EMB_DIR/word_embeddings.p \
                                                --batch_size 128 --no_of_epochs 20 --no_of_candidates 10 \
												--test_predictions_output $DATA_DIR/$SITE_NAME/test_predictions_${MODEL}.out \
												--stdout_file $OUTPUT_DIR/${SITE_NAME}.${MODEL}.out \
												--model $MODEL \
