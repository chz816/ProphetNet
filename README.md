# ProphetNet

This repo modifies the [original repo](https://github.com/microsoft/ProphetNet) for [*ProphetNet: Predicting Future N-gram for Sequence-to-Sequence Pre-training*](https://arxiv.org/pdf/2001.04063).

Link for original repo: https://github.com/microsoft/ProphetNet



## Local Setup

Tested with Python 3.7 via virtual environment. 

Clone the repo, go to the repo folder, setup the virtual environment, and install the required packages:

```bash
$ python3.7 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```



## Data - CNN/Daily Mail

### Download

The data can be downloaded [here](https://drive.google.com/file/d/1jiDbDbAsqy_5BM79SmX6aSu5DQVCAZq1/view). To run this program, you need to put the data files into the following directory: ```/data/cnndm_data/yourdata.zip```.

Also you can directly run the following command to download the data.

```bash
$ mkdir data
$ cd data
$ mkdir cnndm_data
$ cd cnndm_data
$ gdown --id 1jiDbDbAsqy_5BM79SmX6aSu5DQVCAZq1 --output data.zip
$ unzip data.zip
```

### Data Preprocessing

After downloading the data, firstly we run ```preprocess_cnn_dm.py``` to tokenize CNN/DailyMail data.

```bash
$ python preprocess_cnn_dm.py
```

Then we need to generate the binary data files.

```bash
$ chmod +x cnndm-data-preprocess.sh
$ ./cnndm-data-preprocess.sh
```

### Fine-tune

```bash
$ chmod +x cnndm-fine-tuning.sh
$ ./cnndm-fine-tuning.sh
```

### Evaluation & Inference

To generate the result:

```bash
$ chmod +x cnndm-generate.sh
$ ./cnndm-generate.sh
```

To evaluate the result

```bash
$ chmod +x cnndm-evaluation.sh
$ /cnndm-evaluation.sh
```



## Evaluation Result

Here is the evaluation result I got for CNN/DM dataset:

```
---------------------------------------------
1 ROUGE-1 Average_R: 0.37606 (95%-conf.int. 0.37373 - 0.37846)
1 ROUGE-1 Average_P: 0.49294 (95%-conf.int. 0.48986 - 0.49598)
1 ROUGE-1 Average_F: 0.41450 (95%-conf.int. 0.41220 - 0.41674)
---------------------------------------------
1 ROUGE-2 Average_R: 0.18094 (95%-conf.int. 0.17857 - 0.18315)
1 ROUGE-2 Average_P: 0.24029 (95%-conf.int. 0.23736 - 0.24321)
1 ROUGE-2 Average_F: 0.20032 (95%-conf.int. 0.19788 - 0.20275)
---------------------------------------------
1 ROUGE-L Average_R: 0.35153 (95%-conf.int. 0.34924 - 0.35386)
1 ROUGE-L Average_P: 0.46082 (95%-conf.int. 0.45789 - 0.46372)
1 ROUGE-L Average_F: 0.38751 (95%-conf.int. 0.38526 - 0.38971)

>> ROUGE-F(1/2/l): 41.45/20.03/38.75
ROUGE-R(1/2/3/l): 37.61/18.09/35.15
```



## For ```pyrouge```

If you meet any problems related to ```pyrouge```, you can refer to this useful [solution](https://stackoverflow.com/questions/45894212/installing-pyrouge-gets-error-in-ubuntu).

