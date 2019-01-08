import sqlite3
import xml.etree.ElementTree as ET
import os

class PyFSpiderfoot:
    BASE_SQL_QUERY = "SELECT data from tbl_scan_results WHERE `type` = '{}'"
    CAPABILITIES = ['domains', 'ips', 'emails', 'tcp_ports', 'udp_ports', 'urls']

    def __init__(self, 
        file, 
        list_domains = [],
        list_ips = [],
        list_emails = [],
        list_tcp_ports = [],
        list_udp_ports = [],
        list_urls = []
    ):
        self.file = file
        self.list_domains = list_domains
        self.list_ips = list_ips
        self.list_emails = list_emails
        self.list_tcp_ports = list_tcp_ports
        self.list_udp_ports = list_udp_ports
        self.list_urls = list_urls
        
    def _get_results_from_db(self, category_names, storage_attribute):
        conn = sqlite3.connect(self.file)
        for category in category_names: 
            cursor = conn.execute(self.BASE_SQL_QUERY.format(category))
            for row in cursor:
                if row[0] not in storage_attribute:
                    storage_attribute.append(row[0])
        conn.close()

    def domains(self):
        domain_col_names = ["INTERNET_NAME", "SIMILARDOMAIN"]
        self._get_results_from_db(domain_col_names, self.list_domains)

    def ips(self):
        ip_col_categories = [
            "AFFILIATE_IPADDR",
            "IP_ADDRESS",
            ]
        self._get_results_from_db(ip_col_categories, self.list_ips)

    def emails(self):
        email_col_categories = [
            "EMAILADDR",
            ]
        self._get_results_from_db(email_col_categories, self.list_emails)

    def tcp_ports(self):
        tcp_port_col_categories = [
            "TCP_PORT_OPEN",
            ]
        self._get_results_from_db(tcp_port_col_categories, self.list_tcp_ports)

    def udp_ports(self):
        udp_port_col_categories = [
            "UDP_PORT_OPEN",
            ]
        self._get_results_from_db(udp_port_col_categories, self.list_udp_ports)

    def urls(self):
        url_col_categories = [
            "LINKED_URL_INTERNAL",
            "URL_STATIC",
            ]
        self._get_results_from_db(url_col_categories, self.list_urls)

class PyFReconng:
    BASE_SQL_QUERY = "SELECT {} from {}"
    CAPABILITIES = ['domains', 'ips', 'emails']

    def __init__(self, 
        file, 
        list_domains = [],
        list_ips =  [],
        list_emails = []
    ):
        self.file = file
        self.list_domains = list_domains
        self.list_ips = list_ips
        self.list_emails = list_emails

    def _get_results_from_db(self, col, table, storage_attribute):
        conn = sqlite3.connect(self.file)
        cursor = conn.execute(self.BASE_SQL_QUERY.format(col, table))
        for row in cursor:
            if row[0] not in storage_attribute:
                storage_attribute.append(row[0])
        conn.close()

    def domains(self):
        self._get_results_from_db("host", "hosts", self.list_domains)

    def ips(self):
        self._get_results_from_db("ip_address", "hosts", self.list_ips)
 
    def emails(self):
        self._get_results_from_db("email", "contacts", self.list_emails)

class PyFtheHarvester:
    CAPABILITIES = ['domains', 'ips', 'emails']

    def __init__(self, 
        file, 
        list_domains = [],
        list_ips = [],
        list_emails = []
    ):
        self.file = file
        self.list_domains = list_domains
        self.list_ips = list_ips
        self.list_emails = list_emails
        self.tree = ET.parse(self.file)
        self.root = self.tree.getroot()

    def domains(self):
        for child in self.root:
            if child.tag == "host":
                if child[1].tag == "hostname":
                    if child[1].text not in self.list_domains:
                        self.list_domains.append(child[1].text)

    def ips(self):
        for child in self.root:
            if child.tag == "host":
                if child[0].tag == "ip":
                    if child[0].text not in self.list_ips:
                        self.list_ips.append(child[0].text)

    def emails(self):
        for child in self.root:
            if child.tag == "email":
                if child.text not in self.list_emails:
                    self.list_emails.append(child.text)

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

class PyFPhoton:
    CAPABILITIES = ['domains', 'emails']

    def __init__(self, 
        file, 
        list_domains= [],
        list_emails = []
    ):
        self.file = file
        self.list_domains = list_domains
        self.list_emails = list_emails

    def domains(self):
        for f in os.listdir(self.file):
            if f == "subdomains.txt":
                f_path = self.file + f
                with open(f_path, 'r') as domain_file:
                    for domain in domain_file:
                        if domain.rstrip() not in self.list_domains:
                            self.list_domains.append(domain.rstrip())

    def emails(self):
        for f in os.listdir(self.file):
            if f == "intel.txt":
                f_path = self.file + f
                with open(f_path, 'r') as email_file:
                    for email in email_file:
                        if "@" in email:
                            if email not in self.list_emails:
                                self.list_emails.append(email)

class PyFunnels:
    REGISTERED_DATA_SOURCES = {
        'spiderfoot': PyFSpiderfoot,
        'recon_ng': PyFReconng,
        'theharvester': PyFtheHarvester,
        'nmap': PyFNmap,
        'photon': PyFPhoton
    }
    
    def __init__(self, sources):
        """
        Intiating the data sources
        """
        self.data_sources = []
        self.sources = sources
        for k, v in sources.items(): #Ensure the provided data sources are supported
            if k in self.REGISTERED_DATA_SOURCES:
                self.data_sources.append(v)
    
    def funnel(self, data_point):
        storage_attribute = set()
        for k, v in self.sources.items():
            data_source_object = self.REGISTERED_DATA_SOURCES[k.lower()](v) #Tool class being worked on
            if data_point in data_source_object.CAPABILITIES: #Ensure the data point is supported by the tool
                method = getattr(data_source_object, data_point) #pass in the tool class and method
                method()
                list_data_point = getattr(data_source_object, "list_" + data_point)
                for data in list_data_point:
                    storage_attribute.add(data)
        if storage_attribute:
            return storage_attribute