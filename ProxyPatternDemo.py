from Proxy.ConcreteRemote import ConcreteRemote
from Proxy.RemoteProxy import RemoteProxy
from Proxy.VirtualProxy import VirtualProxy

remote = ConcreteRemote()
remote_proxy = RemoteProxy(remote)

print(remote_proxy.get_data())

virtual_proxy = VirtualProxy("csv_data.csv")
print(virtual_proxy.get_file_content())
print(virtual_proxy.get_file_content())
