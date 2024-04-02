create database najottalim;
create table students(id serial primary key, f_name varchar(20), l_name varchar(20), age int);
create table teachers(id serial primary key, f_name varchar(20), l_name varchar(20), student_id int, filial varchar(20));
create table filial(id serial primary key, teacher_id int, student_id int);

insert into students (id, f_name, l_name, age) values (1, 'Matilda', 'Lording', 32);
insert into students (id, f_name, l_name, age) values (2, 'Verine', 'Brader', 12);
insert into students (id, f_name, l_name, age) values (3, 'Karlan', 'Dunbobin', 22);
insert into students (id, f_name, l_name, age) values (4, 'Barrett', 'Comolli', 33);
insert into students (id, f_name, l_name, age) values (5, 'Corny', 'Woodroffe', 16)
insert into students (id, f_name, l_name, age) values (6, 'Callida', 'Wager', 26)
insert into students (id, f_name, l_name, age) values (7, 'Danette', 'Kennermann', 22)
insert into students (id, f_name, l_name, age) values (8, 'Merola', 'Clubb', 19)
insert into students (id, f_name, l_name, age) values (9, 'Marketa', 'Tabour', 33)
insert into students (id, f_name, l_name, age) values (10, 'Sibyl', 'Infante', 15)


