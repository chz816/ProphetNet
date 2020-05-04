SUFFIX=_ck9_pelt1.2_test_beam5
BEAM=5
LENPEN=1.2
CHECK_POINT=./log/cnndm/finetune_cnndm_checkpoints/prophetnet_large_160G_cnndm_model.pt
OUTPUT_FILE=./output/cnndm/output$SUFFIX.txt
SCORE_FILE=./output/cnndm/score$SUFFIX.txt

grep ^H $OUTPUT_FILE | cut -c 3- | sort -n | cut -f3- | sed "s/ ##//g" > ./output/cnndm/sort_hypo$SUFFIX.txt
python ./src/cnndm/eval/postprocess_cnn_dm.py --generated ./output/cnndm/sort_hypo$SUFFIX.txt --golden ./data/cnndm_data/org_data/test.summary > $SCORE_FILE