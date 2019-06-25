select em.last_name '이름', em.salary '급여', dept.department_name '부서 이름'
  from Employees em inner join Departments dept on em.department_id = dept.department_id
 where dept.department_name = 'Marketing'
   and em.salary < (select avg(salary) from Employees where department_id = 80);
