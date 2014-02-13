#!/usr/bin/env python3

"""
CS327e: Quiz #11 (5 pts) <Aizhuldyz>
"""

""" ----------------------------------------------------------------------
 1. In the paper, "A Bug and a Crash" about the Ariane 5, what was the
    software bug?
    (1 pt)

the conversion of a 64-bit number to a 16-bit number
"""

""" ----------------------------------------------------------------------
 2. In the paper, "Mariner 1", what was the software bug?
    (1 pt)

the ommission of a hyphen
"""

""" ----------------------------------------------------------------------
 3. What's the output of the following?
    (2 pts)

2
3
"""

a = [2, 3, 4]
p = iter(a)

v = next(p)
print(v)

v = next(p)
print(v)
