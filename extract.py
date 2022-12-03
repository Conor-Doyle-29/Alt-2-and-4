file=open("tmp.csv","r")
dataIn=file.read()
file.close
print(dataIn)

tmpList= dataIn.split(",")
tmpList.remove(tmpList[-1])
print(tmpList)

list1=tmpList[0::3]
print(list1)

list2=tmpList[1::3]
print(list2)

list3=tmpList[2::3]
print(list3)