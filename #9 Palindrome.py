Input = input("Enter text or number to find whether it's a palindrome\n")
i_l = []
r_l = []
Reverse = ""

l = len(Input)

for word in Input:
    i_l.append(word)

n = -1
for number in range(l):
    r_l.append(i_l[n])
    n -= 1

for char in r_l:
    Reverse += char

if Input == Reverse:
    print("Yes. It's a Palindrome")
else:
    print("No. It's not a Palindrome")