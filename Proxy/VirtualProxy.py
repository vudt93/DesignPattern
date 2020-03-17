from Proxy.ConcreteResource import ConcreteResource
from Proxy.Resource import Resource


class VirtualProxy(Resource):
    def __init__(self, file_name):
        self.resource = None
        self.file_name = file_name

    def get_file_content(self):
        if self.resource is None:
            print("Start loading resource")
            self.resource = ConcreteResource(self.file_name)

        return self.resource.get_file_content()
