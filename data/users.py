import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    password_hash = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    creation_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_ordered = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    made_review = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    reviews = orm.relationship("Review", back_populates='user')
