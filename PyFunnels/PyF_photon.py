import os
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