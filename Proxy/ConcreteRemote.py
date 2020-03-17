from Proxy.Remote import Remote


class ConcreteRemote(Remote):
    def get_data(self):
        return "Data"
