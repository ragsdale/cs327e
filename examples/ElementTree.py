#!/usr/bin/env python3

# --------------
# ElementTree.py
# --------------

from xml.etree.ElementTree import Element, fromstring, tostring

print("ElementTree.py")
print()

def traverse (a, c = 0, d = "") :
    print(d + "(" + str(c) + ") " + a.tag)
    for v in a :
        c += 1
        c = traverse(v, c, d + "\t")
    print(d + "/" + a.tag)
    return c

s = "<xml>" + "".join(open("ElementTree.xml")) + "</xml>"
assert(type(s) is str)

a = fromstring(s)
assert(type(a) is Element)

print("*** The Whole Tree ***")
traverse(a)
print()

print("*** top two elements by indexing ***")
print(a[0].tag)
print(a[1].tag)
print()

print("*** top two elements by iterating ***")
p = iter(a)

e = next(p)
print(e.tag)

e = next(p)
print(e.tag)
print()

print("*** child element Team ***")
b = a.findall("Team")
for v in b :
    print(v)
print()

print("*** grandchild element JiaJia ***")
b = a.findall("*/JiaJia")
for v in b :
    print(v)
print()

print("*** all elements Team ***")
b = a.findall(".//Team")
for v in b :
    print(v)
print()

print("Done.")

"""
ElementTree.py

*** The Whole Tree ***
(0) xml
	(1) THU
		(2) Team
			(3) ACRush
			/ACRush
			(4) Jelly
			/Jelly
			(5) Cooly
			/Cooly
		/Team
		(6) JiaJia
			(7) Team
				(8) Ahyangyi
				/Ahyangyi
				(9) Dragon
				/Dragon
				(10) Cooly
					(11) Amber
					/Amber
				/Cooly
			/Team
		/JiaJia
	/THU
	(12) Team
		(13) Cooly
		/Cooly
	/Team
/xml

*** top two elements by indexing ***
THU
Team

*** top two elements by iterating ***
THU
Team

*** child element Team ***
<Element 'Team' at 0x10e0c8db8>

*** grandchild element JiaJia ***
<Element 'JiaJia' at 0x10e0c8af8>

*** all elements Team ***
<Element 'Team' at 0x10e0c8940>
<Element 'Team' at 0x10e0c8b50>
<Element 'Team' at 0x10e0c8db8>

Done.
"""
