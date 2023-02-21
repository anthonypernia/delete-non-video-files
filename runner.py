
from processor import DeleteProcessor
import json
import configparser

def process():
    """main function to process files
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    directories = config['DEFAULT']['PATH_TO_DELETE']
    words_to_exclude = config['DEFAULT']['WORDS_TO_EXCLUDE']
    directories = json.loads(directories)
    words_to_exclude = json.loads(words_to_exclude)

    processor = DeleteProcessor(directories, words_to_exclude)
    processor.process()


if __name__ == '__main__':
    process()