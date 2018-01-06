from functools import wraps


class Log:
    """
    This is decarator for logging functions
    """

    def __init__(self, logger):
        self.logger = logger

    @staticmethod
    def _create_message(result=None, *args, **kwargs):
        """
        This method build body of logging message

        :return: one string
        """
        message = ''
        if args:
            message += 'args: {} '.format(args)
        if kwargs:
            message += 'kwargs: {} '.format(kwargs)
        if result:
            message += '= {}'.format(result)
        return message

    def __call__(self, func):
        """
        This is decarator realisation with class. There is use __call__ method
        :param func: its a function
        :return:
        """
        @wraps(func)
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            message = Log._create_message(result, *args, **kwargs)
            self.logger.info(message)
            return result
        return decorated
