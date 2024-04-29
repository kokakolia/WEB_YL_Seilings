import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Review(SqlAlchemyBase):
    __tablename__ = 'reviews'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    text = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    rating = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    img = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = orm.relationship('User')
