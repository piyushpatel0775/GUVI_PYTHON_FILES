lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in lst:
    if i%3==0:
        print("fizz")
    elif i%5 == 0:
        print("buzz")
    elif i%3==0 and i %5 ==0:
        print("fizz buzz")
    else:
        print(i)
  
 
