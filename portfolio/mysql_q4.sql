create table Dept(
id smallint unsigned not null auto_increment primary key,
name varchar(10) comment '학과명',
prof smallint(5) unsigned comment '지도교수',
student int(5) unsigned not null comment '과대표',
constraint foreign key fk_prof_prof(prof) references Prof(id),
constraint foreign key fk_student_student(student) references Student(id)
); 

insert into Dept set name = '천문학과' ;

insert into Dept(prof) select id from Prof order by rand() limit 5; 
insert into Dept(student) select id from Student order by rand() limit 5; 
 
 
alter table Student add column dept smallint unsigned not null;
alter table Student add constraint foreign key fk_dept_dept(dept) references Dept(id);

select stu.name(*) as '학생', dept.name(*) as '해당 과'
from Student stu inner join Dept dept on stu.dept = dept.id;