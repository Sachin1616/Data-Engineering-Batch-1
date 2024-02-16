﻿CREATE DATABASE ExampleDB; 
GO
USE ExampleDB;
GO
CREATE TABLE Users (
	UserID INT PRIMARY KEY,
	UserName VARCHAR(50), 
	Age INT
	);
GO
INSERT INTO Users (UserID, UserName, Age) VALUES
(1, 'JohnDoe', 25),
(2, 'Janesmith', 30), 
(3, 'BobJohnson', 22);
﻿--Create a Stored Procedure 
CREATE PROCEDURE GetUserByID
	@UserID INT
AS
BEGIN
	SELECT * FROM Users WHERE UserID = @UserID;
END;
--Execute the Stored Procedure
EXEC GetUserByID @UserID = 2;