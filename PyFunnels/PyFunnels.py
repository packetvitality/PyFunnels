from PyFunnels.PyF_nmap import PyFNmap
from PyFunnels.PyF_photon import PyFPhoton
from PyFunnels.PyF_recon_ng import PyFReconng
from PyFunnels.PyF_spiderfoot import PyFSpiderfoot
from PyFunnels.PyF_theharvester import PyFtheHarvester

class Funnel:
    REGISTERED_DATA_SOURCES = {
        'spiderfoot': PyFSpiderfoot,
        'recon_ng': PyFReconng,
        'theharvester': PyFtheHarvester,
        'nmap': PyFNmap,
        'photon': PyFPhoton
    }
    
    def __init__(self, sources=None):
        """
        Intiating the data sources
        """
        if sources: #Case for no sources is when providing the user help
            self.data_sources = []
            self.sources = sources
            for k, v in sources.items(): #Ensure the provided data sources are supported
                if k in self.REGISTERED_DATA_SOURCES:
                    self.data_sources.append(v)
    
    def funnel_data(self, data_point):
        """
        Aggregates the output of one or more tools.
        """
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

    def get_capabilities(self):
        capabilities = {}
        for k, v in self.REGISTERED_DATA_SOURCES.items():
            method = getattr(v, "CAPABILITIES" ) #Pull the capabilities listed in the tool class.
            tool = '{0}'.format(k)
            caps = method
            capabilities.update({tool : caps})
        return capabilities