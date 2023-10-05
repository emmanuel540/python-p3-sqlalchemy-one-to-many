#!/usr/bin/env python3


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Base, Game, Review

engine = create_engine('sqlite:///one_to_many.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

fake = Faker()


game = Game(title=fake.catch_phrase(), genre=fake.word(), platform=fake.word(), price=fake.random_int(min=20, max=60))
session.add(game)
session.commit()


review = Review(score=fake.random_int(min=1, max=10), comment=fake.sentence(), game=game)
session.add(review)
session.commit()

