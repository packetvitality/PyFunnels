from PyFunnels import PyFunnels
#Specify the output file for each tool in a dictionary.
source_files = {
    "spiderfoot":"/path/to/file/spiderfoot.db",
    "recon_ng":""/path/to/file/recon-ng-tester.db",
    "TheHarvester":"/path/to/file/theharvester-tester.xml",
    "photon":"/path/to/file/photon_results/",
    "nmap":"/path/to/file/nmap_results.xml"
}
#Create a PyFunnels object.
PyF = PyFunnels(source_files)
#Do something with it
print(PyF.funnel("domains"))
