from functools import wraps


class Log:
    """
    Класс декоратор для логирования функций
    """

    def __init__(self, logger):
        self.logger = logger

    @staticmethod
    def _create_message(result=None, *args, **kwargs):
        message = ''
        if args:
            message += 'args: {} '.format(args)
        if kwargs:
            message += 'kwargs: {} '.format(kwargs)
        if result:
            message += '= {}'.format(result)
        return message

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            message = Log._create_message(result, *args, **kwargs)
            self.logger.info(message)
            return result
        return decorated
