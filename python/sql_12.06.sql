CREATE TABLE `Student` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `tel` varchar(30) CHARACTER SET latin1 NOT NULL,
  `email` varchar(45) CHARACTER SET latin1 NOT NULL,
  `birth` date DEFAULT NULL,
  `addr` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8;
;


create table Club(
    id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null,
    createdate timestamp not null default current_timestamp,
    leader int unsigned,
    constraint foreign key fk_leader_student(leader) references Student(id)
);



create table Subject(
    id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null,
    prof smallint unsigned,
    constraint foreign key fk_prof_prof (prof) references Prof(id)
    on delete set null
);



create table Enroll(
    id int unsigned not null auto_increment primary key,
    subject smallint unsigned not null,
    student int unsigned not null,
    constraint foreign key fk_subject (subject) references Subject(id) on delete cascade,
    constraint foreign key fk_student (student) references Student(id) on delete cascade
    );
    
create table Prof(
    id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null,
    likecnt int not null default 0
);

