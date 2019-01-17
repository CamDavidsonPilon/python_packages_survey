CREATE TABLE table_cnt (table_oid Oid PRIMARY KEY, count int);

CREATE FUNCTION count_increment() RETURNS TRIGGER AS $_$
BEGIN
UPDATE table_cnt SET count = count + 1 WHERE table_oid = TG_RELID;
RETURN NEW;
END $_$ LANGUAGE 'plpgsql';


CREATE TRIGGER increment_trigger AFTER INSERT ON environment FOR EACH ROW EXECUTE PROCEDURE count_increment();

INSERT INTO table_cnt VALUES ('environment'::regclass, 0);
