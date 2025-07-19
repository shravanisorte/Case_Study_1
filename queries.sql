--Top 3 Parking Zones by Revenue
SELECT zone_name, SUM(paid_amount) AS revenue
FROM parking_data
GROUP BY zone_name
ORDER BY revenue DESC
LIMIT 3;

--Most Frequent Parkers
SELECT vehicle_id, COUNT(*) AS visits
FROM parking_data
GROUP BY vehicle_id
ORDER BY visits DESC;

CREATE VIEW vehicle_summary AS
SELECT vehicle_id, owner_name, COUNT(*) AS total_visits, SUM(paid_amount) AS total_paid
FROM parking_data
GROUP BY vehicle_id, owner_name;

SELECT * FROM vehicle_summary;

BEGIN TRANSACTION;
CREATE TABLE account_balance (
    user_id INTEGER,
    balance DOUBLE
);
INSERT INTO account_balance VALUES (1, 100);
UPDATE account_balance SET balance = balance - 10 WHERE user_id = 1;
SELECT * FROM account_balance;
ROLLBACK;


