import xml.etree.ElementTree as ET
import csv

tree = ET.parse("data_test.xml")
root = tree.getroot()
#for m in root:
 #   print(root, m)
#
# open a file for writing

labeled_file = open('labeledfile_test.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(labeled_file)
f=  open("data.txt",'r')
#f=  open("sample124196.xml",'r')
txt1 = f.read()
f.close()

r = []
temp=[]
count = 0
print(root)
for roots in root.findall('AnnotationSet'):
    #print('roots',roots.tag,roots.keys(), count)
    ##print('roots',roots.tag,roots.keys(),roots.attrib)
    for child in roots.findall('Annotation'):
        #print('child',child.tag, count)
        ##print('child',child.tag,child.keys(),child.text,child.attrib)
       
        for gchild in child.findall('Feature'):
            #print('grandchild',gchild.tag, count)
            ##print('grandchild',gchild.tag,gchild.keys(),gchild.attrib)
            
            for ggchild in gchild.findall('Value'):
                len(gchild)
                #print('greatgrandchild',ggchild.tag, count)
                ##print('grandgrandchild',ggchild.tag,ggchild.keys(),ggchild.text)
   
            if count == 0:
                #r.append(child.tag)
                for i in child.keys():
                    temp.append(i)
                r = [temp[0],temp[2],temp[3],"Labeled word in the text",temp[1],ggchild.tag]
                #print(child.keys())
                csvwriter.writerow(r)
                count = count + 1
                r = []
                temp = []
            else:
                #r.append(child.text)
                for i in child.attrib.values():
                    temp.append(i)
                r = [temp[0],int(temp[2]),int(temp[3]),txt1[int(temp[2]):int(temp[3])],temp[1],ggchild.text]
                #print(temp[2],type(temp[2]))
                #print(child.attrib.values())
                #print(temp)
                print(int(temp[2]),int(temp[3]))
                csvwriter.writerow(r)
                count = count + 1
                r =[]
                temp =[]
    

'''
for m in root:
   print(root, m)
for roots in root.findall('AnnotationSet'):
    print('roots',roots.tag,roots.keys(), count)
    '''

  