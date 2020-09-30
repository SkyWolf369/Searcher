s = input("Enter the word to search in the file:")

fp = 'file.txt'
f = open(fp)  
flag = index = 0

for line in f:
    line.strip().split('\n')
    index+=1
    if s in line:
       flag = 1
       break

if flag == 0:
   print(f"Sorry couldn't find {s}")
else:
   print(f'Found {s} in line {index}')

f.close()
