import mysql_migration as mm

# Oracle connection
connection = mm.get_oracle_conn()

with connection:
  cursor = connection.cursor()
# -----------------------Select Employees-------------------------
  sql = '''select employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id
            from Employees'''
  cursor.execute(sql)
  rows = cursor.fetchall()
# -----------------------Select Jobs------------------------------
  sql_job = '''select job_id, job_title, min_salary, max_salary from Jobs'''
 
  cursor.execute(sql_job)
  job = cursor.fetchall()
# -----------------------Select Departments------------------------------
  sql_department = '''select department_id, department_name, manager_id from Departments'''
  cursor.execute(sql_department)
  department = cursor.fetchall()
# -----------------------Select Job_history--------------------------------
  sql_job_history = '''select employee_id, start_date, end_date, job_id, department_id from Job_history'''
  cursor.execute(sql_job_history)
  job_history = cursor.fetchall()


# Mysql connection
conn_dooodb = mm.get_mysql_conn('dooodb')
with conn_dooodb:
    cur = conn_dooodb.cursor()

# -----------------------Create Job-------------------------
    conn_dooodb.commit()
    cur.execute("call sp_drop_fk_refs('Job')")
    cur.execute("drop table if exists Job")
    job_create = '''create table Job(
                    id varchar(10) not null primary key,
                    job_title varchar(35) not null,
                    min_salary int unsigned,
                    max_salary int unsigned
                    )'''

    cur.execute(job_create)
    job_insert = '''insert into Job(id, job_title, min_salary, max_salary)
                    values(%s, %s, %s, %s)'''
    cur.executemany(job_insert, job)
    print("AffectedRowsJob-->", cur.rowcount)


# -----------------------Create Department-------------------------
    cur.execute("call sp_drop_fk_refs('Department')")
    cur.execute("drop table if exists Department")
    department_create = '''create table Department(
                   id smallint(4) not null auto_increment primary key,
                   department_name varchar(30) not null,
                   manager_id int unsigned
                   )'''

    cur.execute(department_create)
    department_insert = '''insert into Department(id, department_name, manager_id)
                   values(%s, %s, %s)'''
    cur.executemany(department_insert, department)
    print("AffectedRowsDepartment-->", cur.rowcount)

# -----------------------Create Job_history-------------------------
    cur.execute("call sp_drop_fk_refs('Job_history')")
    cur.execute("drop table if exists Job_history")
    job_history_create = '''create table Job_history(
                  employee_id int unsigned not null ,
                  start_date datetime not null ,
                  end_date datetime not null,
                  job_id varchar(10) not null,
                  department_id smallint(4),
                  primary key(employee_id, start_date)
                   );'''

    cur.execute(job_history_create)
    job_history_insert = '''insert into Job_history(employee_id, start_date, end_date, job_id, department_id)
                 values(%s, %s, %s, %s, %s)'''
    cur.executemany(job_history_insert, job_history)
    print("AffectedRowsJob_history-->", cur.rowcount)

# -----------------------Create Employee-------------------------
    cur.execute("call sp_drop_fk_refs('Employee')")
    cur.execute("drop table if exists Employee")
    sql_create = '''create table Employee(
                    id int unsigned not null auto_increment primary key,
                    first_name varchar(20),
                    last_name varchar(25) not null ,
                    email varchar(25) not null,
                    phone_number varchar(20),
                    hire_date datetime not null,
                    job_id varchar(10) not null,
                    salary int unsigned,
                    commission_pct decimal(3, 2),
                    manager_id int unsigned,
                    department_id smallint(4)
                    )'''
    cur.execute(sql_create)
    sql_insert = '''insert into Employee(id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) 
                    values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    cur.executemany(sql_insert,rows)
    print("AffectedRowsEmployee-->", cur.rowcount)



    conn_dooodb.commit()


conn_dooodb = mm.get_mysql_conn('dooodb')
with conn_dooodb:
    cur = conn_dooodb.cursor()
    employee_fk1 = "alter table Employee add constraint foreign key fk_emp_dept (department_id) references Department(id)"
    employee_fk2 = "alter table Employee add constraint foreign key fk_emp_job (job_id) references Job(id)"
    employee_fk3 = "alter table Employee add constraint foreign key fk_emp_manager (manager_id) references Employee(id)"
    job_history_fk1 = "alter table Job_history add constraint foreign key fk_jobhis_dept (department_id) references Department(id)"
    job_history_fk2 = "alter table Job_history add constraint foreign key fk_jobhis_emp (employee_id) references Employee(id)"
    job_history_fk3 = "alter table Job_history add constraint foreign key fk_jobhis_job (job_id) references Job(id)"
    department_fk1 = "alter table Department add constraint foreign key fk_dept_emp (manager_id) references Employee(id)"

    cur.execute(employee_fk1)
    cur.execute(employee_fk2)
    cur.execute(employee_fk3)
    cur.execute(job_history_fk1)
    cur.execute(job_history_fk2)
    cur.execute(job_history_fk3)
    cur.execute(department_fk1)

    conn_dooodb.commit()
