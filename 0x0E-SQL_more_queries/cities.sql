-- List all the cities in california found in the database hbtn_0d_2
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
);
