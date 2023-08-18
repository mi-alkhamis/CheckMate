from datetime import datetime
from config import db, ma
from util import uuidgen
from marshmallow_sqlalchemy import fields


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.String(64), primary_key=True, default=uuidgen)
    username = db.Column(db.String(32), unique=True, index=True)
    email = db.Column(db.String(32), unique=True, index=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    tasks = db.relationship("Task",  # Calss_name
                            backref="User",  # User class, refers as back reference
                            cascade="all, delete, delete-orphan",
                            single_parent=True,
                            order_by="desc(Task.timestamp)"
                            )


class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.String(64), primary_key=True, default=uuidgen)
    user_id = db.Column(db.String(64), db.ForeignKey("User.id"))
    task_title = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow, onupdate=datetime.utcnow
    )

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        load_instance = True
        sqla_session = db.session
        include_fk = True   # to marshmallow recognise Foreign Key

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        include_relationships =True
    tasks = fields.Nested(TaskSchema, many=True) # to get nested fields from task tablle




user_schema = UserSchema()
users_schema = UserSchema(many=True)


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

