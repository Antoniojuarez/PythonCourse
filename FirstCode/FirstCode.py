import datetime
mynow = datetime.datetime.now()
print(mynow)

mynumber = 10
mytext = "Hello"

print(mynumber, mytext)

x = 10
y = "10"
z = 10.1

sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))

student_grades = [9.1, 8.4, 7.5]

mysum = sum(student_grades)
mycount = len(student_grades)
mean = mysum / mycount
print(mean)

myword = "hello"
print(myword.title())