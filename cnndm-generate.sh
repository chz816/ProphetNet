SUFFIX=_ck9_pelt1.2_test_beam5
BEAM=5
LENPEN=1.2
CHECK_POINT=./log/cnndm/finetune_cnndm_checkpoints/prophetnet_large_160G_cnndm_model.pt
OUTPUT_FILE=./output/cnndm/output$SUFFIX.txt
SCORE_FILE=./output/cnndm/score$SUFFIX.txt

fairseq-generate ./data/cnndm_data/processed --path $CHECK_POINT --user-dir ./src/prophetnet --task translation_prophetnet --batch-size 8 --gen-subset test --beam $BEAM --num-workers 4 --min-len 45 --max-len-b 50 --no-repeat-ngram-size 3 --lenpen $LENPEN 2>&1 > $OUTPUT_FILE
