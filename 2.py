def last_char(str1,str2):
    lc=str2[-1]
    count=0
    for i in range(0,len(str1)):
        if(str1[i]==lc):
            count+=1
        else:
            i+=1
    return count

str1=input()
str2=input()
