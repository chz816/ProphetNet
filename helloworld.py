from metaflow import FlowSpec, step
import subprocess
from preprocess_cnn_dm import preocess

class HelloFlow(FlowSpec):
    """
    A flow where Metaflow prints 'Hi'.

    Run this flow to validate that Metaflow is installed correctly.

    """
    @step
    def start(self):
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.

        """
        print("Starting the flow.")
        self.next(self.preprocess)

    @step
    def preprocess(self):
        """
        A step for metaflow to introduce itself.

        """
        print("Hi! Start to preprocess the data!")
        preocess('cnndm/original_data/dev.article', 'cnndm/prophetnet_tokenized/valid.src', keep_sep=False)
        preocess('cnndm/original_data/dev.summary', 'cnndm/prophetnet_tokenized/valid.tgt', keep_sep=True)
        preocess('cnndm/original_data/test.article', 'cnndm/prophetnet_tokenized/test.src', keep_sep=False)
        preocess('cnndm/original_data/test.summary', 'cnndm/prophetnet_tokenized/test.tgt', keep_sep=True)
        preocess('cnndm/original_data/training.article', 'cnndm/prophetnet_tokenized/train.src', keep_sep=False)
        preocess('cnndm/original_data/training.summary', 'cnndm/prophetnet_tokenized/train.tgt', keep_sep=True)
        self.next(self.binary)
    @step
    def binary(self):
        """
        A step for change the text file to binary file
        """
        print("Hi! Starting to get the binary file!")
        subprocess.run(['./cnndm-data-preprocess.sh'], shell=True)
        self.next(self.generate)

    @step
    def generate(self):
        """
        A step for generating the output
        """
        print("Hi! Starting to generate the output!")
        subprocess.run(['./cnndm-data-generate.sh'], shell=True)
        self.next(self.evaluate)

    @step
    def evaluate(self):
        """
        A step for evaluation the performance
        """
        print("Hi! Starting to evaluate the performance!")
        subprocess.run(['./cnndm-evaluation.sh'], shell=True)
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.
        """
        print("Everything is all done.")


if __name__ == '__main__':
    HelloFlow()
