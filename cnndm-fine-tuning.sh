DATA_DIR=./data/cnndm_data/processed
USER_DIR=./src/prophetnet
ARCH=ngram_transformer_prophet_large
CRITERION=ngram_language_loss
SAVE_DIR=./log/cnndm/finetune_cnndm_checkpoints
TENSORBOARD_LOGDIR=./log/cnndm/finetune_cnndm_tensorboard
PRETRAINED_MODEL=./pretrain/prophetnet_large_pretrained_16G_64epoch_model.pt

fairseq-train \
--fp16 \
--user-dir $USER_DIR --task translation_prophetnet --arch $ARCH \
--optimizer adam --adam-betas '(0.9, 0.999)' --clip-norm 0.1 \
--lr 0.0001 \
--lr-scheduler inverse_sqrt --warmup-init-lr 1e-07 --warmup-updates 1000 \
--dropout 0.1 --attention-dropout 0.1 --weight-decay 0.01 \
--criterion $CRITERION --label-smoothing 0.1 \
--update-freq 32  --max-sentences 2 \
--num-workers 4 \
--load-from-pretrained-model $PRETRAINED_MODEL \
--load-sep \
--ddp-backend=no_c10d --max-epoch 10 \
--max-source-positions 128 --max-target-positions 128 \
--skip-invalid-size-inputs-valid-test \
--seed 1 \
--save-dir $SAVE_DIR \
--keep-last-epochs 10 \
--tensorboard-logdir $TENSORBOARD_LOGDIR \
$DATA_DIR