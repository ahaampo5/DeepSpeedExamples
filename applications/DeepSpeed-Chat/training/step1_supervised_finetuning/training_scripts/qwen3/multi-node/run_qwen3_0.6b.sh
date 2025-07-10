#!/bin/bash
# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team
export NCCL_DEBUG=WARN
export NCCL_DEBUG_SUBSYS=ALL
# export CUDA_LAUNCH_BLOCKING=1
export NCCL_TIMEOUT=6000

BATCH_SIZE=1
ACCUMULATION_STEPS=16
MAX_LENGTH=16384
NUM_GPUS=16
TARGET=ko_en_zh

export WANDB_PROJECT="foundationModel"
export WANDB_NAME="0.6B_b_$BATCH_SIZE*$ACCUMULATION_STEPS*$NUM_GPUS-$MAX_LENGTH-$TARGET" # 6*2=12
export WANDB_NOTES="Smaller learning rate, more regularization."

OUTPUT=$1
ZERO_STAGE=$2
if [ "$OUTPUT" = "" ]; then
    OUTPUT=./output_step1_qwen3_0.6b
fi
if [ "$ZERO_STAGE" = "" ]; then
    ZERO_STAGE=1
fi
mkdir -p $OUTPUT

deepspeed --hostfile=hostfile --num_nodes 2 main.py \
   --data_path mncai/foundation_model_smoltalk_ko_translate mncai/foundation_model_smoltalk_zh_translate HuggingFaceTB/smoltalk \
   --data_name default default all \
   --data_split 1,0,0 \
   --model_name_or_path Qwen/Qwen3-0.6B \
   --per_device_train_batch_size $BATCH_SIZE \
   --per_device_eval_batch_size $BATCH_SIZE \
   --max_seq_len $MAX_LENGTH \
   --learning_rate 9.65e-6 \
   --weight_decay 0. \
   --num_train_epochs 1 \
   --gradient_accumulation_steps $ACCUMULATION_STEPS \
   --lr_scheduler_type cosine \
   --num_warmup_steps 500 \
   --seed 1234 \
   --gradient_checkpointing \
   --zero_stage $ZERO_STAGE \
   --deepspeed \
   --output_dir $OUTPUT \
   --dtype bf16 \
   > $OUTPUT/training.log

#    --offload \