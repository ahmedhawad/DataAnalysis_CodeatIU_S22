


from numpy import intp


Student = [

  {"sid": 1000 , "sname": "Margaret", "hwometown": "Carmel"},
  {"sid": 1002 , "sname": "James", "hometown": "NYC"},
  {"sid": 1003 , "sname": "Zack", "hometown": "LA"},
  {"sid": 1004 , "sname": "Candice", "hometown": "Chicago"},
  {"sid": 1005 , "sname": "Bob", "hometown": "Loisiville"},
  {"sid": 1006 , "sname": "Jackson", "hometown": "Talahassee"},
  {"sid": 1007 , "sname": "George", "hometown": "Miami"},
  {"sid": 1008 , "sname": "David", "hometown": "Albany"},
  {"sid": 1009 , "sname": "Nickolas", "hometown": "St.Charles"},
  {"sid": 1010 , "sname": "Christian", "hometown": "Denver"},
  {"sid": 1011 , "sname": "Margaret", "hometown": "SanFrancisco"},
  {"sid": 1012 , "sname": "Ashley", "hometown": "Delhi"},
  {"sid": 10013 , "sname": "Mohammed", "hometown": "Paris"},
  {"sid": 10014, "sname": "Edward", "hometown": "Elizabeth"},
  {"sid": 10015, "sname": "Benjamin", "hometown": "Ft.Wayne"},
  {"sid": 10016 , "sname": "Samantha", "hometown": "Indianapolis"},
  {"sid": 10017 , "sname": "Jody", "hometown": "London"},
  {"sid": 10018, "sname": "Eduardo", "hometown": "Cairo"},
    
]



Company = [

  {"company": "Apple", "cid" :100},
  {"company": "Google", "cid" :101},
  {"company": "Aldis", "cid" :102},
  {"company": "Amazon", "cid" :103},
  {"company": "Chase", "cid" :104},
  {"company": "Microsoft", "cid" :105},
  {"company": "Twitter", "cid" :106},
  {"company": "Mom&Pop", "cid" :107},
  {"company": "LocalCompany", "cid" :108},
  {"company": "Aldis", "cid" :109}

]


Internship = [

  {"sid": 1000 , "cid": 100, "hourlySalary": 12},
  {"sid": 1002 , "cid": 102, "hourlySalary": 10},
  {"sid": 1003 , "cid": 100, "hourlySalary": 15},
  {"sid": 1004 , "cid": 103, "hourlySalary": 23},
  {"sid": 1005 , "cid": 106, "hourlySalary": 22},
  {"sid": 1006 ,"cid": 107, "hourlySalary": 13},
  {"sid": 1007 , "cid": 109, "hourlySalary": 14},
  {"sid": 1008 , "cid": 100, "hourlySalary": 18},
  {"sid": 1010 ,"cid": 107, "hourlySalary": 20},
  {"sid": 1011 , "cid": 105, "hourlySalary": 18},
  {"sid": 1012 , "cid": 105, "hourlySalary": 12},
  {"sid": 10015, "cid": 105, "hourlySalary": 16},
  {"sid": 10016 , "cid": 106, "hourlySalary": 14},
  {"sid": 10017 , "cid": 101, "hourlySalary": 13},
  {"sid": 10018, "cid": 101, "hourlySalary": 14}



]



"""

Queries in SQL are a lot like list comprehensions in Python

"""





######### Using List comprehensions #########



#Making a list of elements of range(5) through a regular for loop and then though a list comprehension


#1. for loop:
print(1)

templist = []

for x in range(5):
  templist.append(x)

print(templist)

otherlist = []
#double loop
for a in range(3):
  for b in ["x","y","z"]:
    otherlist.append((a,b))

print(otherlist)



#2. list comp:
print(2)



print([x for x in range(5)])

print( [ (a,b) for a in range(3) for b in ["x","y","z"] 

])


######### Queries #########



#3. Tell me everyone in Student
print(3)



print([x for x in Student])




#4. Tell me the Person's name whp's sid is 1010
print(4)

print([s["sname"] for s in Student if s["sid"] == 1010])




# 5. Tell me the person's name who's salary is >= 18
print(5)


print([ s["sname"] for i in Internship for s in Student if s["sid"] == i["sid"] and i["hourlySalary"] >= 18



])


#########
