from hmac import compare_digest

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse

from modules.models.managers.user import UserManager
from modules.schemas.auth import RegisterUserSchema, OAuthUserSchema
from modules.schemas.user import UserSchema, Role
from modules.security import logged_in_as_user
from modules.utils import encrypt_password

auth = APIRouter()


@auth.get('/current', tags=['auth'])
def authenticated_user(current_user: UserSchema = Depends(logged_in_as_user)):
    return current_user


# @auth.get('/admin-test', tags=['auth'])
# def authenticated_admin(current_admin=Depends(logged_in_as_user)):
#     u = UserManager.get_by_login(current_admin['login'])
#     if Role.is_admin(u):
#         return dict(for_admin_only=42)
#     raise HTTPException(status_code=401, detail="Insufficient permissions!")


@auth.post('/register', tags=['auth'])
def register(user: RegisterUserSchema):
    status = UserManager.create_if_not_exists(
        display_name=user.display_name,
        login=user.login,
        password=user.password
    )
    if not status:
        raise HTTPException(status_code=400, detail="User already exists!")
    return dict(created=status)


@auth.post('/login', tags=['auth'])
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    client_id = form_data.client_id
    display_name = form_data.client_secret
    status = 'logged_in'
    if not UserManager.get_by_login(form_data.username):
        if 'google' in client_id:
            UserManager.create_if_not_exists(form_data.username, form_data.password, display_name)
            status = 'registered'
        else:
            raise HTTPException(status_code=400, detail="Incorrect username or password")

    user = UserManager.get_by_login(form_data.username)
    user_hash = user.password_hash
    user_salt = user.password_salt

    suggested_hash, suggested_salt = encrypt_password(form_data.password, user_salt)
    correct_hash = compare_digest(suggested_hash, user_hash)
    if not correct_hash:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    user_extracted = UserManager.as_dict(user, exclude_fields=('password_hash', 'password_salt', 'role'))
    return dict(status=status, access_token=user_extracted.get('token'), token_type='bearer')


@auth.post('/oauth', tags=['auth'])
def login_oauth(user: OAuthUserSchema):
    status = UserManager.create_if_not_exists(user)
    if not status:
        raise HTTPException(status_code=400, detail="User already exists!")
    return dict(created=status)
