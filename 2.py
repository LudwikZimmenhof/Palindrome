import sys

def palindrome(s):
    x = s.lower().replace(" ", "")
    if x == ''.join(reversed(x)):
        print(f"This is a palindrome\nInput = {x}\nReversed = {x}\n")
    else:
        print(f"This is not a palindrome\nInput = {x}\nReversed = {''.join(reversed(x))}\n")

def main():
    for i in range(1, len(sys.argv)):
        palindrome(sys.argv[i])

main()
