from uuid import UUID

from fastapi import APIRouter
from pony.orm.serialization import to_dict

from modules.core.database import DatabaseManager
from modules.models.space import Space
from modules.models.user import User
from modules.schemas.user import UserSchema, Role
from modules.utils import encrypt_password, generate_jwt_token, extract_entity

user = APIRouter()


@user.post('/create', tags=['user'])
def create_user(new_user: UserSchema):
    hashed, salt = encrypt_password(new_user.password)

    created_user = DatabaseManager.create(
        User,
        display_name=new_user.display_name,
        password_hash=hashed,
        password_salt=salt,
        login=new_user.login,
        token=generate_jwt_token(),
        role=Role.READ_WRITE.value,
    )

    DatabaseManager.create(
        Space,
        user=created_user.id
    )

    return dict(status='created', user_id=created_user.id, created_at=str(created_user.created_at))


@user.delete('/{user_uuid}', tags=['user'])
def delete_user(user_uuid: str):
    DatabaseManager.delete(
        User,
        user_uuid
    )
    return dict(status='deleted', user_id=user_uuid)


@user.patch('/{user_uuid}', tags=['user'])
def update_user(user_uuid: str, current_user: UserSchema):
    current_user_db = DatabaseManager.get(User, lambda u: u.id == UUID(user_uuid), as_entity=True)

    hashed = current_user_db.password_hash
    salt = current_user_db.password_salt

    if current_user.password:
        hashed, salt = encrypt_password(current_user.password)

    updated_user = DatabaseManager.update(
        User,
        user_uuid,
        login=current_user.login if current_user.login else current_user_db.login,
        display_name=current_user.display_name if current_user.display_name else current_user_db.display_name,
        password_hash=hashed,
        password_salt=salt
    )
    return dict(status='updated', user_id=updated_user.id)


@user.get('/{user_uuid}', tags=['user'])
def get_user(user_uuid: str):
    current_user = DatabaseManager.get(User, lambda u: u.id == UUID(user_uuid))
    current_user_extracted = extract_entity(current_user,
                                            exclude_fields=('password_hash', 'password_salt', 'role'))
    return dict(status='read_one', result=current_user_extracted)


@user.get('/', tags=['user'])
def list_users():
    users = DatabaseManager.all(User)
    users = [extract_entity(current_user, exclude_fields=('password_hash', 'password_salt', 'role'))
             for current_user in users]
    return dict(status='read_all', count=len(users), result=users)
