#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[2]:


Password_DB = "pw"


# In[3]:


from urllib.parse import quote
password = quote("pw")
connection_url = f"postgresql://postgres:{pw}@localhost:5432/cohort_4"


# In[4]:


get_ipython().run_line_magic('sql', '$connection_url')


# # 1. Problem Statement: Assume there are two tables, orders and order_details . Write an SQL query to retrieve all orders along with their corresponding order details where the total price of the order is greater than 100.

# In[6]:


get_ipython().run_cell_magic('sql', '', '\nCREATE TABLE orders1 (\norder_id INT PRIMARY KEY,\ncustomer_id INT,\norder_date DATE\n);\n\nCREATE TABLE order_details (\ndetail_id INT PRIMARY KEY,\norder_id INT,\nproduct_id INT,\nquantity INT,\nprice DECIMAL(10, 2)\n);\n')


# In[7]:


get_ipython().run_cell_magic('sql', '', "\nINSERT INTO orders1 (order_id, customer_id, order_date) VALUES\n(1, 1, '2021-01-01'),\n(2, 2, '2021-01-02'),\n(3, 1, '2021-01-03'),\n(4, 3, '2021-01-04');\n\nINSERT INTO order_details (detail_id, order_id, product_id, quantity, price) VALUES\n(1, 1, 1, 2, 50),\n(2, 1, 2, 1, 30),\n(3, 2, 3, 3, 20),\n(4, 3, 1, 3, 40);\n")


# In[22]:


get_ipython().run_cell_magic('sql', '', '\nINSERT INTO order_details (detail_id, order_id, product_id, quantity, price) VALUES \n(5, 4, 2, 2, 25),\n(6, 4, 3, 1, 15);\n')


# In[23]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM orders1\n')


# In[24]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM order_details\n')


# In[28]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * from order_details WHERE price*quantity > 100\n')


# In[7]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM orders1 as o\nJOIN order_details as d\nON o.order_id = d.order_id\n\nWHERE price*quantity > 100\n')


# # 2.  Problem Statement: Assume there are two tables, employees and departments . Write an SQL query to retrieve all employees along with their corresponding department name.

# In[8]:


get_ipython().run_cell_magic('sql', '', '\n\nCREATE TABLE departments (\ndept_id INT PRIMARY KEY,\ndept_name VARCHAR(50)\n);\n\nCREATE TABLE employees (\nemp_id INT PRIMARY KEY,\nemp_name VARCHAR(50),\ndept_id INT,\nhire_date DATE,\nsalary DECIMAL(10, 2)\n);\n')


# In[9]:


get_ipython().run_cell_magic('sql', '', "\nINSERT INTO departments (dept_id, dept_name) VALUES\n(1, 'IT'),\n(2, 'Finance'),\n(3, 'HR');\n\nINSERT INTO employees (emp_id, emp_name, dept_id, hire_date, salary) VALUES\n(1, 'John', 1, '2020-01-01', 50000),\n(2, 'Jane', 2, '2020-02-01', 60000),\n(3, 'Mark', 1, '2020-03-01', 55000),\n(4, 'Mike', 3, '2020-04-01', 65000);\n")


# In[10]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM departments\n')


# In[11]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM employees\n')


# In[12]:


get_ipython().run_cell_magic('sql', '', '\nSELECT emp_name FROM employees\n')


# In[15]:


get_ipython().run_cell_magic('sql', '', '\nSELECT e.emp_name, d.dept_name FROM employees as e\n\nJOIN departmentS as d\nON e.dept_id = d.dept_id\n\n\n')


# # 3.  Problem Statement: Assume there is a table sales with columns product_id , sale_date , and amount . Write an SQL query to retrieve the total sales amount for each product for the month of January 2021.

# In[16]:


get_ipython().run_cell_magic('sql', '', '\nCREATE TABLE sales (\nsale_id INT PRIMARY KEY,\nproduct_id INT,\nsale_date DATE,\namount DECIMAL(10, 2)\n);\n')


# In[17]:


get_ipython().run_cell_magic('sql', '', "\nINSERT INTO sales (sale_id, product_id, sale_date, amount) VALUES\n(1, 1, '2021-01-01', 100),\n(2, 2, '2021-01-02', 200),\n(3, 1, '2021-01-03', 150),\n(4, 3, '2021-01-04', 300),\n(5, 2, '2021-02-01', 250),\n(6, 3, '2021-02-02', 350);\n")


# In[18]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM sales\n')


# In[32]:


get_ipython().run_cell_magic('sql', '', '\nSELECT sum(amount) as total_sales_amount from sales WHERE EXTRACT(MONTH FROM sale_date) = 1\n')


