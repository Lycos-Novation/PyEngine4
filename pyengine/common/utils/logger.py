import logging
import logging.handlers


class Logger(logging.Logger):
    def __init__(self, name, stream=False, file=None):
        super(Logger, self).__init__(name)

        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', '%d/%m/%Y %H:%M:%S')

        if file is not None:

            self.file_handler = logging.FileHandler(file, "w", "utf-8")
            self.file_handler.setFormatter(self.formatter)
            self.addHandler(self.file_handler)
        else:
            self.file_handler = None

        if stream:
            self.stream_handler = logging.StreamHandler()
            self.stream_handler.setFormatter(self.formatter)
            self.addHandler(self.stream_handler)
        else:
            self.stream_handler = None

    def setLevel(self, level):
        super(Logger, self).setLevel(level)
        if self.stream_handler:
            self.stream_handler.setLevel(level)
        if self.file_handler:
            self.file_handler.setLevel(level)


build_logger = Logger("PyEngine4 - BUILD", True, "builds/build.log")
core_logger = Logger("PyEngine4 - Core", True)
