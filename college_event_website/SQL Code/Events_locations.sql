CREATE TABLE Events_locations(
    id INT PRIMARY KEY NOTNULL,
    location_name VARCHAR(100) NOTNULL,
    latitude VARCHAR(100) NOTNULL,
    longitude VARCHAR(100) NOTNULL
    
);
INSERT INTO Events_locations(
    id,
    location_name,
    latitude,
    longitude
)
VALUES (
    9,	
    "Tampa",	
    "28.0587",	
    "-82.4139"
) 