all:
	make WCDB.zip

clean:
	rm -f *.pyc
	rm -f RunWCDB.out
	rm -f RunWCDB.tmp
	rm -f TestWCDB.out
	rm -f WCDB.html
	rm -f WCDB.log
	rm -f WCDB.zip

diff: RunWCDB.in RunWCDB.py WCDB.py
	RunWCDB.py < RunWCDB.in > RunWCDB.tmp
	diff RunWCDB.out RunWCDB.tmp
	rm RunWCDB.tmp

turnin-list:
	turnin --list aizhuli cs327epj3

turnin-submit: WCDB.zip
	turnin --submit aizhuli cs327epj3 WCDB.zip

turnin-verify:
	turnin --verify aizhuli cs327epj3

WCDB.html: WCDB.py
	pydoc -w WCDB

WCDB.log:
	git log > WCDB.log

WCDB.zip: makefile                          \
          WCDB.html WCDB.log WCDB.py        \
          WCDB.xml WCDB.xsd.xml             \
          RunWCDB.in RunWCDB.out RunWCDB.py \
          TestWCDB.py TestWCDB.out
	zip -r WCDB.zip                          \
           makefile                          \
           WCDB.html WCDB.log WCDB.py        \
           WCDB.xml WCDB.xsd.xml             \
           RunWCDB.in RunWCDB.out RunWCDB.py \
           TestWCDB.py TestWCDB.out

RunWCDB.out: RunWCDB.in RunWCDB.py WCDB.py
	RunWCDB.py < RunWCDB.in > RunWCDB.out

TestWCDB.out: TestWCDB.py WCDB.py
	TestWCDB.py >& TestWCDB.out
