""" Write a Python function that checks whether a passed string is
palindrome or not"""

def palindrome(string): #beginning to last and last to first is same string is called palindrome
    if (string == string[::-1]):
        return "the string is a palindrome"
    else:
        return "the string is not a palindrome"
string = input("Enter string : ")

print(palindrome(string))