#!/usr/bin/env python
from Command.CommandLogging import CommandLogging
from Command.CommandSendMail import CommandSendMail
from Command.Invoke import Invoke
from Command.LoggingService import LoggingService
from Command.MailService import MailService

mail_service = MailService()
logging_service = LoggingService()

mail_command = CommandSendMail(mail_service)
logging_command = CommandLogging(logging_service)

invoke_send_mail = Invoke(mail_command)
invoke_logging = Invoke(logging_command)

invoke_send_mail.invoke_command()
invoke_logging.invoke_command()
