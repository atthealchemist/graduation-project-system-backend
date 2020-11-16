import logging


class ConsoleLogger:

    handlers = [
        (logging.StreamHandler,
         dict(),
         "[%(name)s]\t %(asctime)s [%(levelname)s] %(message)s ",
         logging.DEBUG)
    ]

    def set_level(self, level):
        self.logger.setLevel(level)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def exception(self, message):
        self.logger.exception(message)

    def __init__(self, name=__name__, default_level=logging.DEBUG):
        self.logger = logging.Logger(name)
        if not self.logger.handlers or len(self.logger.handlers) < 1:
            for handler_class, params, formatted, level in self.handlers:
                handler = handler_class(**params)
                handler.setFormatter(logging.Formatter(formatted))
                handler.setLevel(level if not default_level else default_level)

                self.logger.addHandler(handler)
