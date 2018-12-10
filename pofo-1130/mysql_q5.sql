create table Classroom (
id smallint unsigned not null auto_increment primary key,
name varchar(10) comment '강의실 이름'
);



alter table Subject add column classroom smallint unsigned not null;

alter table Subject add constraint foreign key fk_classroom_classroom(classroom) references Classroom(id); 


insert into Classroom(name)
 select concat(subj.name, '실') 
 from Subject subj inner join Classroom cla on subj.classroom = cla.id limit 10;
 

select subj.name as '과목', cla.name as '강의실'
from Subject subj inner join Classroom cla on subj.classroom = cla.id;

