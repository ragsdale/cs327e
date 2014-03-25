#!/usr/bin/env python3

# --------
# Login.py
# --------

import _mysql

def login () :
    c = _mysql.connect(
            host   = "z",
            user   = "<username>",
            passwd = "<password>",
            db     = "downing_test")
    assert str(type(c)) == "<type '_mysql.connection'>"
    return c
