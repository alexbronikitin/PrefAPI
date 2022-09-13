from ursinanetworking import *
from ursinanetworking.easyursinanetworking import *


class Server:
    def __init__(self, ip, port):
        self.server = UrsinaNetworkingServer(ip, port)
        self.easy = EasyUrsinaNetworkingServer(self.server)
        print(f"PrefAPI > Server was started, address: {ip}:{port}")
