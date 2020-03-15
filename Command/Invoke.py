class Invoke:
    def __init__(self, command):
        self.command = command

    def invoke_command(self):
        self.command.execute()
