CREATE TABLE RSO_students(
    id INTEGER PRIMARY KEY NOTNULL,
    rso_id INTEGER NOTNULL,
    user_id INTEGER NOTNULL
);

INSERT INTO RSO_students(
    id,
    rso_id,
    user_id
)

VALUES(
    1,
    1,
    3
) 