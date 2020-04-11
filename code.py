# --------------
#Code starts here
def palindrome(num):
    if len(str(num))==1:
        return num+1
    while(str(num)!=str(num)[::-1]):
        num+=1
    return num



# --------------
#Code starts here
from collections import Counter
 
def a_scramble(str_1, str_2):
 
    c=Counter(str_1.lower())
    c2=Counter(str_2.lower())
 
    for key,value in c2.items():
        if c2[key] > c[key]:
        
            return False 
    return True



# --------------
#Code starts here
import math
def check_fib(num):
    x1=5*num*num+4
    x2=5*num*num-4
    if x1==int(math.sqrt(x1))*int(math.sqrt(x1)) or x2==int(math.sqrt(x2))*int(math.sqrt(x2)):
        return True
    else:
        return False



# --------------
#Code starts here
def compress(word):
    word=word.lower()
    k=word[0]
    
    num=0
    str1=""
 
    for i in word:
        if k==i:
            num+=1
            
            k=i
        else:
            str1+=k+str(num)
            num=1
            k=i
            
    return str1+i+str(num)



# --------------
#Code starts here
def k_distinct(string,k):
    
    if (len(set(string.lower())))==k:
        return True
    else:
        return False



