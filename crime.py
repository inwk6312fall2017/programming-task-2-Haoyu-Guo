with open(crime.csv,'r') as myfile

mylist=['Crime type','Crime ID','Crime Count' \t]
count=0
summ=0
calc=0
addd=0

mylist.append('Assault')
mylist.append('1430')
for i in myfile:
    if i == 'Assault':
       count+=1
    mylist.apppend(count)
mylist.append('Robbery')
mylist.append('2142')
for i in myfile:
    if i == 'Robbery':
       calc +=1
    mylist.append(calc)
mylist.append('Theft of')
mylist.append('2135')
for i in myfile:
    if i == 'Theft':
       summ+=1
    mylist.append(summ)
mylist.append('Break')
mylist.append('2120')
for i in myfile:
    if i =='Break'      
        addd+=1
    mylist.append(addd)

def __srt__(mylist):
    print '%s | %s | %s \t' % (mylist[0],mylist[1],mylist[2])
