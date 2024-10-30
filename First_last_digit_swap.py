num=int(input())
def swap_first_last(num):
    temp=num
    b=temp%10
    count=0
    while temp>0:
        a=temp%10
        temp//=10
        count+=1
    y=num-(a*(10**(count-1)))
    y=int(y)
    y-=b
    x=(b*(10**(count-1)))+y+a
    return x
print(swap_first_last(num))
