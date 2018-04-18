import csv
# open and read CSV file of labels
file = open('labeledfile_test.csv')
gate_csv = csv.reader(file)
list_gate_csv = list(gate_csv)

# Open and read the transcribed file 
txt_file = open('data.txt')
text_file = txt_file.read()

# A file to write the labeled data in
gtext_file = open('labeled_text2.txt','w')



list_of_labeled = []
for i in range(1,len(list_gate_csv)):
    list_of_labeled.append(list_gate_csv[i][1])
    list_of_labeled.append(list_gate_csv[i][2])
    

i=0
j=1



while i != len(list_of_labeled):
    if i ==0 and list_of_labeled[i] !=0:
        gtext_file.write(text_file[0:int(list_of_labeled[i])])
    print(text_file[int(list_of_labeled[i]):int(list_of_labeled[i+1])])
    #print('********')
    #gtext_file.write("""{\\rtf1 This is \\b TEXT FILE  \\b0\line\}""")
    gtext_file.write('*$*$*$*')
    gtext_file.write(text_file[int(list_of_labeled[i]):int(list_of_labeled[i+1])])
    gtext_file.write('(')
    gtext_file.write(list_gate_csv[j][4])
    gtext_file.write(', ')
    gtext_file.write(list_gate_csv[j][5])
    gtext_file.write(')')
    gtext_file.write('*$*$*$*  ')
    #i = i+1
    if i+2 != len(list_of_labeled):
       # print(text_file[int(list_of_labeled[i+1])+1:int(list_of_labeled[i+2])-1])
        #print('######')
        #gtext_file.write('MYTEXT')
        #gtext_file.write(text_file[int(list_of_labeled[i+1])+1:int(list_of_labeled[i+2])-1])
        gtext_file.write(text_file[int(list_of_labeled[i+1]):int(list_of_labeled[i+2])])
    i = i+2
    j= j+1

#for i in range(len(list_of_labeled)):
 #   print(list_of_labeled[i])
  #  if i == len(list_of_labeled)-1:
   #     print('break')
    #    break
    #else:
     #   print(i,i+1)
      #  print(int(list_of_labeled[i]),list_of_labeled[i+1])
       # a = int(list_of_labeled[i])
        #b = int(list_of_labeled[i+1])
        #print(text_file[a:b])
    #print(text_file[23:38])
    #print(text_file[int(i):(int(i)+1)])


#for j in text_file:
    #print(j)
    #gtext_file.write(j)
    #gtext_file.write(i[2])
#print(list_of_labeled)

file.close()
txt_file.close()