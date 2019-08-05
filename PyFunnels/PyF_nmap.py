import xml.etree.ElementTree as ET

class PyFNmap:
    CAPABILITIES = ['domains', 'ips', 'tcp_ports', 'udp_ports']

    def __init__(self, 
        file, 
        list_domains = [],
        list_ips = [],
        list_tcp_ports = [],
        list_udp_ports = []
    ):
        self.file = file
        self.list_domains = list_domains
        self.list_ips = list_ips
        self.list_tcp_ports = list_tcp_ports
        self.list_udp_ports = list_udp_ports
        self.tree = ET.parse(self.file)
        self.root = self.tree.getroot()

    def domains(self):
        for child in self.root:
            if child.tag == "host":
                for child2 in child[2]:
                    if child2.attrib.get("name") not in self.list_domains:
                        self.list_domains.append(child2.attrib.get("name"))

    def ips(self):
        for child in self.root:
            if child.tag == "host":
                if child[0].attrib.get("state") == "up":
                    if child[1].attrib.get("addr") not in self.list_ips:
                        self.list_ips.append(child[1].attrib.get("addr"))

    def tcp_ports(self):
        for child in self.root: #first level
            if child.tag == "host":
                for child2 in child[3]: #second level
                    for child3 in child2: # third level
                        if child3.attrib.get("state") == "open" and child2.attrib.get("protocol") == "tcp" :
                            socket = child[1].attrib.get("addr") + ":" + child2.attrib.get("portid")
                            if socket not in self.list_tcp_ports:
                                self.list_tcp_ports.append(socket)

    def udp_ports(self):
        for child in self.root: #first level
            if child.tag == "host":
                for child2 in child[3]: #second level
                    for child3 in child2: # third level
                        if child3.attrib.get("state") == "open" and child2.attrib.get("protocol") == "udp" :
                            socket = child[1].attrib.get("addr") + ":" + child2.attrib.get("portid")
                            if socket not in self.list_udp_ports:
                                self.list_udp_ports.append(socket)