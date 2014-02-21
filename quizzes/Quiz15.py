#!/usr/bin/env python3

"""
CS327e: Quiz #15 (5 pts) <Aizhuldyz>
"""

""" ----------------------------------------------------------------------
 1. What's the output of the following?
    (4 pts)

[{'sName': 'Fay',   'sID': 678},
 {'sName': 'Irene', 'sID': 876}]
[]
"""

def select (r, up) :
    return [t for t in r if up(t)]

def project (r, *a) :
    return [{v : t[v] for v in a if v in t} for t in r]

Student = [ \
    {"sID" : 123, "sName" : 'Amy',    "GPA" : 3.9, "sizeHS" : 1000},
    {"sID" : 345, "sName" : 'Craig',  "GPA" : 3.5, "sizeHS" :  500},
    {"sID" : 456, "sName" : 'Doris',  "GPA" : 3.9, "sizeHS" : 1000},
    {"sID" : 678, "sName" : 'Fay',    "GPA" : 3.8, "sizeHS" :  200},
    {"sID" : 789, "sName" : 'Gary',   "GPA" : 3.4, "sizeHS" :  800},
    {"sID" : 987, "sName" : 'Helen',  "GPA" : 3.7, "sizeHS" :  800},
    {"sID" : 876, "sName" : 'Irene',  "GPA" : 3.9, "sizeHS" :  400},
    {"sID" : 654, "sName" : 'Amy',    "GPA" : 3.9, "sizeHS" : 1000},
    {"sID" : 543, "sName" : 'Craig',  "GPA" : 3.4, "sizeHS" : 2000}]

print(
    project(
        select(
            Student,
            lambda v :
                ("GPA"       in v)      and
                (v["GPA"]    >  3.7)    and
                ("sizeHS"    in v)      and
                (v["sizeHS"] <  1000)),
        "sID",
        "sName"))

print(
    select(
        project(
            Student,
            "sID",
            "sName"),
        lambda v :
            ("GPA"       in v)      and
            (v["GPA"]    >  3.7)    and
            ("sizeHS"    in v)      and
            (v["sizeHS"] <  1000)))
