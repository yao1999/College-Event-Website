CREATE TABLE Universities_university(
    id INT PRIMARY KEY NOTNULL,
    name VARCHAR(100) NOTNULL,
    description TEXT NOTNULL,
    number_of_students INT NOT NULL,
    location_id INT NOTNULL,
    super_admin
);

CREATE TRIGGER UniversityChecker
    AFTER INNER ON Universities_locations
REFERENCING NEW AS NEW Universities_university
WHEN ((SELECT COUNT(*)  
    FROM RSO_rso_students M
    WHERE M.rso_id = NewMember.rso_id) > 4) 
FOR EACH ROW   
UPDATE RSOs    
SET Status = ‘active’    
WHERE RSO_ID = NewMember.RSO_ID