fairseq-preprocess \
  --user-dir ./prophetnet \
  --task translation_prophetnet \
  --source-lang src --target-lang tgt \
  --trainpref ./data/cnndm_data/train --validpref ./data/cnndm_data/valid --testpref ./data/cnndm_data/test \
  --destdir ./data/cnndm_data/processed --srcdict ./vocab.txt --tgtdict ./vocab.txt \
  --workers 20