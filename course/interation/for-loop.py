# ITERATION

# For Loop
# Structure that helps achieve interation
# • Specify a range of numbers using range()
#   • Range() => (start, stop, step)
#       • Start (optional): default 0
#       • Stop  (required) 
#       • Step  (optional): derfault 1

print ("num from 0 - 3")
# i is the loop variable
for i in range(4):
    print(i)

print ("----------------------")

# 1 start at 1
# 8 end at 7
# 2 step of 2
for i in range(1,8,2):
    print(i)

print ("----------------------")

vowels = ['a','e','i','o','u']

for v in vowels:
    print (v)