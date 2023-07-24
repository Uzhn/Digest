import os

from dotenv import load_dotenv
from sqlalchemy import (Column, ForeignKey, Integer, String, Table,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

user_subscription_association = Table('user_subscription', Base.metadata,
                                      Column('user_id', Integer, ForeignKey('users.id')),
                                      Column('subscription_id', Integer,
                                             ForeignKey('subscriptions.id'))
                                      )

digest_post_association = Table(
    'digest_post_association', Base.metadata,
    Column('digest_id', Integer, ForeignKey('digests.id')),
    Column('post_id', Integer, ForeignKey('posts.id'))
)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    subscriptions = relationship('Subscription', secondary=user_subscription_association,
                                 back_populates='subscribers')
    digests = relationship('Digest', back_populates='user')

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"


class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer, primary_key=True)
    source_name = Column(String, nullable=False)

    subscribers = relationship('User', secondary=user_subscription_association,
                               back_populates='subscriptions')
    posts = relationship('Post', back_populates='subscription')

    def __repr__(self):
        return f"Subscription(id={self.id}, source_name='{self.source_name}')"


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'), nullable=False)

    subscription = relationship('Subscription', back_populates='posts')
    digests = relationship('Digest', secondary=digest_post_association, back_populates='posts')

    def __repr__(self):
        return f"Post(id={self.id}, content='{self.content}')"


class Digest(Base):
    __tablename__ = 'digests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='digests')
    posts = relationship('Post', secondary=digest_post_association, back_populates='digests')
