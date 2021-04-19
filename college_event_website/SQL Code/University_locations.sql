CREATE TABLE university_locations(
    id INT PRIMARY KEY NOTNULL,
    location_name VARCHAR(100) NOTNULL,
    latitude VARCHAR(100) NOTNULL,
    longitude VARCHAR(100) NOTNULL
);

INSERT INTO(
    id,	
    location_name,	
    latitude,	
    longitude
)
VALUES(
    1,	
    Orlando,	
    "28.6024",
    "-81.2001"
) 