#!/usr/bin/env python3

# --------------
# ElementTree.py
# --------------

from xml.etree.ElementTree import Element, fromstring

print("ElementTree.py")
print()

s = "<xml>" + "".join(open("ElementTree.xml")) + "</xml>"
assert(type(s) is str)
print(s)
print()

x = fromstring(s)
assert(type(x) is Element)

print("First Leve Elements")
print()
for u in x :
    print(u)
print()

print("Second Level Elements")
print()
for u in x :
    for v in u :
        print(v)
print()

print("Third Level Elements")
print()
for u in x :
    for v in u :
        for w in v :
            print(w)
print()

print("Done.")

"""
ElementTree.py

<xml><THU>
	<Team>
		<ACRush></ACRush>
		<Jelly></Jelly>
		<Cooly></Cooly>
	</Team>
	<JiaJia>
		<Team>
			<Ahyangyi></Ahyangyi>
			<Dragon></Dragon>
			<Cooly><Amber></Amber></Cooly>
		</Team>
	</JiaJia>
</THU>
<Team><Cooly></Cooly></Team>
</xml>

<Element 'THU' at 0x10ba256d8>
<Element 'Team' at 0x10ba25788>
<Element 'JiaJia' at 0x10ba25940>

<Element 'Team' at 0x10ba25c00>
<Element 'Cooly' at 0x10ba25c58>

Done.
"""
