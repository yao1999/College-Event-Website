SELECT DISTINCT*FROM 'Events_event' e 
    WHERE e.is_public = 1


SELECT DISTINCT*FROM 'Events_event' e, 'Users_user' m
    WHERE e.is_private = 1 And m.university_id = e.university_id


SELECT DISTINCT*FROM 'Events_event' e, 'Users_rsonumber' u 'Users_user' m
    WHERE e.is_RSO = 1 And u.rso_id = e.rso_id AND m.username = u.username

