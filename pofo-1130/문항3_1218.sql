DELIMITER //
Create Trigger trig_club_stu
  after insert
  on Club FOR EACH ROW
BEGIN
	
    insert into Clubmember set name = new.id
    
    
    insert into Clubmember(student, level) 
     select id, 2 from Student 
     where (select cm.level from Student stu inner join ClubMember cm on stu.id = cm.student limit 1) = 0
     order by rand()
    
	
    
END //
DELIMITER ;

insert into Club set name = '농구부';

select * from ClubMember
 where club = (select max(id) from Club);