# # 4. Problem Statement: Assume there is a table logins with columns user_id and login_time . Write an SQL query to retrieve the number of logins for each user for the month of January 2021.

# In[33]:


get_ipython().run_cell_magic('sql', '', '\nCREATE TABLE logins (\nlogin_id INT PRIMARY KEY,\nuser_id INT,\nlogin_time TIMESTAMP\n);\n')


# In[35]:


get_ipython().run_cell_magic('sql', '', "\nINSERT INTO logins (login_id, user_id, login_time) VALUES\n(1, 1, '2021-01-01 12:00:00'),\n(2, 2, '2021-01-01 13:00:00'),\n(3, 1, '2021-01-02 10:00:00'),\n(4, 3, '2021-01-02 11:00:00'),\n(5, 2, '2021-02-01 12:00:00'),\n(6, 3, '2021-02-01 13:00:00');\n")


# In[36]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM logins\n')


# In[343]:


get_ipython().run_cell_magic('sql', '', '\nSELECT user_id, count(*)from logins WHERE EXTRACT(MONTH FROM login_time)= 1 GROUP BY user_id\n')


# # 5. Assume there are two tables, customers and orders . Write an SQL query to retrieve all customers who have placed at least one order.

# In[73]:


get_ipython().run_cell_magic('sql', '', '\nCREATE TABLE orders2 (\norder_id INT PRIMARY KEY,\ncustomer_id INT,\norder_date DATE\n);\n')


# In[77]:


get_ipython().run_cell_magic('sql', '', '\nCREATE TABLE customers (\ncustomer_id INT PRIMARY KEY,\ncustomer_name VARCHAR(50),\naddress VARCHAR(100)\n);\n')


# In[78]:


get_ipython().run_cell_magic('sql', '', "\nINSERT INTO customers (customer_id, customer_name, address) VALUES\n(1, 'John', '123 Main St'),\n(2, 'Jane', '456 Oak Ave'),\n(3, 'Mark', '789 Elm St');\n\nINSERT INTO orders2 (order_id, customer_id, order_date) VALUES\n(1, 1, '2021-01-01'),\n(2, 2, '2021-01-02'),\n(3, 1, '2021-01-03'),\n(4, 3, '2021-01-04');\n")


# In[79]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM customers\n')


# In[80]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM orders2\n')


# In[82]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * from orders WHERE customer_id >= 1;\n')


# In[83]:


get_ipython().run_cell_magic('sql', '', '\nSELECT customer_id from orders WHERE customer_id >= 1;\n')


# In[85]:


get_ipython().run_cell_magic('sql', '', '\nSELECT customer_name from customers WHERE customer_id IN\n\n(SELECT customer_id from orders WHERE customer_id >= 1)\n')


# #  6. Assume there is a table transactions with columns transaction_id , user_id , and amount . Write an SQL query to retrieve the average transaction amount for each user.

# In[86]:


get_ipython().run_cell_magic('sql', '', '\nCREATE TABLE transactions (\ntransaction_id INT PRIMARY KEY,\nuser_id INT,\namount DECIMAL(10, 2)\n);\n')


# In[87]:


get_ipython().run_cell_magic('sql', '', '\nINSERT INTO transactions (transaction_id, user_id, amount) VALUES\n(1, 1, 50),\n(2, 2, 100),\n(3, 1, 75),\n(4, 3, 200),\n(5, 2, 125),\n(6, 3, 150);\n')


# In[88]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM transactions\n')


# In[105]:


get_ipython().run_cell_magic('sql', '', '\nSELECT user_id, count(*), SUM(amount) as Total_Number_amount from transactions GROUP BY user_id \n')


# In[345]:


get_ipython().run_cell_magic('sql', '', '\nSELECT user_id, round(AVG(amount),1) as average_transaction_amount from transactions GROUP BY user_id\n')


# # 7 Assume there is a table products with columns product_id and price . Write an SQL query to retrieve the top 3 most expensive products.

# In[107]:


get_ipython().run_cell_magic('sql', '', '\nCREATE TABLE products1 (\nproduct_id INT PRIMARY KEY,\nprice DECIMAL(10, 2)\n);\n')


# In[108]:


get_ipython().run_cell_magic('sql', '', '\nINSERT INTO products1 (product_id, price) VALUES\n(1, 100),\n(2, 200),\n(3, 150),\n(4, 300),\n(5, 250);\n')


# In[110]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM products1\n')


# In[114]:


get_ipython().run_cell_magic('sql', '', '\nSELECT product_id, price from products1 ORDER BY price DESC LIMIT 3\n')


