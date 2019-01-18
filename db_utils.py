from sqlalchemy.sql import text
from main import db, Environment

def drop_tables():
    db.drop_all()

def create_tables():
    db.create_all()


def create_counter_trigger():
    sql = """
    DROP TABLE IF EXISTS table_cnt;
    CREATE TABLE table_cnt (table_oid Oid PRIMARY KEY, count int);
    INSERT INTO table_cnt VALUES ('environment'::regclass, 0);
    """
    print(sql)
    db.engine.execute(text(sql))
    
    sql = """
    CREATE OR REPLACE FUNCTION count_increment() RETURNS TRIGGER AS $_$
    BEGIN
    UPDATE table_cnt SET count = count + 1 WHERE table_oid = TG_RELID;
    RETURN NEW;
    END $_$ LANGUAGE 'plpgsql';
    """
    print(sql)

    db.engine.execute(text(sql))

    sql = """
    DROP TRIGGER IF EXISTS increment_trigger ON environment;
    CREATE TRIGGER increment_trigger AFTER INSERT ON environment FOR EACH ROW EXECUTE PROCEDURE count_increment();
    """
    print(sql)

    db.engine.execute(text(sql))



def delete_environment_for_uuid(uuid):
    Environment.query.filter_by(uuid=uuid).delete()
    db.session.commit()