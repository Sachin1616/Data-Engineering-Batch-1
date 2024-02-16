CREATE DATABASE coding_challenge_01;
USE coding_challenge_01;
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50),
    CourseID INT
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50)
);

INSERT INTO Students VALUES 
(1, 'Sachin', 101),
(2, 'Chaithu', 102),
(3, 'Jeevan', 103),
(4, 'Akash', 104);

INSERT INTO Courses VALUES 
(101, 'Math'),
(102, 'English'),
(103, 'Science'),
(104, 'History');

-- INNER JOIN
SELECT Students.StudentID, StudentName, CourseName
FROM Students
INNER JOIN Courses ON Students.CourseID = Courses.CourseID;

--LEFT JOIN
SELECT Students.StudentID, StudentName, CourseName
FROM Students
LEFT JOIN Courses ON Students.CourseID = Courses.CourseID;

-- RIGHT JOIN
SELECT Students.StudentID, StudentName, CourseName
FROM Students
RIGHT JOIN Courses ON Students.CourseID = Courses.CourseID;

--FULL JOIN
SELECT Students.StudentID, StudentName, CourseName
FROM Students
FULL OUTER JOIN Courses ON Students.CourseID = Courses.CourseID;

--CROSS JOIN
SELECT Students.StudentID, StudentName, Courses.CourseID, CourseName
FROM Students
CROSS JOIN Courses;

--SELF JOIN
SELECT s1.StudentName AS Student1, s2.StudentName AS Student2, c.CourseName
FROM Students s1
INNER JOIN Courses c ON s1.CourseID = c.CourseID
INNER JOIN Students s2 ON s1.StudentID <> s2.StudentID;





