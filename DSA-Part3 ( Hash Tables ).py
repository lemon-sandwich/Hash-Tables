class HashTable:
    def __init__(self):
        self.size = 100
        self.arr = [None for i in range(self.size)] # To fill an array upto a range
    
    def HashFunction(self,key):
        h = 0
        for n in range(len(key)):
            h += ord(key[n])
        h %= 100
        return h
    
    def insert(self,data,key):
        self.arr[self.HashFunction(key)] = data
    
    def display(self):
        for n in range(len(self.arr)):
            print(self.arr[n])
    
    def display_specific(self,key):
        print(self.arr[self.HashFunction(key)])

    def delete(self,data,key):
        self.arr[self.HashFunction(key)] = "None"
    
h = HashTable()

while True:
    print("1. Insert\n")
    print("2. Delete\n")
    print("3. Display All\n")
    print("4. Display Specific\n")
    print("Press Any Other Button To Start The Next Variation")
    op = input("Choose: ")
    if op == '1':
        h.insert(input("Value: "),input("Key: "))
    elif op == '2':
        h.delete(input("Value: "),input("Key: "))
    elif op == '3':
        h.display()
    elif op == '4':
        h.display_specific(input("Key: "))
    else:
        break

# -------------------------------------------------------- #
# Using Built-In Functions
# In this variation, we converted arr in a dictionary and used setitem and getitem built-in functions to 
# implement hashtable

class HashTable2:
    def __init__(self):
        self.size = 100
        self.arr = [None for i in range(self.size)] # To fill an array upto a range
    
    def HashFunction(self,key):
        h = 0
        for n in key:
            h += ord(n)
        h %= 100
        return h
    
    def __setitem__(self,key,data):
        self.arr[self.HashFunction(key)] = data
    
    def __getitem__(self,key):
         h = self.arr[self.HashFunction(key)]
         return h

    def __delitem__(self,key):
        self.arr[self.HashFunction(key)] = "None"
    
h2 = HashTable2()
h2.arr = {}
while True:
    print("1. Insert\n")
    print("2. Delete\n")
    print("3. Display All\n")
    print("4. Display Specific\n")
    print("Press Any Other Button To Start The Hash Table Collision Program")
    op = input("Choose: ")
    if op == '1':
        h2.arr[input("Key: ")] = input("Value: ")
    elif op == '2':
        del h2.arr[input("Key: ")]
    elif op == '3':
        print(h2.arr)
    elif op == '4':
        print(h2.arr[input("Key: ")])
    else:
        break


# ----------------------------------------------------------- #
# Collision Handling

class HashTable3:
    def __init__(self):
        self.size = 100
        self.arr = [None for i in range(self.size)] # To fill an array upto a range
    
    def HashFunction(self,key):
        h = 0
        for n in key:
            h += ord(n)
        h = h^2 + h*2 + 1
        h %= 100
        return h
    
    def __setitem__(self,key,data):
        h = self.HashFunction(key)
        found = False
        # In each array index a map is stored, that's why when we iteratre the loop we check for the 0th index
        # because the keys are stored in the 0th index of map and the value in the 1st index.
        # index will keep on iterating through the maps in that index
        for index, element in enumerate(self.arr[h]):   # Enumerator function is also a loop function
            if element[0] == key:   
                self.arr[h][index] = (index,data)   # This will change the map values
                found = True
        if not found:
            self.arr[h].append(key,data)
    
    def __getitem__(self,key):
        found = False
        h = self.arr[self.HashFunction(key)]
        if self.arr[h][0] == key:
            found = True
        if not found:
            for index, element in enumerate(self.arr[h]):
                if element[0] == key:
                    found = True
                    return self.arr[h][index][1]
        if not found:
            return "Item Not Found!\n"
        return self.arr[h][0][1]

    def __delitem__(self,key):
        found = False
        h = self.HashFunction(key)
        if self.arr[h][0][0] == key:
            self.arr[h][0] = "None"
            found = True
            return
        for index,element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][index] = "None"
                found = True
        if not found:
            print("Item Not Found!\n")
    
