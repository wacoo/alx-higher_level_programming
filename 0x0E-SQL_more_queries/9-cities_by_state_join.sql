-- List all the cities in hbtn_0d_usa database
-- cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.id ORDER BY cities.id ASC;
