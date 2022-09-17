import random         # module
print("Welcome To Your Generator \n")

# we write alphabet small and capital and numbers and some symbols to creat very complex password
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+=-)(*&^%$#@!:;{}[]"

number = int(input("Number of passwords that you want: "))  # number of passwords
length = int(input("How character you need: "))  # length one of them

print("\nYour Passwords\n")

for x in range (number):    # you can name "x" anything you want
    password=""
    for y in range (length):
        password+= random.choice(char)
    print(password)

# you can use "while loop" to do this over and over again


