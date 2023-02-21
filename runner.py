
from processor import DeleteProcessor
import json
import configparser
import logging

def start_logging():
    """start logging
    """
    logging.basicConfig(level=logging.DEBUG)

def process():
    """main function to process files
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    directories = config['DEFAULT']['PATH_TO_DELETE']
    words_to_exclude = config['DEFAULT']['WORDS_TO_EXCLUDE']
    directories = json.loads(directories)
    words_to_exclude = json.loads(words_to_exclude)
    logging.info(f'directories to delete: {directories}')
    logging.info(f'words_to_exclude in paths: {words_to_exclude}')
    processor = DeleteProcessor(directories, words_to_exclude)
    processor.process()


if __name__ == '__main__':
    start_logging()
    process()