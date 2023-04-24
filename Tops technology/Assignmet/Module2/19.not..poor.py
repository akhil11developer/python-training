"""
Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string

"""

str = "The song is not that poor"
str1 = str.find("not")
str2 = str.find("poor")

if str1 < str2:
    print(str[:str1]+"Good")