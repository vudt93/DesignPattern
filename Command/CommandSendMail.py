from Command.Command import Command


class CommandSendMail(Command):
    def __init__(self, mail_service):
        self.mail_service = mail_service

    def execute(self):
        self.mail_service.send_mail()
