CREATE DATABASE MyDatabase; 
USE MyDatabase;
CREATE TABLE RawData (
	ID INT PRIMARY KEY,
	Name NVARCHAR(255),
	Amount DECIMAL(18, 2),
	DateOfBirth DATE
	);
INSERT INTO RawData (ID, Name, Amount, DateOfBirth)
VALUES
	(1, 'John Doe', 1500.50, '1980-05-15'),
	(2, 'Jane Smith', 2000.75, '1990-02-20'),
	(3, 'Bob', 5000.00, '1991-03-10'), 
	(4, 'Michel', 8000.00, '1999-11-11'), 
	(5, 'Zaya', 8500.00, '2000-06-10');

--let's assume we want to remove any rows with NULL values in the Name column 
DELETE FROM RawData WHERE Name IS NULL;

--Update the Amount column by doubling the values
UPDATE RawData SET Amount = Amount * 2;

--Add a new column to store the age based on the DateOfBirth 
ALTER TABLE RawData ADD Age INT;
UPDATE RawData SET Age = YEAR (GETDATE()) - YEAR (DateOfBirth);

﻿-- Ranking the data based on the Amount column (You can use the ROW NUMBER() window function for ranking)
SELECT ID, Name, Amount, DateOfBirth, Age,
ROW_NUMBER() OVER (ORDER BY Amount DESC) AS Rank INTO RankedData
FROM RawData;

--Display the ranked data 
SELECT * FROM RankedData;