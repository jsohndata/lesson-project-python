# Compound Condition
# A conditional statement controls the flow of a program by testing whether a specific condition is met.

raining = input ("raining? (y/n)")
umbrella = input ("umbrealla? (y/n)")

if raining == "y" and umbrella == "y":
    print ("good!")
elif raining == "y" and umbrella == "n":
    print("okay...")



x = input("Enter a numuber:")

# float() instead of int()
# Because int() can convert float to int, whereas float() doesn't convert the numerical value.

# xx = 1
# print (f"xx => {float(xx)}") => 1

# yy = 1.5
# print (f"yy => {int(yy)}") => 1
x = float(x)

if x < 2:
    print("the number less than 2")
elif x < 6:
    print("the number is less than 6")
elif x < 8:
    print("the number is less than 8")
elif x < 10:
    print("the number is less than 10")

# absolute nuymber
def abs_value (num):
    if num < 0:
        # return -1 * num
        return -num 
    elif num == 0:
        return 0
    else:
        return num

result = abs_value(-4)
print (result)

result = abs_value(78.13213123123)
print (result)


