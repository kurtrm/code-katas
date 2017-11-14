SELECT Salesperson.Name
FROM Salesperson JOIN Orders
    ON Salesperson.ID = Orders.salesperson_id
GROUP BY Salesperson.Name
HAVING SUM(Orders.Amount) > 1300;