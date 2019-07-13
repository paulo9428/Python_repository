drop table if exists Employee;
drop table if exists Job;
drop table if exists Job_history;
drop table if exists Department;

create table Employee(
id int unsigned not null auto_increment primary key,
first_name varchar(20),
last_name varchar(25) not null ,
email varchar(25) not null,
phone_number varchar(20),
hire_date date not null,
job_id varchar(10) not null,
salary int unsigned,
commision_pct decimal(3, 2),
manager_id int unsigned,
department_id smallint(4)

);


create table Job(
id varchar(10) not null primary key,
job_title varchar(35) not null,
min_salary int unsigned,
max_salary int unsigned
);


create table Job_history(
employee_id int unsigned not null ,
start_date date not null ,
end_date date not null,
job_id varchar(10) not null,
department_id smallint(4),
primary key(employee_id, start_date)
);


create table Department(
id smallint(4) not null auto_increment primary key,
department_name varchar(30) not null,
manager_id int unsigned
);

alter table Employee add constraint foreign key fk_emp_dept (department_id) references Department(id);
alter table Employee add constraint foreign key fk_emp_job (job_id) references Job(id);
alter table Employee add constraint foreign key fk_emp_manager (manager_id) references Employee(id);

alter table Job_history add constraint foreign key fk_jobhis_dept (department_id) references Department(id);
alter table Job_history add constraint foreign key fk_jobhis_emp (employee_id) references Employee(id);
alter table Job_history add constraint foreign key fk_jobhis_job (job_id) references Job(id);


alter table Department add constraint foreign key fk_dept_emp (manager_id) references Employee(id);
