from Proxy.Remote import Remote


class RemoteProxy(Remote):
    def __init__(self, remote):
        self.remote = remote

    def get_data(self):
        print("Connect to remote")
        return self.remote.get_data()
