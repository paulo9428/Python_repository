DROP Procedure IF EXISTS prof_recommend;

DELIMITER $$
CREATE Procedure prof_recommend(in  , out ) 

BEGIN
	
declare _stu_cnt smallint(10)
declare _stu_grade int(15)
declare _prof_hot int(15)

_prof_hot = (_stu_cnt * 0.4) + (_stu_grade * 0.6)

create temporary table popul_prof(
name varchar(10) '교수명'
popul_point int(15) '인기도'
);

insert into popul_prof 


select *
from popul_prof
order by popul_point limit 3;   
    
END $$
DELIMITER ;

call prof_recommend(_stu_cnt, _stu_grade);

select   
from Grade g inner join enroll en on g.enroll = en.id
             inner join Subject subj on en.subject = subj.id
			 inner join Prof p on subj.prof = p.id


select count(*)
from Subject subj inner join Prof p on subj.prof = p.id
group by subj.id

##기준 수강학생 수: 0.4 , 좋아요 수: 0.6 

##커서, 임시테이블?