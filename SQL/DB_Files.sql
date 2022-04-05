
Create table Student (

sid int,
sname text, 
hometown text,
PRIMARY KEY(sid)

)
;


Create table Company(

cid int,
company text,
primary key (cid)
)
;




Create Table Internship(

    sid int ,
    cid int ,
    hourlySalary int,
    FOREIGN key (sid) references Student (sid),
    FOREIGN key (cid) references Company (cid)


)



;




Insert INTO Student VALUES

  ( 1000 , 'Margaret', 'Carmel'),
  ( 1002 , 'James'   , 'NYC'),
  ( 1003 , 'Zack'    , 'LA'),
  ( 1004 , 'Candice' , 'Chicago'),
  ( 1005 , 'Bob'     , 'Loisiville'),
  ( 1006 , 'Jackson', 'Talahassee'),
  ( 1007 , 'George',  'Miami'),
  ( 1008 , 'David',  'Albany'),
  ( 1009 , 'Nickolas', 'St.Charles'),
  ( 1010 , 'Christian',  'Denver'),
  ( 1011 , 'Margaret',  'SanFrancisco'),
  ( 1012 , 'Ashley','Delhi'),
  ( 1013 , 'Mohamme', 'Paris'),
  ( 1014 , 'Edward',  'Elizabeth'),
  ( 1015 , 'Benjamin',  'Ft.Wayne'),
  ( 1016 , 'Samantha',  'Indianapolis'),
  ( 1017 , 'Jody',  'London'),
  ( 1018 , 'Eduardo', 'Cairo')
    





;
INSERT INTO Company VALUES

(100,'Apple'),
(101, 'Google'),
(102,'Aldis'),
(103,'Amazon'),
(104,'Chase'),
(105,'Microsoft'),
(106, 'Twitter'),
(107,'Mom&Pop'),
(108,'LocalCompany'),
(109, 'Zappos')

  
;

Insert INTO Internship Values

(1000 ,100, 12),
(1002 ,102, 10),
(1003 ,100, 15),
(1004 ,103, 23),
(1005 ,106, 22),
(1006, 107, 13),
(1007 ,109, 14),
(1008 ,100, 18),
(1010 ,107, 20),
(1011 ,105, 18),
(1012 ,105, 12),
(1015,105, 16),
(1016 ,106, 14),
(1017 ,101, 13),
(1018, 101, 4)


;



-- Show me everythign from student table



-- Tell me all students names and their salary for everyone whose hourly salary is over 18
;



;
-- join the tables and do the same thing (note the differences)



--Find the ids the 2 people with the same salary
;


;

-- Tell me their names using WITH  (Think of a way to remove duplicates)

;

;