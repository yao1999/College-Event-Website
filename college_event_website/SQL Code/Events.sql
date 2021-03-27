CREATE TRIGGER Event_check
    AFTER INNER ON  Event_event
REFERENCING NEW AS NEW Event
WHEN ((SELECT COUNT(*)  
    FROM Event M
    WHERE M.start_time = NewEvent.start_time
    WHERE M.endt_time = NewEvent.end_time
    WHERE M.location_id = NewEvent.location_id
    ))


CREATE TRIGGER Event_admin_checker
    AFTER INNER ON Event
REFERENCING NEW AS NEW Event
WHEN ((SELECT COUNT(*)
    FROM Users M
    WHERE M.rso_id = NewEvent.admin_id.rso_id
    ))
FOR EACH ROW
UPDATE Event

INSERT INTO Event_event (
    id,
    name,
    description,
    date,
    start_time,
    end_time,
    phone,
    email,
    is_public,
    is_privateL,
    is_RSO,
    admin_id,
    is_approved,
    location_iD,
    university_id,
    category)

VALUES(
    1,
    "Database event"
    "For Database"
    "2021-04-14"
    "12:00:00"
    "15:00:00"
    "1231231231"
    "test@gmail.com”	
    1	
    0	
    0	
    NULL	
    1	
    1	
    NULL	
    “School”
)