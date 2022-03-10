import datetime
import sqlalchemy as sa
from db_session import ORMBase


class User(ORMBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer,
                           primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    about = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sa.Column(sa.String, nullable=True)
    created_date = sa.Column(sa.DateTime,
                                     default=datetime.datetime.now)