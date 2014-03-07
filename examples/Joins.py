#!/usr/bin/env python3

# --------
# Joins.py
# --------

def cross_join_1 (r, s) :
    x = []
    for v in r :
        for w in s :
            y = {}
            for u in v :
                y[u] = v[u]
            for u in w :
                y[u] = w[u]
            x.append(y)
    return x

def cross_join_2 (r, s) :
    return [dict(list(v.items()) + list(w.items())) for v in r for w in s]

def theta_join_1 (r, s, bp) :
    x = []
    for v in r :
        for w in s :
            if bp(v, w) :
                y = {}
                for u in v :
                    y[u] = v[u]
                for u in w :
                    y[u] = w[u]
                x.append(y)
    return x

def theta_join_2 (r, s, bp) :
    return [dict(list(v.items()) + list(w.items())) for v in r for w in s if bp(v, w)]

print("Joins.py")

r = [ \
    {"A" : 1, "B" : 6},
    {"A" : 2, "B" : 7},
    {"A" : 3, "B" : 8}]
assert(len(r) == 3)

s = [ \
    {"A" : 4, "C" : 6},
    {"A" : 1, "C" : 7},
    {"A" : 2, "C" : 8},
    {"A" : 2, "C" : 9}]
assert(len(s) == 4)

def test (f) :
    x = f(r, s)
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

test(cross_join_1)
test(cross_join_1)

def test (f) :
    x = f(r, s, lambda v, w : v["A"] == w["A"])
    assert(len(x) == 3)
    assert(
        x
        ==
        [{'A': 1, 'B': 6, 'C': 7},
         {'A': 2, 'B': 7, 'C': 8},
         {'A': 2, 'B': 7, 'C': 9}])

test(theta_join_1)
test(theta_join_1)

print("Done.")
