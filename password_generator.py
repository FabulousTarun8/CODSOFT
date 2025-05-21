#modules_and_data
import random
password = ""

#length_input
while True:
    length = int(input("Enter the length of the password: "))
    if type(length) != type(10) or length <= 0:
        print("Please enter a valid length!")
    else:
        break

#characters
characters = []
for ordinate in range(65, 65+26):
    characters.append(chr(ordinate))
    characters.append(chr(ordinate).lower())
for number in range(0, 10):
    characters.append(str(number))
for symbol in ["!", "@", "#", "$", "%", "^", "&", "*", "+", "?"]:
    characters.append(symbol)

#making_password
possible = len(characters)-1
while length:
    password += characters[random.randint(0, possible)]
    length -= 1

#display
print(password)
