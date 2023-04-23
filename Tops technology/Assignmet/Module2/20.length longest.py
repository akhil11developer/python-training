str = ["my", "name" ,"is", "akhil", "delvadiya"]
max = len(str)
for i in str:
    if (len(i)>max):
        max = len(i)
        max_word = i
print(max)