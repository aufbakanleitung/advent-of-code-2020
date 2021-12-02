# maak een applicatie die telt maar bij meervouden van 3 Fizz zegt en meervouden van 5 Buzz
# En dus bijv bij 15 FizzBuzz
# 7 = "Bitch"
# 11 = "Tits"

for i in range(1, 100):
    output = ""
    if i % 3 == 0: output += "Fizz"
    if i % 5 == 0: output += "Buzz"
    if i % 7 == 0: output += "Bitch"
    if i % 11 == 0: output += "Tits"
    if output == "": output = i

    print(output)
