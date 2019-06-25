start transaction;

insert into Enroll(student, subject)
 select id, (select id from Subject order by rand() limit 1) sid from Student 
 order by rand() limit 100 
on duplicate key update student = student ;


#검증
select s.name, subj.name
 from Enroll e inner join Student s on e.student = s.id
			   inner join Subject subj on e.subject = subj.id;



commit;

rollback;