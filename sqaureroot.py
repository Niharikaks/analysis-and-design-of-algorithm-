n = int(input("Enter a positive integer: "))

guess =n/2
for i in range(10):
    guess=(guess+n/guess)/2
    print("sqaure root:",guess)
print("sqaure root:",guess)