-- Create Database (MySQL users)
CREATE DATABASE srushti_akash_db;

-- Use database
USE srushti_akash_db;

-- Create Employees table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(40),
    salary INT,
    joining_date DATE
);

-- Insert records
INSERT INTO employees VALUES (101, 'Akash', 'IT', 35000, '2024-01-15');
INSERT INTO employees VALUES (102, 'Srushti', 'HR', 32000, '2024-02-10');
INSERT INTO employees VALUES (103, 'Ravi', 'Finance', 30000, '2023-12-05');
INSERT INTO employees VALUES (104, 'Anu', 'IT', 40000, '2023-11-20');

-- View all employees
SELECT * FROM employees;

-- Employees from IT department
SELECT * FROM employees
WHERE department = 'IT';

-- Salary greater than 33000
SELECT emp_name, salary
FROM employees
WHERE salary > 33000;

-- Update salary
UPDATE employees
SET salary = 45000
WHERE emp_id = 104;

-- Delete an employee
DELETE FROM employees
WHERE emp_id = 103;

-- Sort by salary (highest first)
SELECT * FROM employees
ORDER BY salary DESC;

-- Count employees per department
SELECT department, COUNT(*) AS total
FROM employees
GROUP BY department;
