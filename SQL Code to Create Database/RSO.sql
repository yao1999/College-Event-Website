CREATE TABLE RSO_rso(
    id INT PRIMARY KEY NOTNULL,
    name VARCHAR(255) NOTNULL,
    description TEXT,
    total_students INT NOTNULL,
    admin_id INT NOTNULL,
    university_id INT NOTNULL,
);

CREATE TRIGGER RSOStatusUpdateA
    AFTER INNER ON RSO_rso_students
REFERENCING NEW AS NEW NewMember
WHEN ((SELECT COUNT(*)  
    FROM RSO_rso_students M
    WHERE M.rso_id = NewMember.rso_id) > 4) 
FOR EACH ROW   
UPDATE RSOs    
SET Status = ‘active’    
WHERE RSO_ID = NewMember.RSO_ID

CREATE TRIGGER RSOStatusUpdateP
    AFTER INNER ON RSO_rso_students
REFERENCING OLD AS ExMember
WHEN ((SELECT COUNT(*)  
    FROM RSO_rso_students M
    WHERE M.rso_id = ExMember.rso_id) > 4) 
FOR EACH ROW  
UPDATE RSOs    
SET Status = ‘INactive’    
WHERE RSO_ID = ExMember.RSO_ID


CREATE TRIGGER RSOStatusUpdateB
    AFTER INNER ON RSO_rso_students
REFERENCING NEW AS NEW NewMember
When((SELECT COUNT(*)  
    FROM RSO_rso M
    WHERE M.admin.university_id = NewMember.university_id) > 4)
FOR EACH ROW  
UPDATE RSO_rso     
SET Status = ‘active’    
WHERE rso_id = NewMember.rso_id

CREATE TRIGGER RSOStatusUpdateC
    AFTER INNER ON RSO_rso_students
REFERENCING OLD AS ExMember
When((SELECT COUNT(*)  
    FROM RSO_rso M
    WHERE M.admin.university_id = ExMember.university_id) > 4)
FOR EACH ROW  
UPDATE RSO_rso    
SET Status = ‘active’    
WHERE rso_id = ExMember.rso_id

