#!/usr/bin/env python
# coding: utf-8

# In[11]:


print("Dev_Ashu:- The best web dev you've ever met😊")


# In[2]:


print("don't try console.log on this😂")


# In[10]:


print("So, don't you know how to find mean, median & mode?? Lem'me help then...😊👍")

#Mean
a=[1,2,1,4,5,6,7,8,9]
print("Given Array is (" , a, ")")
c=0
for i in a:
    c+=i
print("Mean of the given array (", a, ") is 👉 {0}".format(c/len(a)))

#Median
no = len(a)
a.sort()
if no % 2 == 0:
    median1 = a[no//2]
    median2 = a[no//2 - 1]
    median = (median1 + median2)/2
else:
    median = a[no//2]
print("The median of the given numbers  (", a, ") is 👉", str(median))

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
print("Mode is 👉 {0}".format(most_frequent(a)))


# In[ ]:




