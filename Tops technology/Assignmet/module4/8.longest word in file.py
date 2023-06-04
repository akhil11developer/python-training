f= open("akhil.txt","r")

wordslist = f.read().split()

longestword = len(max(wordslist,key = len))

longestword = len(max(wordslist, key=len))

result = [textword for textword in wordslist if len(textword) == longestword]

# Print the longest words from a text file
print(result)