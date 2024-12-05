import os
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

            logger.debug(f'Output: {result}')
            return result
        
        return new_function

    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    current_path = None
    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)
        current_path = path
    
    assert os.path.exists(current_path), f'файл {current_path} должен существовать'

    with open(current_path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'

    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()
