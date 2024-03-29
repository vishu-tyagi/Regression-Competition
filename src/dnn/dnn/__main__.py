import sys
import logging

from dnn.api import train


if __name__ == "__main__":
    FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.INFO)
    try:
        if sys.argv[1] == "train":
            train()
    except IndexError:
        raise ValueError("Call to API requires an endpoint")
