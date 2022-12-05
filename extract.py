import statistics as stat
import matplotlib.pyplot as plt 

file=open("tmp.csv","r")
dataIn=file.read()
file.close
print(dataIn)

tmpList= dataIn.split(",")
tmpList.remove(tmpList[-1])
print(tmpList)

list1=tmpList[0::3]
print(list1)
list1=[int(item) for item in list1]

list2=tmpList[1::3]
print(list2)
list2=[int(item) for item in list2]

list3=tmpList[2::3]
print(list3)
list3=[int(item) for item in list3]

mean1= stat.mean(list1)
print(mean1)
mean2= stat.mean(list2)
print(mean2)
mean3= stat.mean(list3)
print(mean3)
median1 = stat.median(list1)
print(median1)
median2 = stat.median(list2)
print(median2)
median3 = stat.median(list3)
print(median3)

mode1=stat.mode(list1)
print(mode1)
mode2=stat.mode(list2)
print(mode2)
mode3=stat.mode(list3)
print(mode3)

plt.plot(list1)
plt.show()
