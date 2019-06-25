create table Student (
id int(5) unsigned not null auto_increment primary key comment '학번', 
name varchar(10) not null comment '학생이름',
tel varchar (15) not null comment '전화번호',
email varchar(30) not null comment '이메일',
birth date not null comment '생일',
addr varchar(30) not null comment '주소'
);

create table Prof (
id smallint(5) unsigned not null auto_increment primary key,
name varchar(10) not null comment '교수 이름',
likecnt int(10) unsigned comment '좋아요 수'
);

create table Subject (
id smallint(5) unsigned not null auto_increment primary key,
name varchar(31) not null comment '과목이름',
prof smallint(5) unsigned not null comment '담당 교수',
constraint foreign key fk_prof_prof(prof) references Prof(id)
);

create table Enroll (
id int unsigned not null auto_increment primary key,
subject smallint(5) unsigned not null,
student int(5) unsigned not null, 
constraint foreign key fk_subject_subject(subject) references Subject(id) on delete cascade,
constraint foreign key fk_student_student(student) references Student(id) on delete cascade,
);

desc Student;
desc Enroll;

show index from Student;
show index from Enroll; 

