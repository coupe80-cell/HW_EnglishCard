import configparser

import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from models import create_tables, MainDictionary


def create_db(engine):
    main_words = (
        ('Peace', 'Мир'),
        ('Dog', 'Собака'),
        ('Cat', 'Кот'),
        ('Bear', 'Медведь'),
        ('Wolf', 'Волк'),
        ('Giraffe', 'Жираф'),
        ('bird', 'Птица'),
        ('Chicken', 'Курица'),
        ('Mouse', 'Мыш'),
        ('Raccoon', 'Енот'),
    )

    create_tables(engine)

    session = (sessionmaker(bind=engine))()

    for row in main_words:
        session.add(MainDictionary(word=row[0], translate=row[1]))
    session.commit()
    session.close()


config = configparser.ConfigParser()
config.read('settings.ini')

engine = sq.create_engine(config['postgres']['DSN'])

create_db(engine)