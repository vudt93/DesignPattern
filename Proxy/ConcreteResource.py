from Proxy.Resource import Resource


class ConcreteResource(Resource):
    def __init__(self, file_name):
        self.file_name = file_name

    def get_file_content(self):
        print("Load file " + self.file_name)
        return "CSV File Content Result"
