/*
CS327e: Quiz #24 (5 pts) <Fiona>
*/

/* -----------------------------------------------------------------------
 1. Consider the following two queries for finding the ID of students who
    applied in CS but NOT in EE.
    Which one is correct?
    Why is the incorrect one incorrect?
    (4 pts)

the first is incorrect
it finds the IDs of all students who applied in CS regardless of any other
applications
*/

select distinct R.sID
    from Apply as R
    inner join Apply as S using (sID)
    where R.major  = 'CS'  and
          S.major != 'EE';

select sID
    from Student
    where
        sID in     (select sID from Apply where major = 'CS')
        and
        sID not in (select sID from Apply where major = 'EE');
