# Q1 What is the output of this?
print(5 * 10 == 50)
True
# Q2 What is the output of this?
print("5" * 10 == 50)
[Type Error; Can only concatenate Str to Str and Int to Int, not Str to Int]
ANS: False
# Q3 What is the output of this?
if 5 == 5:
    print("A")
elif 1 != 0:
    print("B")
else:
    print("C")
<!-- ANSWER IS A :alarm: -->

# Q4 What is the output of this?
num = 5
print("The num is " + num)
Type Error
# Q5 What is the output of this?
num = 5
if num = 5:
    print("Hello")
else:
    print("Bye)
Output: Hello

# Q6 What is the result?
students = ["Geng Woon", "Darissa", "Walden", "Guhaan"]
students.append("Tyler")
students.insert(0, "Xinxi")
students.append("Ebenezer")
students.pop()
del(students[0])
students.pop(len(students) - 1)
print(students)
Xinxi
Geng Woon
Darissa
Walden
Guhaan
Tyler
Ebenezer

# Q7 Using a while loop, print out all the multiples of 3 and 5 that are less than or equal to 20
Expected output:
3 is a multiple of 3
5 is a multiple of 5
6 is a multiple of 3
9 is a multiple of 3
10 is a multiple of 5
12 is a multiple of 3
15 is a multiple of 3 and 5
18 is a multiple of 3
20 is a multiple of 5

# Q7 Convert the following for loop into a while loop
for i in range(100, -1, -10):
    print(i)




