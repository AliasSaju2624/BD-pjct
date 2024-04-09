import logging

class BaseClass:
    def get_logger(self, logger_name):
        log = logging.getLogger(logger_name)
        fileHandler = logging.FileHandler('absolute/path/to/logfile.log')  # Specify absolute path
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        log.addHandler(fileHandler)
        log.setLevel(logging.INFO)  # Adjust logging level as needed
        return log
