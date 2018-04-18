#!/usr/bin/env python
# coding= utf-8

import csv

#csvFile = 'SYMP.csv'
#xmlFile = 'Symptoms.xml'

#csvFile = 'CSSO1.csv'
#xmlFile = 'signs.xml'


csvFile = 'COPDO.csv'
xmlFile = 'copd.xml'


#elementName= 'Symptoms'
#restrictionName = 'Symptom'
#attributeName = "Category"

#import io
#with io.open(csvFile,'r',encoding='utf8') as f:
#   csvData = csv.reader(f)



csvData = csv.reader(open(csvFile,'r',encoding='utf8'))
xmlData = open(xmlFile, 'w')

xmlData.write('<?xml version = "1.0"?>' + "\n")
xmlData.write('<schema xmlns="http://www.w3.org/2000/10/XMLSchema">' + "\n")
xmlData.write('<!-- XSchema definition for COPD-->' + "\n")
#xmlData.write('<element name= "Symptoms" >' + "\n")
xmlData.write('<element name= "COPD" >' + "\n")



xmlData.write('    ' +'<complexType>' + "\n")
xmlData.write('    ' +'    ' +'<attribute name = "Category" use="optional">'+ "\n")
xmlData.write('    ' +'    ' +'    ' +'<simpleType>'+ "\n")
#xmlData.write('    ' +'    ' +'    ' +'<restriction base= "Symptom">' + "\n")
xmlData.write('    ' +'    ' +'    ' +'<restriction base= "COPD">' + "\n")

#print(csvData.encode('utf-8').strip())

for row in csvData:
    xmlData.write('    ' +'    ' +'    ' +'    ' +'<enumeration value = "'+ row[1] + '"/>'+ "\n")

xmlData.write('    ' +'    ' +'</restriction>' + "\n")
xmlData.write('    ' +'    ' +'    ' + '</simpleType>' + "\n")
xmlData.write('    ' +'    ' +'    ' + '</attribute>' + "\n")
xmlData.write('    ' +'</complexType>' + "\n")
xmlData.write('</element>' + "\n")

xmlData.write('</schema>' + "\n")


'''
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(0, 2):
            tags[i] = tags[i].replace(' ', '_')

        else:
            for i in range(0, 2):
                xmlData.write('    ' + '<' + tags[i] + '>' \
                      + row[i] + '</' + tags[i] + '>' + "\n")
'''


 
                          #rowNum +=1





'''
xmlData.write('<?xml version="1.0" encoding="utf-8"?>' + "\n")
# there must be only one top-level tag
xmlData.write('<Catchment xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">' + "\n")
xmlData.write('<CatchmentParamters>' + "\n")
rowNum = 0


for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(0, 2):
            tags[i] = tags[i].replace(' ', '_')

    else: 
      for i in range(0, 2):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")

      xmlData.write('</CatchmentParameters>' + "\n")
      xmlData.write('<VegetationZone>' + "\n")
      xmlData.write('<VegetationZoneParameters>' + "\n")

      for i in range(2, 4):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")

      xmlData.write('</VegetationZoneParameters>' + "\n")
      xmlData.write('</VegetationZone>' + "\n")

    rowNum +=1

xmlData.write('</Catchment>' + "\n")
xmlData.close()
'''