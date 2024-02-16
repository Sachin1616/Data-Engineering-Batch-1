CREATE DATABASE coding_challenge01;
USE coding_challenge01;
CREATE TABLE Sales 
(
    SaleID INT PRIMARY KEY,
    ProductID INT,
    SaleDate DATE,
    Quantity INT,
    Amount DECIMAL(10, 2)
);
INSERT INTO Sales VALUES
(1, 101, '2024-01-01', 10, 70.00),
(2, 102, '2024-01-01', 5, 50.00),
(3, 101, '2024-01-02', 8, 80.00),
(4, 102, '2024-01-02', 12, 130.00),
(5, 101, '2024-01-03', 15, 150.00),
(6, 102, '2024-01-03', 7, 90.00);

--OVER and PARTITION BY clause
SELECT SaleID, ProductID, SaleDate, Quantity, Amount,
SUM(Quantity) OVER (PARTITION BY ProductID, SaleDate) AS TotalQuantityPerProductDate, -- Calculate the sum of Quantity for each ProductID over the SaleDate partition
SUM(Amount) OVER (PARTITION BY SaleDate) AS TotalAmountPerDate -- Calculate the total amount for each SaleDate partition
FROM Sales;

--
-- Query with SUBTOTALS and TOTAL AGGRETATIONS.
SELECT ProductID, SaleDate, Quantity, Amount,
SUM(Quantity) OVER (PARTITION BY ProductID, SaleDate) AS SubtotalQuantity, -- Calculate the subtotal of Quantity for each ProductID and SaleDate
SUM(Quantity) OVER (PARTITION BY SaleDate) AS TotalQuantity,     -- Calculate the total Quantity for each SaleDate
SUM(Amount) OVER (PARTITION BY ProductID, SaleDate) AS SubtotalAmount,  -- Calculate the subtotal of Amount for each ProductID and SaleDate
SUM(Amount) OVER (PARTITION BY SaleDate) AS TotalAmount  -- Calculate the total Amount for each SaleDate
FROM Sales;
