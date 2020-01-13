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

def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(sum1, sum2)
print(type(x), type(y), type(z))

monday_temperatures = [9.1, 8.4, 7.5]
monday_temperatures.append(8.1)
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

mysum = sum(student_grades.values())
mycount = len(student_grades)
mymean = mysum / mycount
print(mean(monday_temperatures))

myword = "hello"
print(myword.title())