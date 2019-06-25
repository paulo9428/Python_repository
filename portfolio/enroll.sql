insert into Prof(name, likecnt) select name, ceil(rand() * 100) from Student order by rand() limit 100;



insert into Subject(name, prof) select '국어', id from Prof order by rand() limit 100;
 
update Subject set name='수학' where name='국어' and id != 10 limit 1;
 

insert into Enroll(subject, student)
select sbj.id, s.id
  from (select id from Subject where id not in (select distinct subject from Enroll) order by id limit 1) sbj, 
       (select id from Student order by rand() limit 100) s;
       
