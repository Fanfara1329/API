import sqlalchemy as sa
from db_session import ORMBase
from sqlalchemy_serializer import SerializerMixin


class Job(ORMBase, SerializerMixin):
    __tablename__ = 'jobs'

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    team_leader = sa.Column(sa.Integer)
    job = sa.Column(sa.String)
    work_size = sa.Column(sa.Integer)
    collaborators = sa.Column(sa.String)
    is_finished = sa.Column(sa.Boolean)