h3 = HashTable3()
h3.arr = {}
while True:
    print("1. Insert\n") 
    print("2. Delete\n")
    print("3. Display All\n")
    print("4. Display Specific\n")
    print("Press Any Other Button To Start The Exercise")
    op = input("Choose: ")
    if op == '1':
        h3.arr[input("Key: ")] = input("Value: ")
    elif op == '2':
        del h3.arr[input("Key: ")]
    elif op == '3':
        print(h3.arr)
    elif op == '4':
        print(h3.arr[input("Key: ")])
    else:
        break

# ----------------------------------------------------------- #
# Exercise

class HashTable4:
    def __init__(self):
        self.size = 100
        self.arr = [None for i in range(self.size)] # To fill an array upto a range
    
    def HashFunction(self,key):
        h = 0
        for n in key:
            h += ord(n)
        h = h^2 + h*2 + 1
        h %= 100
        return h
    
    def __setitem__(self,key,data):
        h = self.HashFunction(key)
        found = False
        # In each array index a map is stored, that's why when we iteratre the loop we check for the 0th index
        # because the keys are stored in the 0th index of map and the value in the 1st index.
        # index will keep on iterating through the maps in that index
        for index, element in enumerate(self.arr[h]):   # Enumerator function is also a loop function
            if element[0] == key:   
                self.arr[h][index] = (index,data)   # This will change the map values
                found = True
        if not found:
            self.arr[h].append(key,data)
    
    def __getitem__(self,key):
        found = False
        h = self.arr[self.HashFunction(key)]
        if self.arr[h][0] == key:
            found = True
        if not found:
            for index, element in enumerate(self.arr[h]):
                if element[0] == key:
                    found = True
                    return self.arr[h][index][1]
        if not found:
            return "Item Not Found!\n"
        return self.arr[h][0][1]

    def __delitem__(self,key):
        found = False
        h = self.HashFunction(key)
        if self.arr[h][0][0] == key:
            self.arr[h][0] = "None"
            found = True
            return
        for index,element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][index] = "None"
                found = True
        if not found:
            print("Item Not Found!\n")
    
h4 = HashTable4()
h4.arr = {}
h4.arr["Jan 1"] = 27
h4.arr["Jan 2"] = 31
h4.arr["Jan 3"] = 23
h4.arr["Jan 4"] = 34
h4.arr["Jan 5"] = 37
h4.arr["Jan 6"] = 38
h4.arr["Jan 7"] = 29
h4.arr["Jan 8"] = 30
h4.arr["Jan 9"] = 35
h4.arr["Jan 10"] = 30

print("What was the average temperature in first week of Jan")
avg = 0
for index, element in enumerate(h4.arr):
    if element is not "Jan 8":
        if element is not "Jan 9":
            if element is not "Jan 10":
                avg += h4.arr[element]
avg /=7
print(avg)
max = 0
date = "None"
print("What was the maximum temperature in first 10 days of Jan")

for index, element in enumerate(h4.arr):
    if h4.arr[element] > max:
        max = h4.arr[element]
        date = element
print(f"{date} : {max}")

print("What was the temperature on Jan 9?")
print(h4.arr["Jan 9"])

print("What was the temperature on Jan 4?")
print(h4.arr["Jan 4"])

# ----------------------------------------------------------------- #
# File Handling

input("Press Any Other Button For The File Handling Exercise\n")

"""
h5 = HashTable4()
h5.arr = {}
f = open("poem.txt", "rt") # Opening file in read-text file mode ( Default Mode )
To Make Hashfunctions for every word
l = []
content = f.readlines()
for n in content:
    l.append(n.split(' '))  # will separate the content whenever a space comes
ll = []
for index,element in enumerate(l):
    for n in element:
        ll.append(n)
for n in ll:
    if n is not ' ' and "\n":
        h5.arr[n] = int(h5.HashFunction(n))
for n in h5.arr:
    print(n)
"""
wordcount = {}
f = open("poem.txt","rt")
for line in f:
    words = line.split(' ')
    for word in words:
        word = word.replace('\n','')
        word = word.replace(';','')
        word = word.replace(',','')
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

for n in wordcount:
    print(n , ':', wordcount[n])

# --------------------------------------------------------- #
# Liner Probing Function