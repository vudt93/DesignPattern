from Command.Command import Command


class CommandLogging(Command):
    def __init__(self, logging_service):
        self.logging_service = logging_service

    def execute(self):
        self.logging_service.log()
