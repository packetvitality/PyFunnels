# PyFunnels

The goal of PyFunnels is to create a collaborative code library which makes integrating data into automated workflows easier. The library acts as a centralized location where everyone can contribute and use code. 

PyFunnels consists of multiple classes structured modularly so that additional tools and data points can be easily added and work independently of one another. The classes within the library can be thought of as a catalog of tools and methods to retrieve data. Not all data point methods are required for each tool, meaning a new tool can be added with only a single method. Ideally, all data points would be supported for each tool but this structure allows the functionality to grow organically and makes it easy to contribute code to the project. 

![](name-of-giphy.gif)

The library reduces the time it takes information security professionals to utilize output from tools. For example, consider the following workflow:
1.	Collect data with tool one.
2.	Collect data with tool two.
3.	Write code to isolate the data for tool one.
4.	Write code to isolate and data for tool two. 
5.	Merge data into a standard format.
6.	Remove duplicated data.
7.	Expose normalized data.

To summarize, this workflow can be reduced to the following using PyFunnels:
1.	Specify output files
2.	Initiate an object.
3.	Use method on the object.
4.	Expose normalized data.

PyFunnels has been purposely structured for ease of use and extensibility to new tools and data points. Users of the library are encouraged to contribute code for new tools and data points they find useful. Whenever a user creates Python3 code to isolate data from the output of a tool, he or she is encouraged to commit that code to PyFunnels so others in the community can use it as well.
