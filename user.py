from models import  users_schema, User


def read_all():
    all_users = User.query.all()
    return users_schema.dump(all_users)

