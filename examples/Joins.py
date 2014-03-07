#!/usr/bin/env python3

# --------
# Joins.py
# --------

def select (r, up) :
    return [t for t in r if up(t)]

def project (r, *a) :
    return [{v : t[v] for v in a if v in t} for t in r]

def cross_join (r, s) :
    return [dict(list(v.items()) + list(w.items())) for v in r for w in s]

def theta_join (r, s, bp) :
    return [dict(list(v.items()) + list(w.items())) for v in r for w in s if bp(v, w)]

print("Joins.py")

R = [ \
    {"A" : 1, "B" : 6},
    {"A" : 2, "B" : 7},
    {"A" : 3, "B" : 8}]
assert(len(R) == 3)

S = [ \
    {"A" : 4, "C" : 6},
    {"A" : 1, "C" : 7},
    {"A" : 2, "C" : 8},
    {"A" : 2, "C" : 9}]
assert(len(S) == 4)

x = cross_join(R, S)
assert(len(x) == 12)
assert(
    x
    ==
    [{'A': 4, 'B': 6, 'C': 6},
     {'A': 1, 'B': 6, 'C': 7},
     {'A': 2, 'B': 6, 'C': 8},
     {'A': 2, 'B': 6, 'C': 9},
     {'A': 4, 'B': 7, 'C': 6},
     {'A': 1, 'B': 7, 'C': 7},
     {'A': 2, 'B': 7, 'C': 8},
     {'A': 2, 'B': 7, 'C': 9},
     {'A': 4, 'B': 8, 'C': 6},
     {'A': 1, 'B': 8, 'C': 7},
     {'A': 2, 'B': 8, 'C': 8},
     {'A': 2, 'B': 8, 'C': 9}])

x = theta_join(R, S, lambda v, w : v["A"] == w["A"])
assert(len(x) == 3)
assert(
    x
    ==
    [{'A': 1, 'B': 6, 'C': 7},
     {'A': 2, 'B': 7, 'C': 8},
     {'A': 2, 'B': 7, 'C': 9}])

print("Done.")
