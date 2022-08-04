import math
#Mean
a=[1,2,1,4,5,6,7,8,9]
c=0
for i in a:
    c+=i
print("Mean of the given array (", a, ") is {0}".format(c/len(a)))
#Median
no = len(a)
a.sort()
if no % 2 == 0:
    median1 = a[no//2]
    median2 = a[no//2 - 1]
    median = (median1 + median2)/2
else:
    median = a[no//2]
print("The median of the given numbers  (", a, ") is", str(median))
#Mode
def countX(a, x):
	count = 0
	for ele in a:
		if (ele == x):
			count = count + 1
	return count
    
def most_frequent(a):
	counter = 0
	num = a[0]
	for i in a:
		curr_frequency = a.count(i)
		if(curr_frequency> counter):
			counter = curr_frequency
			num = i
	return num
print("Mode is {0}".format(most_frequent(a)))
#Standard Deviation
mean = c / len(a)   # mean
var  = sum(pow(x-mean,2) for x in a) / len(a)
std  = math.sqrt(var)
print("Standard Deviation is {0}".format(std))
#Variance
length= int(len(a))
ans = sum((i - mean) ** 2 for i in a) / length
  
print("The variance of list is : " + str(ans)) 
