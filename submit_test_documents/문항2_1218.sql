
DELIMITER $$

CREATE Function f_student_avg(stu_id int(10)) 
 RETURNS smallint(10)
 
BEGIN

select ceil((avg(midterm) + avg(finalterm)) / 2)       
from Grade g inner join Enroll en on g.enroll = en.id
			 inner join Student stu on en.student = stu.id
             inner join Subject subj on en.subject = subj.id
group by stu.id
	
    
RETURN ceil((avg(midterm) + avg(finalterm)) / 2) 

END $$
DELIMITER ;

select f_student_avg();

declare _stu int(10);

select id into _stu from Student;  