CREATE DATABASE Collections;
USE Collections;
CREATE TABLE students (
    ROLL_NO INT,
    NAME VARCHAR(255),
    ADDRESS VARCHAR(255),
    PHONE VARCHAR(10),
    AGE INT
);
INSERT INTO students (ROLL_NO, NAME, ADDRESS, PHONE, AGE)
VALUES
    (1, 'Shubham Kumar', '123 Main Street, Bangalore', '9876543210', 23),
    (2, 'Shreya Gupta', '456 Park Road, Mumbai', '9876543211', 23),
    (3, 'Naveen Singh', '789 Market Lane, Delhi', '9876543212', 26), 
    (4, 'Aman Chopra', '246 Forest Avenue, Kolkata', '9876543213', 22), 
    (5, 'Aditya Patel', '7898 Ocean Drive, Chennai', '9876543214', 27), 
    (6, 'Avdeep Desai', '34 River View, Hyderabad', '9876543215', 24); 

SELECT * FROM students;

SELECT DISTINCT NAME FROM students;

SELECT COUNT(DISTINCT ROLL_NO) FROM students;