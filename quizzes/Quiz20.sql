/*
CS327e: Quiz #20 (5 pts) <Fiona>
*/

/* -----------------------------------------------------------------------
 1. What is the output of the following?
    (4 pts)

A B C
1 6 7
2 7 8
2 7 9
3 8 null
*/

create table R (A int, B int);
create table S (A int, C int);

insert into R values (1, 6);
insert into R values (2, 7);
insert into R values (3, 8);

insert into S values (4, 6);
insert into S values (1, 7);
insert into S values (2, 8);
insert into S values (2, 9);

select * from R left join S using (A);
