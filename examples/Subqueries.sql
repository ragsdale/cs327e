use downing_test;

/* -----------------------------------------------------------------------
Drop
*/

select "Drop";

drop table if exists Student;
drop table if exists Apply;
drop table if exists College;

/* -----------------------------------------------------------------------
Create
*/

select "Create";

create table Student (
    sID    int,
    sName  text,
    GPA    float,
    sizeHS int);

create table Apply (
    sID      int,
    cName    text,
    major    text,
    decision boolean);

create table College (
    cName      text,
    state      char(2),
    enrollment int);

/* -----------------------------------------------------------------------
Insert
*/

select "Insert";

insert into Student values (123, 'Amy',    3.9,  1000);
insert into Student values (234, 'Bob',    3.6,  1500);
insert into Student values (320, 'Lori',   null, 2500);
insert into Student values (345, 'Craig',  3.5,   500);
insert into Student values (432, 'Kevin',  null, 1500);
insert into Student values (456, 'Doris',  3.9,  1000);
insert into Student values (543, 'Craig',  3.4,  2000);
insert into Student values (567, 'Edward', 2.9,  2000);
insert into Student values (654, 'Amy',    3.9,  1000);
insert into Student values (678, 'Fay',    3.8,   200);
insert into Student values (765, 'Jay',    2.9,  1500);
insert into Student values (789, 'Gary',   3.4,   800);
insert into Student values (876, 'Irene',  3.9,   400);
insert into Student values (987, 'Helen',  3.7,   800);

insert into Apply values (123, 'Berkeley', 'CS',             true);
insert into Apply values (123, 'Cornell',  'EE',             true);
insert into Apply values (123, 'Stanford', 'CS',             true);
insert into Apply values (123, 'Stanford', 'EE',             false);
insert into Apply values (234, 'Berkeley', 'biology',        false);
insert into Apply values (321, 'MIT',      'history',        false);
insert into Apply values (321, 'MIT',      'psychology',     true);
insert into Apply values (345, 'Cornell',  'bioengineering', false);
insert into Apply values (345, 'Cornell',  'CS',             true);
insert into Apply values (345, 'Cornell',  'EE',             false);
insert into Apply values (345, 'MIT',      'bioengineering', true);
insert into Apply values (543, 'MIT',       'CS',            false);
insert into Apply values (678, 'Stanford', 'history',        true);
insert into Apply values (765, 'Cornell',  'history',        false);
insert into Apply values (765, 'Cornell',  'psychology',     true);
insert into Apply values (765, 'Stanford', 'history',        true);
insert into Apply values (876, 'MIT',      'biology',        true);
insert into Apply values (876, 'MIT',      'marine biology', false);
insert into Apply values (876, 'Stanford', 'CS',             false);
insert into Apply values (987, 'Berkeley', 'CS',             true);
insert into Apply values (987, 'Stanford', 'CS',             true);

insert into College values ('Berkeley', 'CA', 36000);
insert into College values ('Cornell',  'NY', 21000);
insert into College values ('Irene',    'TX', 25000);
insert into College values ('MIT',      'MA', 10000);
insert into College values ('Stanford', 'CA', 15000);

/* -----------------------------------------------------------------------
Select
*/

select "Select";

select *
    from Student
    order by sID;

select *
    from Apply
    order by sID;

select *
    from College
    order by cName;

/* -----------------------------------------------------------------------
ID, name, and GPA of students who applied in CS
*/

select "ID, name, and GPA of students who applied in CS";

select "this is not right, why? - duplicates";

select *
    from Student
    inner join Apply using (sID)
    where major = 'CS'
    order by sID;

select sID, sName, GPA
    from Student
    inner join Apply using (sID)
    where major = 'CS'
    order by sID;

select "this is right";

select distinct sID, sName, GPA
    from Student
    inner join Apply using (sID)
    where major = 'CS'
    order by sID;

select "this is also right, using subquery, with in";

select sID, sName, GPA
    from Student
    where sID in
        (select distinct sID from Apply where major = 'CS')
    order by sID;

/* -----------------------------------------------------------------------
GPA of students who applied in CS
*/

select "GPA of students who applied in CS";

select "this is not right, why? - duplicates";

select *
    from Student
    inner join Apply using (sID)
    where major = 'CS'
    order by GPA desc;

select GPA
    from Student
    inner join Apply using (sID)
    where major = 'CS'
    order by GPA desc;

select "this is not right either, why? - removed some wrong duplicates";

select distinct GPA
    from Student
    inner join Apply using (sID)
    where major = 'CS'
    order by GPA desc;

select "this is right, using subquery, with in";

select *
    from Student
    where sID in (select distinct sID from Apply where major = 'CS')
    order by GPA desc;

select GPA
    from Student
    where sID in (select distinct sID from Apply where major = 'CS')
    order by GPA desc;

/* -----------------------------------------------------------------------
ID of students who have applied to major in CS but not in EE
*/

select "ID of students who have applied to major in CS but not in EE";

select "this is not right, why? - includes students majoring in non-CS, non-EE";

select *
    from Apply as R
    inner join Apply as S using (sID)
    where R.major  = 'CS'  and
          S.major != 'EE';

select distinct R.sID
    from Apply as R
    inner join Apply as S using (sID)
    where R.major  = 'CS'  and
          S.major != 'EE';

select "this is right, using subquery, with in and not in";

select sID
    from Student
    where
        sID in     (select sID from Apply where major = 'CS')
        and
        sID not in (select sID from Apply where major = 'EE');

/* -----------------------------------------------------------------------
colleges, such that there's another college in the same state
*/

select "colleges, such that there's another college in the same state";

select *
    from College as R inner join College as S
    where (R.cName != S.cName) and
          (R.state =  S.state)
    order by R.cName;

select R.cName, R.state
    from College as R inner join College as S
    where (R.cName != S.cName) and
          (R.state =  S.state)
    order by R.cName;

select "using as, using subquery, with exists";

select cName, state
    from College as R
    where exists
        (select *
            from College as S
            where (R.cName != S.cName) and
                  (R.state =  S.state));

/* -----------------------------------------------------------------------
colleges with highest enrollment
*/

select "colleges with highest enrollment";

select "using subquery, with not exists";

select cName, enrollment
    from College as R
    where not exists
        (select *
            from College as S
            where R.enrollment < S.enrollment);

select "using subquery, with all";

select cName, enrollment
    from College
    where enrollment >= all
        (select enrollment
            from College
            where enrollment is not null);

/* -----------------------------------------------------------------------
students with highest GPA
*/

select "students with highest GPA";

select "using subquery, with not exists, is insufficient, why? - because of nulls";

select sID, sName, GPA
    from Student as R
    where not exists
        (select *
            from Student as S
            where R.GPA < S.GPA)
    order by sID;

select "this is right";

select sID, sName, GPA
    from Student as R
    where
        not exists
            (select *
                from Student as S
                where R.GPA < S.GPA)
        and
        (GPA is not null)
    order by sID;

select "this is also right, using subquery, with all";

select sID, sName, GPA
    from Student
    where GPA >= all
        (select GPA
            from Student
            where GPA is not null)
    order by sID;

/* -----------------------------------------------------------------------
Drop
*/

drop table if exists Student;
drop table if exists Apply;
drop table if exists College;

exit
