users = ['Dave', 'John', 'Sara']
data = ['Dave', 42, True]
emptyList= []
print("Dave" in users)
print(users[0])
print(users[-1]) # last value
print(users[-2]) # second last value?
print(users.index('Sara'))
print(users[0:2]) # slicing stuff
print(users[1:])
print(users[-3:-1])
print(len(data))
users.append('Elsa')
print(users)
users+=['Jason']
print(users)
users.extend(['Rob','Jimmy'])
print(users)
users.insert(0,'Bob')
print(users)
users[2:2] = ['Eddie', 'Alex']
print(users)
users[1:3] = ['Robert', 'JPJ']
print(users)
users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

users.sort()
print(users)

users[1:2]='morgan' # adds to the list alphabetically but not as a whole string
users.sort(key=str.lower)
print(users)

nums=[4,42,78,1,5]
nums.reverse() # reverses list
print(nums)

nums.sort(reverse=True) # descending order
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1,"Nora",True])
print(mylist)
mytuple = tuple(('Dave',42,True))
anothertuple= (2,5,1,2)
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Kaleisha')
newtuple = tuple(newlist)
print(newtuple)
