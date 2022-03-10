from flask import Blueprint, jsonify
from data import db_session
from data.models import Job

jobs_api = Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@jobs_api.route('/api/jobs')
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Job).all()
    return jsonify(
        {
            'jobs':
                [x.to_dict() for x in jobs]
        }
    )