import xml.etree.ElementTree as ET

class PyFNmap:
    CAPABILITIES = ['domains', 'ips', 'tcp_sockets', 'udp_sockets']

    def __init__(self, 
        file, 
        list_domains = [],
        list_ips = [],
        list_tcp_sockets = [],
        list_udp_sockets = []
    ):
        self.file = file
        self.list_domains = list_domains
        self.list_ips = list_ips
        self.list_tcp_sockets = list_tcp_sockets
        self.list_udp_sockets = list_udp_sockets
        self.tree = ET.parse(self.file)
        self.root = self.tree.getroot()

    def domains(self): 
        for h in self.root.iter('hostname'):
            host = h.attrib.get("name")
            if host not in self.list_ips:
                self.list_domains.append(host)

    def ips(self): 
        for i in self.root.iter('address'):
            if "ipv" in i.attrib.get("addrtype"): #Avoids MAC addresses
                ip = i.attrib.get("addr")
                if ip not in self.list_ips:
                    self.list_ips.append(ip)

    def tcp_sockets(self):
        for child in self.root: #first level
            if child.tag == "host":
                for child2 in child[3]: #second level
                    for child3 in child2: # third level
                        if child3.attrib.get("state") == "open" and child2.attrib.get("protocol") == "tcp" :
                            socket = child[1].attrib.get("addr") + ":" + child2.attrib.get("portid")
                            if socket not in self.list_tcp_sockets:
                                self.list_tcp_sockets.append(socket)

    def udp_sockets(self):
        for child in self.root: #first level
            if child.tag == "host":
                for child2 in child[3]: #second level
                    for child3 in child2: # third level
                        if child3.attrib.get("state") == "open" and child2.attrib.get("protocol") == "udp" :
                            socket = child[1].attrib.get("addr") + ":" + child2.attrib.get("portid")
                            if socket not in self.list_udp_sockets:
                                self.list_udp_sockets.append(socket)