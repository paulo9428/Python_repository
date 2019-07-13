import mysql_migration as mm


# -------------검증 1번-------------------
conn_dooodb = mm.get_mysql_conn('dooodb')
with conn_dooodb:
    dooo_cnt_emp = mm.get_count(conn_dooodb, 'Employee')
    dooo_cnt_dept = mm.get_count(conn_dooodb, 'Department')
    dooo_cnt_job = mm.get_count(conn_dooodb, 'Job')
    dooo_cnt_jobhis = mm.get_count(conn_dooodb, 'Job_history')

connection = mm.get_oracle_conn()
with connection:
    ora_cnt_emp = mm.get_count(connection, 'Employees')
    ora_cnt_dept = mm.get_count(connection, 'Departments')
    ora_cnt_job = mm.get_count(connection, 'Jobs')
    ora_cnt_jobhis = mm.get_count(connection, 'Job_history')

#--------------------------------검증 2번 함수화------------------------------------



ora_emp_column = 'employee_id, first_name, last_name, email, phone_number, hire_date, job_id, round(salary), round(commission_pct * 100), manager_id, department_id'
mys_emp_column = 'id, first_name, last_name, email, phone_number, hire_date, job_id, round(salary), round(commission_pct * 100), manager_id, department_id'

ora_dept_column = 'department_id, department_name, manager_id'
mys_dept_column = 'id, department_name, manager_id'       

ora_job_column = 'job_id, job_title, min_salary, max_salary'
mys_job_column = 'id, job_title, min_salary, max_salary'

ora_jobhis_column = 'employee_id, start_date, end_date, job_id, department_id'
mys_jobhis_column = 'employee_id, start_date, end_date, job_id, department_id'

counts = [(dooo_cnt_emp, ora_cnt_emp), (dooo_cnt_dept, ora_cnt_dept), (dooo_cnt_job, ora_cnt_job), (dooo_cnt_jobhis, ora_cnt_jobhis) ]
ora_column = [ora_emp_column, ora_dept_column, ora_job_column, ora_jobhis_column]
ora_table = ['Employees', 'Departments', 'Jobs', 'Job_history' ]
mys_column = [mys_emp_column, mys_dept_column, mys_job_column, mys_jobhis_column]
mys_table = ['Employee', 'Department', 'Job', 'Job_history' ]
mys_id = ['id', 'id', 'id', 'employee_id']

for k in range(0,4):
    if counts[k][0] != counts[k][1]:
        print("=================== ", mys_table[k], " Failed=======================")
        break
    else:
        mm.valid (ora_column[k], ora_table[k] , mys_column[k], mys_table[k], mys_id[k] )
