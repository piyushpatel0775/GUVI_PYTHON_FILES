numbers = [1,2,3,4,5]
target = 4

if target in numbers :
    print(f"target is in list")
else:
    print(f"target not in list")


# first question  completed



num= int(input("enter number:"))
factorial= 1
for i in range(1,num+1):
    factorial*=i 
print("factorial of",num, "is", factorial)

# second question  completed



s = "malayalam"
if s == s[::-1]:
    print("pallindrome")
else:
    print("not pallindrome")


# third question  completed 



word = "banana"
count = 0

for char in word:
    if char == 'a':
          count += 1
print("the number of occurences of 'a' is:" , count)   


# fourth question  completed



numbers = [2,3,5,6,8]
sum_squares = 0

for num in numbers:
    if num%2 == 0:
        sum_squares += num**2
print("sum of squares of even numbers is:", sum_squares)        


# fifth question  completed
