def Bit(n):
    x= 0
    for i in range(n):
        inp= input()
        if inp == "++X" or inp == "X++":
            x+=1
        else:
            x-=1
    return x




n= int(input())
print(Bit(n))