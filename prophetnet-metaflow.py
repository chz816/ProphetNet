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
        A step for metaflow to preprocess the data
        """
        print("Hi! Start to preprocess the data!")

        preocess('./data/cnndm_data/org_data/dev.article', './data/cnndm_data/valid.src', keep_sep=False)
        preocess('./data/cnndm_data/org_data/dev.summary', './data/cnndm_data/valid.tgt', keep_sep=True)
        preocess('./data/cnndm_data/org_data/test.article', './data/cnndm_data/test.src', keep_sep=False)
        preocess('./data/cnndm_data/org_data/test.summary', './data/cnndm_data/test.tgt', keep_sep=True)
        preocess('./data/cnndm_data/org_data/training.article', './data/cnndm_data/train.src', keep_sep=False)
        preocess('./data/cnndm_data/org_data/training.summary', './data/cnndm_data/train.tgt', keep_sep=True)
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
