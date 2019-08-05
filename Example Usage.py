from PyFunnels import PyFunnels
#Specify the output file for each tool in a dictionary.
source_files = {
    "spiderfoot":"/path/to/file/spiderfoot.db",
    "recon_ng":"/path/to/file/recon-ng.db",
    "TheHarvester":"/path/to/file/theharvester.xml",
    "photon":"/path/to/file/photon_results/",
    "nmap":"/path/to/file/nmap_results.xml"
}
#Create a PyFunnels object.
PyF = PyFunnels.Funnel(source_files)
#Do something with it
domains = PyF.funnel_data("domains")
for d in domains:
    pass
