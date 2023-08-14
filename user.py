from flask import abort
from config import db
from models import user_schema, users_schema, User


def read_all():
    all_users = User.query.all()
    return users_schema.dump(all_users)


def create(user):
   username = user.get('username')
   existing_user = User.query.filter(User.username == username).one_or_none()

   if existing_user is None:
        new_user = user_schema.load(user ,session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
   else:
        abort(
            406, f"Username {username}  already exist."
        )

