import xml.etree.ElementTree as ET
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