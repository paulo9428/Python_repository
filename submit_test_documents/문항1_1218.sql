## 문항1

create view v_stu_grade as 
select stu.id '학번', stu.name '학생명', count(*) '수강과목수', ceil((avg(midterm) + avg(finalterm)) / 2) '전과목 평균점수'       
from Grade g inner join Enroll en on g.enroll = en.id
			 inner join Student stu on en.student = stu.id
             inner join Subject subj on en.subject = subj.id
group by stu.id;


select * from v_stu_grade;

update Student set name = '오나라' where id = 1