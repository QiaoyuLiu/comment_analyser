from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datamodel as dm


def create_db():
    s = 'mysql+pymysql://{}:{}@{}:3306/{}'.format('root', 'root', 'localhost', 'nps')
    engine = create_engine(s)
    dm.Base.metadata.create_all(engine)


def get_session():
    s = 'mysql+pymysql://{}:{}@{}:3306/{}'.format('root', 'root', 'localhost', 'nps')
    engine = create_engine(s)
    DB_session = sessionmaker(bind=engine)
    session = DB_session()
    session.expire_on_commit = False
    return session


# insert a row in the dedicate table depends on the class name
def create_entity(entity):
    session = get_session()
    try:
        session.add(entity)
        session.commit()
    except Exception as e:
        session.rollback()
        print(str(e))
    finally:
        session.close()


# Get all comments witch has not been parsed (id greater than the current_id in properties.json)
def get_all_comments(current_id):
    session = get_session()
    try:
        res_list = session.query(dm.Comment).filter(dm.Comment.id > current_id).all()
        print(res_list)
        return res_list
    except Exception as e:
        session.rollback()
        print(str(e))
    finally:
        session.close()


# Get all entities with a weight greater than the value set in properties.json
def get_all_entities(weight):
    session = get_session()
    try:
        res_list = session.query(dm.Entity).filter(dm.Entity.weight > weight).all()
        return res_list
    except Exception as e:
        session.rollback()
        print(str(e))
    finally:
        session.close()


def get_negative_weight_entities():
    session = get_session()
    try:
        res_list = session.query(dm.Entity).filter(dm.Entity.weight < 0).all()
        return res_list
    except Exception as e:
        session.rollback()
        print(str(e))
    finally:
        session.close()
