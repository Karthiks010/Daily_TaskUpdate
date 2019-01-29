from xml.etree import ElementTree as et
from xml.dom import minidom

with open("fileData.txt") as fileRead:
   d = fileRead.readlines()
   date,time = [data.split('=')[1].split('\n')[0] for data in d ]
   print(date)
   print(time)

items = minidom.parse("dataXml.arxml")
dValue = items.getElementsByTagName('Category')
dValue[0].firstChild.data=date
dValue[1].firstChild.data=time
print("==================================================")
for dVal in dValue:
   print(dVal.firstChild.data)
    
items.writexml(open('dataXml.arxml','w'))









#ws = autosar.workspace()
#ws.loadXML('dataXml.arxml')

#for elem in ws['DataType'].elements:
  #print("%s : %s"%(elem.name),type(elem))

