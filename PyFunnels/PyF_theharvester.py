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
        for d in self.root.findall('host'):
            domain = d.find('hostname').text
            if domain not in self.list_domains:
                self.list_domains.append(domain)

    def ips(self):
        for i in self.root.findall('host'):
            ip = i.find('ip').text
            if ip not in self.list_ips:
                self.list_ips.append(ip)

    def emails(self):
        for e in self.root.findall('email'):
            email = e.text
            if email not in self.list_emails:
                self.list_emails.append(email)