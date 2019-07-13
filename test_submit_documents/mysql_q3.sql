create table Club(
id smallint unsigned not null auto_increment primary key,
name varchar(10) not null comment '클럽 이름',
leader int(5) unsigned not null comment '클럽장',
constraint foreign key fk_leader_student(leader) references Student(id)
);






create table ClubMember(
id int unsigned not null auto_increment primary key,
club smallint unsigned not null comment '동아리',
student int unsigned not null comment '학생',
level tinyint(5) not null comment '레벨',
constraint foreign key fk_club_club(club) references Club(id),
constraint foreign key fk_student_student(student) references Student(id)
);

insert into ClubMember(club, student)
 select