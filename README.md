# ProphetNet

This repo modifies the original repo for [*ProphetNet: Predicting Future N-gram for Sequence-to-Sequence Pre-training*](https://arxiv.org/pdf/2001.04063).

Link for original repo: https://github.com/microsoft/ProphetNet



## Local Setup

Tested with Python 3.7 via virtual environment. 

Clone the repo, go to the repo folder, setup the virtual environment, and install the required packages:

```bash
$ python3.7 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```



## Data

```
$ gdown --id 1jiDbDbAsqy_5BM79SmX6aSu5DQVCAZq1 --output data.zip
$ unzip data.zip
$ mv cnndm ./data/cnndm
```

