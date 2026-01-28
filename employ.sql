-- Create Employees table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    joining_date DATE
);

-- Insert sample data
INSERT INTO employees VALUES (101, 'Ravi', 'IT', 50000, '2022-01-10');
INSERT INTO employees VALUES (102, 'Anu', 'HR', 40000, '2021-03-15');
INSERT INTO employees VALUES (103, 'Kiran', 'IT', 60000, '2020-07-20');
INSERT INTO employees VALUES (104, 'Sita', 'Finance', 55000, '2019-11-05');
INSERT INTO employees VALUES (105, 'Arjun', 'HR', 42000, '2023-02-12');

-- 1. Show all employees
SELECT * FROM employees;

-- 2. Employees from IT department
SELECT *
FROM employees
WHERE department = 'IT';

-- 3. Employees with salary > 45000
SELECT emp_name, salary
FROM employees
WHERE salary > 45000;

-- 4. Average salary by department
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

-- 5. Highest salary
SELECT MAX(salary) AS highest_salary
FROM employees;

-- 6. Sort employees by salary (high to low)
SELECT *
FROM employees
ORDER BY salary DESC;

-- 7. Count employees in each department
SELECT department, COUNT(*) AS total_employees
FROM employees
GROUP BY department;
