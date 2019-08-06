import sqlite3

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