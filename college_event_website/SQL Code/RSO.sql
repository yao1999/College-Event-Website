CREATE TRIGGER RSOStatusUpdateA
    AFTER INSERT ON Students_RSOs  -- Event
REFERENCING NEW AS NewMember
WHEN ((SELECT COUNT(*)     
        FROM Students_RSOs M
        WHERE M.RSO_ID = NewMember.RSO_ID) > 4) 
FOR EACH ROW  --  Row-level trigger
    UPDATERSOs  --  Action    
        SET Status = ‘active’    
        WHERE RSO_ID = NewMember.RSO_ID
