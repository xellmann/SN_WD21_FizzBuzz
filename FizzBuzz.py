print("Herzlich willkommen zu unserem FizzBuzz!")
zahl1 = int(input("Bitte geben Sie eine Zahl zwischen 1 und 100 ein: "))
print("Die ausgewählte Zahl lautet: " + str(zahl1))

for i in range(1, zahl1+1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
