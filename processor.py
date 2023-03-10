
import os
import logging

class DeleteProcessor:

    def __init__(self, directories: list, words_to_exclude: list):
        self.directories = directories
        self.words_to_exclude = words_to_exclude

    def show_dir(self, directory: str) -> list:
        """return list of files in directory

        Args:
            directory (str): directory to search

        Returns:
            list: list of files in directory
        """        

        list_files = []
        absolute_path = os.path.abspath(directory)
        for root, dirs, files in os.walk(absolute_path):
            for file in files:
                file_path = os.path.join(root, file)
                list_files.append(file_path)

        if len(list_files) == 0:
            logging.info(f'no files found in {directory}')
            return []
        
        logging.info(f'found {len(list_files)} files in {directory}')
        return list_files
    
        
    def get_video_format(self) -> list:
        """return list of video formats"""
        list_video_formats  = [
            'mp4',
            'mkv',
            'avi',
            'mov',
            'flv',
            'wmv',
            'webm',
            'avi',
        ]
        return list_video_formats
    
    def get_subtitles_format(self) -> list:

        list_subtitles_formats = [
            'srt',
            'sub',
            'vtt',
        ]
        return list_subtitles_formats
    
    def get_images_format(self) -> list:
        list_images_formats = [
            'jpg',
            'jpeg',
            'png',
            'gif',
            'bmp',
            'tiff',
            'svg',
        ]
        return list_images_formats
    
    def filter_paths(self, file_paths: list, words_to_exclude: list):
        """return list of paths without paths that contain any of the strings in words_to_exclude

        Args:
            file_paths (list): list of paths
            words_to_exclude (list): list of strings to exclude
        """
        filtered_paths = []
        for path in file_paths:
            if not any(exclude in path for exclude in words_to_exclude):
                if not path.endswith(tuple(self.get_video_format())) \
                and not path.endswith(tuple(self.get_subtitles_format())) \
                and not path.endswith(tuple(self.get_images_format())):
                    filtered_paths.append(path)

        if len(filtered_paths) == 0:
            logging.info('no files to delete')
        return filtered_paths
    

    def delete_files(self, file_paths: list):
        """delete files in file_paths

        Args:
            file_paths (list): list of paths
        """
        for path in file_paths:
            if os.path.isfile(path):
                os.remove(path)
                logging.info(f'deleted file: {path}')
            else:
                logging.info(f'file not found: {path}')
        
    
    def process(self):
        """main function to process files
        """


        file_paths = []
        for directory in self.directories:
            file_paths += self.show_dir(directory)
        file_paths = self.filter_paths(file_paths, self.words_to_exclude)
        self.delete_files(file_paths)
                

        


    
    