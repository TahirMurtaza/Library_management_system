from uuid import UUID

from .serializer import CustomSerializerMixin
from ..extensions import db

class Members(db.Model,CustomSerializerMixin):
    __tablename__ = "members"
    serialize_only = ('Id', 'name', 'to_pay')
    Id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    to_pay = db.Column(db.Integer, nullable=False)
    
    def get_all():
        list = []
        items = Members.query.all()
        for item in items:
            list.append(item.to_dict())
        return list