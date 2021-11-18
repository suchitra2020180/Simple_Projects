## Average height without using mean function

height= input("Enter height of different persons seperate by space: ")
ht_list=height.split(' ')
print(ht_list)
sum=0
count=0
for i in ht_list:
    sum=sum + int(i)
    count += 1
    #Average=round(sum/len(ht_list))
Average=round(sum/count)
#print("Total height:",sum)
#print("Number of students:",count)
print(f"Average of given heights is: {Average}")


## Finding max value
max=0
for i in ht_list:
    if int(i) > max:
        max = int(i)
print("Maximum height in list : ", max)


