from flask import abort, make_response
from config import db
from models import user_schema, users_schema, User


def read_all():
    all_users = User.query.all()
    return users_schema.dump(all_users)



def read_one(username):
    user = User.query.filter(User.username == username).one_or_none()
    if user is not None:
        return user_schema.dump(user)
    else:
        abort(
            404, f"The {username} does not exist."
        )


def create(user):
    username = user.get('username')
    existing_user = User.query.filter(User.username == username).one_or_none()

    if existing_user is None:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(
            406, f"Username {username}  already exist."
        )


def update_one(username, user):

    existing_user = User.query.filter(User.username == username).one_or_none()
    if existing_user:
        update_user = user_schema.load(user, session=db.session)
        existing_user.first_name = update_user.first_name
        existing_user.last_name = update_user.last_name
        existing_user.email = update_user.email
        db.session.merge(existing_user)
        db.session.commit()
        return user_schema.dump(existing_user), 201
    else:
        abort(
            404, f"The {username} does not exist."
        )


def delete_one(username):
    existing_user = User.query.filter(User.username == username).one_or_none()

    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()
        return make_response(f"The Username {username} successfully deleted", 200)
    else:
        abort(
            404, f"The {username} does not exist."
        )
