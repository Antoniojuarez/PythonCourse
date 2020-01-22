import time
import os
import pandas


real = 0

while real:
    if os.path.exists("vegetables.txt"):
        with open("vegetables.txt") as file:
            print(file.read())
    else:
        print("File don't exist.")
    time.sleep(10)

while True:
    if os.path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File dont exist.")
    time.sleep(10)