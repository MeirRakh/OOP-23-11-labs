from abc import ABC, abstractmethod
class Logger(ABC):
    def header(self):
        print("=== LOG START ===")

    @abstractmethod
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        with open("log.txt", "a") as f:
            f.write(message + "\n")
        print("Message written to file")

class ConsoleLogger(Logger):
    def log(self, message):
        print("Console log:", message)

if __name__ == "main":
    console = ConsoleLogger()
    file_logger = FileLogger()

    console.header()
    console.log("Hello from console")

    file_logger.header()
    file_logger.log("Hello from file logger")