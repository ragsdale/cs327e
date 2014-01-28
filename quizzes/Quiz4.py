#!/usr/bin/env python

"""
CS327e: Quiz #4 (5 pts) <Fiona>
"""

""" ----------------------------------------------------------------------
 1. SQL statements are divided into three categories:
        Data Manipulation Language (DML)
        Data Definition   Language (DDL)
        Data Control      Language (DCL)
    Give one example of any of the three.
    But you must correctly identify the category.
    [SQL: Intro, Pg. xv]
    (1 pt)

DML: select, insert, update
DDL: create, alter, drop
DCL: grant, revoke
"""

""" ----------------------------------------------------------------------
 2. What git command was issued in three locations below?
    (3 pts)

a. added file "Add.txt"
b. git add Add.txt
c. git commit -m "..."
"""

% git status
# On branch master
nothing to commit (working directory clean)

% <a. what happened here>

% git status
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#   Add.txt
nothing added to commit but untracked files present (use "git add" to track)

% <b. what happened here>

% git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#   new file:   Add.txt
#

% <c. what happened here>

% git status
# On branch master
nothing to commit (working directory clean)
