## 문항6 (조별 과제)

create table Grade(
id int unsigned not null auto_increment primary key,
enroll int(10) unsigned ,
mid smallint default 0,
final smallint default 0,
constraint foreign key fk_enroll_enroll(enroll) references Enroll(id)
); 

start transaction;

insert into Grade(enroll) select id from Enroll order by rand() limit 10;

update Grade set mid = ceil((0.5 + rand()/2) * 100) where id > 0;
update Grade set final = ceil((0.5 + rand()/2) * 100) where id > 0;



## Report 1

select subj.name as '과목명', stu.name as '학생명', g.mid as '중간 점수', g.final as '기말 점수', (g.mid+g.final) as '총점', cast((g.mid+g.final)/2 as signed integer) as '평균',
case  
when cast((g.mid+g.final)/2 as signed integer) >= 90 then 'A'
when cast((g.mid+g.final)/2 as signed integer) >= 80 then 'B'
when cast((g.mid+g.final)/2 as signed integer) >= 70 then 'C'
when cast((g.mid+g.final)/2 as signed integer) >= 60 then 'D'
else 'F' 
End as '학점'
from Enroll en inner join Subject subj on en.subject = subj.id
			   inner join Student stu on en.student = stu.id
               inner join Grade g on en.id = g.enroll


## Report 2 

start transaction;

select subj.name as '과목명', s.name as '학생명', g.mid '중간' , g.final '기말' , (g.mid + g.final) 총점,
cast((g.mid + g.final) / 2 as signed integer) 평균,
case when cast((g.mid + g.final) / 2 as signed integer)>= 90 then 'A'
     when cast((g.mid + g.final) / 2 as signed integer) >= 80 then 'B'
     when cast((g.mid + g.final) / 2 as signed integer) >= 70 then 'C'
     when cast((g.mid + g.final) / 2 as signed integer) >= 60 then 'D'
else 'F' 
end '학점'
from Enroll en inner join Subject subj on en.subject = subj.id
			   inner join Student stu on en.student = stu.id
               inner join Grade g on en.id = g.enroll
group by en.subject
order by '과목명'

commit;



## Report 3

start transaction;

select max(stu.name) as '학생명', count(*) as '과목 수', sum(g.mid) + sum(g.final) as '총점', cast((sum(g.mid) + sum(g.final)) / (count(en.subject) * 2) as signed integer) as '평균',
case when
cast((sum(g.mid) + sum(g.final)) / (count(en.subject) * 2) as signed integer) >= 90 then 'A'
when
cast((sum(g.mid) + sum(g.final)) / (count(en.subject) * 2) as signed integer) >= 80 then 'B'
when
cast((sum(g.mid) + sum(g.final)) / (count(en.subject) * 2) as signed integer) >= 70 then 'C'
when
cast((sum(g.mid) + sum(g.final)) / (count(en.subject) * 2) as signed integer)>= 60 then 'D'
else 'F' 
end as '학점'
from Enroll en inner join Subject subj on en.subject = subj.id
			   inner join Student stu on en.student = stu.id
               inner join Grade g on en.id = g.enroll

group by en.student
order by '학점', '학생명';

commit;
