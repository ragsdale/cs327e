all:
	make XML.zip

clean:
	rm -f XML.html
	rm -f XML.log
	rm -f XML.zip
	rm -f RunXML.out
	rm -f RunXML.tmp
	rm -f TestXML.out
	rm -f *.pyc

diff: RunXML.in RunXML.py XML.py
	RunXML.py < RunXML.in > RunXML.tmp
	diff RunXML.out RunXML.tmp
	rm RunXML.tmp

turnin-list:
	turnin --list thunt cs373pj2

turnin-submit: XML.zip
	turnin --submit thunt cs373pj2 XML.zip

turnin-verify:
	turnin --verify thunt cs373pj2

XML.html: XML.py
	pydoc -w XML

XML.log:
	git log > XML.log

XML.zip: makefile                           \
             XML.html XML.log XML.py        \
             RunXML.in RunXML.out RunXML.py \
             TestXML.py TestXML.out
	zip -r XML.zip                        \
           makefile                       \
           XML.html XML.log XML.py        \
           RunXML.in RunXML.out RunXML.py \
           TestXML.py TestXML.out

RunXML.out: RunXML.in RunXML.py XML.py
	RunXML.py < RunXML.in > RunXML.out

TestXML.out: TestXML.py XML.py
	TestXML.py >& TestXML.out
