#!/usr/bin/env python3

"""
CS327e: Quiz #9 (5 pts) <Aizhuldyz>
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (4 pts)

THU
Team
JiaJia

Team
Cooly

"""

"""
Quiz9.xml contains the following:

<THU>
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
"""

from xml.etree.ElementTree import fromstring

s = "<xml>" + "".join(open("Quiz9.xml")) + "</xml>"

x = fromstring(s)

for u in x :
    print(u.tag)
    for v in u :
        print(v.tag)
    print()
