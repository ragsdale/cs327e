#!/usr/bin/env python

# ----------
# Project.py
# ----------

print("Project.py")

def project (r, *a) :
    return [{v : t[v] for v in a if v in t} for t in r]

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

x = project(Apply, "sID", "decision")
print(len(x))
print(x)
print()
"""
12
[{'decision': True, 'sID': 123},
 {'decision': False, 'sID': 123},
 {'decision': False, 'sID': 234},
 {'decision': True, 'sID': 345},
 {'decision': False, 'sID': 345},
 {'decision': True, 'sID': 678},
 {'decision': True, 'sID': 987},
 {'decision': False, 'sID': 876},
 {'decision': True, 'sID': 876},
 {'decision': True, 'sID': 765},
 {'decision': False, 'sID': 765},
 {'decision': False, 'sID': 543}]
"""

x = project(Apply, "major", "decision")
print(len(x))
print(x)
print()
"""
12
[{'major': 'CS', 'decision': True},
 {'major': 'EE', 'decision': False},
 {'major': 'EE', 'decision': True},
 {'major': 'biology', 'decision': False},
 {'major': 'bioengineering', 'decision': True},
 {'major': 'bioengineering', 'decision': False},
 {'major': 'history', 'decision': True},
 {'major': 'CS', 'decision': False},
 {'major': 'biology', 'decision': True},
 {'major': 'marine biology', 'decision': False},
 {'major': 'history', 'decision': False},
 {'major': 'psychology', 'decision': True}]
"""

print("Done.")
