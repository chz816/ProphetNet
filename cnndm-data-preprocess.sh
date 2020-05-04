fairseq-preprocess \
  --user-dir ./src/prophetnet \
  --task translation_prophetnet \
  --source-lang src --target-lang tgt \
  --trainpref ./data/cnndm_data/train --validpref ./data/cnndm_data/valid --testpref ./data/cnndm_data/test \
  --destdir ./data/cnndm_data/processed --srcdict ./src/vocab.txt --tgtdict ./src/vocab.txt \
  --workers 20