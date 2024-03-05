Create keyspace keyspace1 with replication =
{'class':'SimpleStrategy','replication_factor': 3}; 
Use keyspace1;
Create table dept ( dept_id int PRIMARY KEY, dept_name text, 
dept_loc text);
Create table emp ( emp_id int PRIMARY KEY, emp_name text, 
dept_id int, email text, phone text );
Insert into dept (dept_id, dept_name, dept_loc) values (1001, 
'Accounts', 'Mumbai');
Insert into dept (dept_id, dept_name, dept_loc) values (1002, 
'Marketing', 'Delhi');
Insert into dept (dept_id, dept_name, dept_loc) values (1003, 
'HR', 'Chennai');
Insert into emp ( emp_id, emp_name, dept_id, email, phone ) 
values (1001, 'ABCD',1001, 'abcd@company.com', 
'1122334455');
Insert into emp ( emp_id, emp_name, dept_id, email, phone ) 
values (1002, 'DEFG',1002, 'defg@company.com', 
'2233445566');
Insert into emp ( emp_id, emp_name, dept_id, email, phone ) 
values (1003, 'GHIJ',1003, 'ghij@company.com', 
'3344556677');
select * from emp; 
select * from dept;
update dept set dept_name='Human Resource' where 
dept_id=1003;
delete from emp where emp_id=1006; 
select * from emp;
