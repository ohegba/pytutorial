
choice_int = int(input('Enter an integer, win a nonexistent prize!: '))

if choice_int < 0:
    print("Negative")
elif choice_int == 0:
    print("Zero")
elif choice_int > 0:
    print("Positive")
else:
    print("???")

wordlist = ['Apple', 'Banana', 'Cherry', 'Durian']

for word in wordlist:
    print(word.upper())

str_built = ''
for i in range(2,10,2):
    str_built += str(i) + "..."
print(str_built + "WHO DO WE APPRECIATE?")
