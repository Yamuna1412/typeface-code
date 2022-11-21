def convert_to_base3(n):
    s=""
    while(n>0):
        x=n%3
        n=n//3
        s+=str(x)
    return s[::-1]

print(convert_to_base3(10))

