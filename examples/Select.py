#!/usr/bin/env python3

# ---------
# Select.py
# ---------

print("Select.py")

def select (r, up) :
    return [t for t in r if up(t)]

Student = [ \
    {"sID" : 123, "sName" : 'Amy',    "GPA" : 3.9, "sizeHS" : 1000},
    {"sID" : 234, "sName" : 'Bob',    "GPA" : 3.6, "sizeHS" : 1500},
    {"sID" : 345, "sName" : 'Craig',  "GPA" : 3.5, "sizeHS" :  500},
    {"sID" : 456, "sName" : 'Doris',  "GPA" : 3.9, "sizeHS" : 1000},
    {"sID" : 567, "sName" : 'Edward', "GPA" : 2.9, "sizeHS" : 2000},
    {"sID" : 678, "sName" : 'Fay',    "GPA" : 3.8, "sizeHS" :  200},
    {"sID" : 789, "sName" : 'Gary',   "GPA" : 3.4, "sizeHS" :  800},
    {"sID" : 987, "sName" : 'Helen',  "GPA" : 3.7, "sizeHS" :  800},
    {"sID" : 876, "sName" : 'Irene',  "GPA" : 3.9, "sizeHS" :  400},
    {"sID" : 765, "sName" : 'Jay',    "GPA" : 2.9, "sizeHS" : 1500},
    {"sID" : 654, "sName" : 'Amy',    "GPA" : 3.9, "sizeHS" : 1000},
    {"sID" : 543, "sName" : 'Craig',  "GPA" : 3.4, "sizeHS" : 2000},
    {"sID" : 432, "sName" : 'Kevin',  "GPA" : 3.2, "sizeHS" : 1500},
    {"sID" : 321, "sName" : 'Lori',   "GPA" : 3.2, "sizeHS" : 2500}]
assert(len(Student) == 14)

Apply = [ \
    {"sID" : 123, "cName" : 'Stanford', "major" : 'CS',             "decision" : True},
    {"sID" : 123, "cName" : 'Stanford', "major" : 'EE',             "decision" : False},
    {"sID" : 123, "cName" : 'Berkeley', "major" : 'CS',             "decision" : True},
    {"sID" : 123, "cName" : 'Cornell',  "major" : 'EE',             "decision" : True},
    {"sID" : 234, "cName" : 'Berkeley', "major" : 'biology',        "decision" : False},
    {"sID" : 345, "cName" : 'MIT',      "major" : 'bioengineering', "decision" : True},
    {"sID" : 345, "cName" : 'Cornell',  "major" : 'bioengineering', "decision" : False},
    {"sID" : 345, "cName" : 'Cornell',  "major" : 'CS',             "decision" : True},
    {"sID" : 345, "cName" : 'Cornell',  "major" : 'EE',             "decision" : False},
    {"sID" : 678, "cName" : 'Stanford', "major" : 'history',        "decision" : True},
    {"sID" : 987, "cName" : 'Stanford', "major" : 'CS',             "decision" : True},
    {"sID" : 987, "cName" : 'Berkeley', "major" : 'CS',             "decision" : True},
    {"sID" : 876, "cName" : 'Stanford', "major" : 'CS',             "decision" : False},
    {"sID" : 876, "cName" : 'MIT',      "major" : 'biology',        "decision" : True},
    {"sID" : 876, "cName" : 'MIT',      "major" : 'marine biology', "decision" : False},
    {"sID" : 765, "cName" : 'Stanford', "major" : 'history',        "decision" : True},
    {"sID" : 765, "cName" : 'Cornell',  "major" : 'history',        "decision" : False},
    {"sID" : 765, "cName" : 'Cornell',  "major" : 'psychology',     "decision" : True},
    {"sID" : 543, "cName" : 'MIT',      "major" : 'CS',             "decision" : False}]
assert(len(Apply) == 19)

College = [ \
    {"cName" : 'Stanford', "state" : 'CA', "enrollment" : 15000},
    {"cName" : 'Berkeley', "state" : 'CA', "enrollment" : 36000},
    {"cName" : 'MIT',      "state" : 'MA', "enrollment" : 10000},
    {"cName" : 'Cornell',  "state" : 'NY', "enrollment" : 21000},
    {"cName" : 'Irene',    "state" : 'TX', "enrollment" : 25000}]
assert(len(College) == 5)

x = select(Student, lambda v : v["GPA"] > 3.7)
print(len(x))
print(x)
print()
"""
5
[{'sName': 'Amy',   'GPA': 3.9, 'sizeHS': 1000, 'sID': 123},
 {'sName': 'Doris', 'GPA': 3.9, 'sizeHS': 1000, 'sID': 456},
 {'sName': 'Fay',   'GPA': 3.8, 'sizeHS': 200,  'sID': 678},
 {'sName': 'Irene', 'GPA': 3.9, 'sizeHS': 400,  'sID': 876},
 {'sName': 'Amy',   'GPA': 3.9, 'sizeHS': 1000, 'sID': 654}]
"""

x = select(Student, lambda v : (v["GPA"] > 3.7) and (v["sizeHS"] < 1000))
print(len(x))
print(x)
print()
"""
2
[{'sName': 'Fay',   'GPA': 3.8, 'sizeHS': 200, 'sID': 678},
 {'sName': 'Irene', 'GPA': 3.9, 'sizeHS': 400, 'sID': 876}]
"""

x = select(Apply, lambda v : (v["cName"] == "Stanford") and (v["major"] == "CS"))
print(len(x))
print(x)
print()
"""
3
[{'major': 'CS', 'cName': 'Stanford', 'decision': True,  'sID': 123},
 {'major': 'CS', 'cName': 'Stanford', 'decision': True,  'sID': 987},
 {'major': 'CS', 'cName': 'Stanford', 'decision': False, 'sID': 876}]
"""

print("Done.")
