import logging

def create_logger(path):
    logger = logging.getLogger(path)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(path)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S'))
    logger.addHandler(handler)
    return logger

def logger(path):
    logger = create_logger(path)
    def __logger(old_function):
        def new_function(*args, **kwargs):
            logger.debug(f'Function: {old_function.__name__}, Arguments: {args}, {kwargs}')

            result = old_function(*args, **kwargs)

            logger.debug(f'Output: {None}')
            return result
        
        return new_function

    return __logger