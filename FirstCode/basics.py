def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Enter some input:"))

print(weather_condition((user_input)))

name_input = input("Enter your name: ")
message = "Hello %s!" % name_input
message = f"Hello {name_input}"
print(message)