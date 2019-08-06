import sqlite3

class PyFSpiderfoot:
    BASE_SQL_QUERY = "SELECT data from tbl_scan_results WHERE `type` = '{}'"
    CAPABILITIES = ['domains', 'ips', 'emails', 'tcp_sockets', 'udp_sockets', 'urls']

    def __init__(self, 
        file, 
        list_domains = [],
        list_ips = [],
        list_emails = [],
        list_tcp_sockets = [],
        list_udp_sockets = [],
        list_urls = []
    ):
        self.file = file
        self.list_domains = list_domains
        self.list_ips = list_ips
        self.list_emails = list_emails
        self.list_tcp_sockets = list_tcp_sockets
        self.list_udp_sockets = list_udp_sockets
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

    def tcp_sockets(self):
        tcp_port_col_categories = [
            "TCP_PORT_OPEN",
            ]
        self._get_results_from_db(tcp_port_col_categories, self.list_tcp_sockets)

    def udp_sockets(self):
        udp_port_col_categories = [
            "UDP_PORT_OPEN",
            ]
        self._get_results_from_db(udp_port_col_categories, self.list_udp_sockets)

    def urls(self):
        url_col_categories = [
            "LINKED_URL_INTERNAL",
            "URL_STATIC",
            ]
        self._get_results_from_db(url_col_categories, self.list_urls)