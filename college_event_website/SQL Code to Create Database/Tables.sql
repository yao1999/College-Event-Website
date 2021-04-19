CREATE DATABASE sqldatabase;

CREATE TABLE Users_user (
    id INT PRIMARY KEY NOTNULL,
    password VARCHAR(128) NOTNULL,
    last_login DATATIME,
    is_superuser BOOL NOTNULL,
    username VARCHAR(150) NOTNULL,
    first_name VARCHar(150) NOTNULL,
    last_name VARCHAR(150) NOTNULL,
    email VARCHAR(254) NOTNULL,
    is_staff BOOL NOTNULL,
    is_active BOOL NOTNULL,
    data_joined DATETIME,
    is_admin BOOL NOTNULL,
    is_super_admin BOOL NOTNULL,
    university_id INT
);

CREATE TABLE Users_rsonumber(
    id INT PRIMARY KEY NOTNULL,
    username VARCHAR(100) NOTNULL,
    rso INT NOT NULL
);

CREATE TABLE Universities_university(
    id INT PRIMARY KEY NOTNULL,
    name VARCHAR(100) NOTNULL,
    description TEXT NOTNULL,
    number_of_students INT NOT NULL,
    location_id INT NOTNULL,
    super_admin
);

CREATE TABLE Universities_locations(
    id INT PRIMARY KEY NOTNULL,
    location_name VARCHAR(100) NOTNULL,
    latitude VARCHAR(100) NOTNULL,
    longitude VARCHAR(100) NOTNULL
);

CREATE TABLE Universities_photos(
    id INT PRIMARY KEY NOTNULL,
    university_name VARCHAR(100) NOTNULL,
    photo_path VARCHAR(100) NOTNULL
);

CREATE TABLE Universities_pictures(
    id INT PRIMARY KEY NOTNULL,
    university_id INT NOTNULL,
    photo_id INT NOTNULL
);

CREATE TABLE RSO_rso(
    id INT PRIMARY KEY NOTNULL,
    name VARCHAR(255) NOTNULL,
    description TEXT,
    total_students INT NOTNULL,
    admin_id INT NOTNULL,
    university_id INT NOTNULL,
);

CREATE TABLE RSO_rso_students(
    id INTEGER PRIMARY KEY NOTNULL,
    rso_id INTEGER NOTNULL,
    user_id INTEGER NOTNULL
);

CREATE TABLE Events_event(
    id INT PRIMARY KEY NOTNULL,
    name VARCHAR(150) NOTNULL,
    description TEXT NOTNULL,
    date DATE NOTNULL,
    start_time TIME NOTNULL,
    end_time TIME NOTNULL,
    phone VARCHAR(31) NOTNULL,
    email VARCHAR(254) NOTNULL,
    is_public BOOL NOTNULL,
    is_private BOOL NOTNULL,
    is_RSO BOOL NOTNULL,
    user_id INT,
    is_approved BOOL NOTNULL,
    location_id INT,
    university_id INT,
    category VARCHAR(150)
    rso_id
);

CREATE TABLE Events_comment(
    id INT PRIMARY KEY NOTNULL,
    content TEXT NOTNULL,
    rating INT NOTNULL,
    event_id INT NOTNULL,
    user_id INT NOTNULL,
    timestamp TIME NOTNULL
);

CREATE TABLE Events_locations(
    id INT PRIMARY KEY NOTNULL,
    location_name VARCHAR(100) NOTNULL,
    latitude VARCHAR(100) NOTNULL,
    longitude VARCHAR(100) NOTNULL
    
);

CREATE TRIGGER Event_check
    AFTER INNER ON  Events_event
REFERENCING NEW AS NEW Events_event
WHEN ((SELECT COUNT(*)  
    FROM Events_event M
    WHERE M.start_time = NewEvent.start_time
    WHERE M.endt_time = NewEvent.end_time
    WHERE M.location_id = NewEvent.location_id
    ))

CREATE TRIGGER Event_admin_checker
    AFTER INNER ON Events_event
REFERENCING NEW AS NEW Events_event
WHEN ((SELECT COUNT(*)
    FROM Users_user M
    WHERE M.rso_id = NewEvent.admin_id.rso_id
    ))
FOR EACH ROW
UPDATE Events_event

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