CREATE TABLE Event_comment(
    id INT PRIMARY KEY NOTNULL,
    content TEXT NOTNULL,
    rating INT NOTNULL,
    event_id INT NOTNULL,
    user_id INT NOTNULL,
    timestamp TIME NOTNULL
);

INSERT INTO Event_comment(
    id,	
    content,	
    rating,	
    event_id,	
    user_id,	
    timestamp
)
VALUES (
    10,	
    "you guys are right, this event is not bad",	
    5,	
    1,	
    11,	
    "2021-04-16 00:00:06"
)