# # 8. Assume there are two tables, students and grades . Write an SQL query to retrieve the average grade for each student.

# In[115]:


get_ipython().run_cell_magic('sql', '', '\nCREATE TABLE students (\nstudent_id INT PRIMARY KEY,\nstudent_name VARCHAR(50),\naddress VARCHAR(100)\n);\n\nCREATE TABLE grades (\ngrade_id INT PRIMARY KEY,student_id INT,\ncourse_name VARCHAR(50),\ngrade DECIMAL(10, 2)\n);\n')


# In[116]:


get_ipython().run_cell_magic('sql', '', "\nINSERT INTO students (student_id, student_name, address) VALUES\n(1, 'John', '123 Main St'),\n(2, 'Jane', '456 Oak Ave'),\n(3, 'Mark', '789 Elm St');\n\nINSERT INTO grades (grade_id, student_id, course_name, grade) VALUES\n(1, 1, 'Math', 90),\n(2, 2, 'Math', 95),\n(3, 1, 'Science', 80),\n(4, 3, 'Math', 85),\n(5, 2, 'Science', 92),\n(6, 3, 'Science', 88);\n")


# In[117]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM students\n')


# In[118]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM grades\n')


# In[281]:


get_ipython().run_cell_magic('sql', '', '\nSELECT s.student_name, round(AVG(g.grade),1) as average_grade from students s\nJOIN grades g ON s.student_id = g.student_id\nGROUP BY student_name\n                       \n')


# # 9. Assume there are two tables, employees and salaries . Write an SQL query to retrieve all employees along with their corresponding salary.

# In[206]:


get_ipython().run_cell_magic('sql', '', '\nCREATE TABLE employees2 (\nemp_id INT PRIMARY KEY,\nemp_name VARCHAR(50),\nhire_date DATE\n);\n\nCREATE TABLE salaries2 (\nsalary_id INT PRIMARY KEY,\nemp_id INT,\nsalary DECIMAL(10, 2),\nstart_date DATE,\nend_date DATE\n);\n')


# In[207]:


get_ipython().run_cell_magic('sql', '', "\nINSERT INTO employees2 (emp_id, emp_name, hire_date) VALUES\n(1, 'John', '2020-01-01'),\n(2, 'Jane', '2020-02-01'),\n(3, 'Mark', '2020-03-01'),\n(4, 'Mike', '2020-04-01');\n\nINSERT INTO salaries2 (salary_id, emp_id, salary, start_date, end_date) VALUES\n(1, 1, 50000, '2020-01-01', '2020-12-31'),\n(2, 2, 60000, '2020-01-01', '2020-12-31'),\n(3, 1, 55000, '2021-01-01', '2021-12-31'),\n(4, 3, 65000, '2021-01-01', '2021-12-31'),\n(5, 2, 70000, '2021-01-01', '2021-12-31'),\n(6, 4, 75000, '2021-01-01', '2021-12-31');\n")


# In[209]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM employees2\n')


# In[211]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM salaries2\n')


# In[212]:


get_ipython().run_cell_magic('sql', '', '\nSELECT salary from salaries2\n')


# In[221]:


get_ipython().run_cell_magic('sql', '', 'SELECT * from employees2 as e\nJOIN salaries2 as s\nON e.emp_id =  s.emp_id\n')


# In[222]:


get_ipython().run_cell_magic('sql', '', '\n\nSELECT e.emp_name, s.salary from employees2 as e\nJOIN salaries2 as s\nON e.emp_id =  s.emp_id\n')


# # 10.  Assume there is a table orders with columns order_id , order_date , and total_price . Write an SQL query to retrieve the total sales for each month.

# In[241]:


get_ipython().run_cell_magic('sql', '', '\nCREATE TABLE orders4 (\norder_id INT PRIMARY KEY,\norder_date DATE,\ntotal_price DECIMAL(10, 2)\n);\n')


# In[242]:


get_ipython().run_cell_magic('sql', '', "\nINSERT INTO orders4 (order_id, order_date, total_price) VALUES\n(1, '2021-01-01', 100),\n(2, '2021-01-02', 200),\n(3, '2021-02-01', 150),\n(4, '2021-02-02', 300),\n(5, '2021-03-01', 250),\n(6, '2021-03-02', 350);\n")


# In[243]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM orders4\n')


# In[293]:


get_ipython().run_cell_magic('sql', '', '\nSELECT EXTRACT(MONTH from order_date) as months, SUM(total_price) as total_sales from orders4 GROUP BY months ORDER BY months;\n')


# In[ ]:




