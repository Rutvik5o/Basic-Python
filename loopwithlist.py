marks = [1,2,"hello"]

print(marks)

print(marks[2])

print(marks[-1])

print(marks[-2])

print(marks[-3])


#for particular index

print("hello")

print(marks[0:3])    # 3 will not included

print("new")

for score in marks:
     print(score)


marks.append(89)  # for add new

print(marks)

marks.insert(0,97)

print(marks)   #0 is index number

print(99 in marks)  # for check that type in marks exist or not

print(len(marks)) # for checking length


i=0
while i< len(marks):  # using while loop
     print(marks[i])
     i= i+1


marks.clear()# using can clear

print(marks)