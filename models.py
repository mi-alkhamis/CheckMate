from datetime import datetime
from config import db, ma
from util import uuidgen


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.String(64), primary_key=True, default=uuidgen)
    username = db.Column(db.String(32))
    email = db.Column(db.String(32), index=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session


user_schema = UserSchema()
users_schema = UserSchema(many=True)
