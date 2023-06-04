"""Write a Python program to count the frequency of words in a file"""

# Open the file in read mode
text = open("akhil.txt", "r")

# Create an empty dictionary
d = dict()

for line in text:
	# Remove the leading spaces and newline character
	line = line.strip()

	# lowercase to avoid case mismatch
	line = line.lower()

	# Split the line into words
	words = line.split(" ")
						

	# Iterate over each word in line
	for word in words:
		if word in d:
			d[word] = d[word] + 1
		else:
			d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
	print(key, ":", d[key])
