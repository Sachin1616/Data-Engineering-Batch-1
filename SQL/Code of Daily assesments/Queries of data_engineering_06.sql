CREATE DATABASE Item;
USE Item;
CREATE TABLE Items (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    Amount INT
);
INSERT INTO Items (ID, Name, Amount)
VALUES
(1, 'ItemA', 100),
(2, 'ItemB', 75),
(3, 'ItemA', 50), 
(4, 'ItemB', 120), 
(5, 'ItemC', 90);

﻿--SUM
SELECT SUM(Amount) AS TotalAmount
FROM Items;

--COUNT
SELECT COUNT(*) AS TotalCount 
FROM Items;

--AVG
SELECT AVG(Amount) AS AverageAmount 
FROM Items;

﻿--GROUP BY
SELECT Name, COUNT(*) As TotalCount
FROM Items
GROUP BY Name;

--ROLL UP
SELECT Name,SUM(Amount) AS TotalAmount
FROM Items
GROUP BY ROLLUP (Name);

--MIN
SELECT MIN(Amount) AS MinAmount
From Items;

--MAX
SELECT MAX(Amount) AS MaxAmount
From Items;