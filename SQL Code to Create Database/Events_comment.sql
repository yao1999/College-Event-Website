CREATE TABLE Events_comment(
    id INT PRIMARY KEY NOTNULL,
    content TEXT NOTNULL,
    rating INT NOTNULL,
    event_id INT NOTNULL,
    user_id INT NOTNULL,
    timestamp TIME NOTNULL
);