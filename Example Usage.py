from PyFunnels import PyFunnels

PyF = PyFunnels.Funnel()
capabilities = PyF.get_capabilities()
print(capabilities)

#Specify the output file for each tool in a dictionary.
source_files = {
   "spiderfoot":"/path/to/file/spiderfoot.db",
   "nmap":"/path/to/file/nmap_results.xml"
   "TheHarvester":"/path/to/file/theharvester-tester.xml",
}
#Create a PyFunnels object.
PyF = PyFunnels.Funnel(source_files)
#Do something with it
domains = PyF.funnel_data("domains")
for d in domains:
   pass #Your use case here.
