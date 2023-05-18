--select cities
SELECT id, name FROM states
WHERE state_id = 1
GROUP BY id;
