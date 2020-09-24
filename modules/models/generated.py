from datetime import datetime
from uuid import UUID, uuid4
from pony.orm import *


db = Database()


class Document(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    name = Required(str, 32)
    title = Required(str, 96)
    created_at = Required(datetime, default=lambda: datetime.now())
    updated_at = Required(datetime, default=lambda: datetime.now())
    slug = Required(str)
    url = Optional(str)
    short_url = Optional(str)
    contents = Required(buffer)
    author = Required('User')
    comments = Set('Comment')
    changes = Set('Change')
    assets = Set('Asset')
    links = Set('Link')
    references = Set('Reference')
    folders = Set('Folder')
    spaces = Set('Space')
    acceses = Set('Access')


class User(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    display_name = Optional(str)
    password_hash = Optional(str)
    password_salt = Optional(str)
    login = Optional(str, unique=True)
    token = Optional(str, unique=True)
    role = Optional(int, default=2)
    documents = Set(Document)
    comments = Set('Comment')
    changes = Set('Change')
    space = Optional('Space')
    acceses = Set('Access')
    created_at = Required(datetime, default=lambda: datetime.now())


class Comment(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    text = Required(str)
    created_at = Required(datetime)
    document = Required(Document)
    user = Required(User)


class Change(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    changed_at = Required(datetime)
    user = Required(User)
    content_diff = Required(str)
    document = Required(Document)


class Asset(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    name = Required(str)
    content = Required(buffer)
    documents = Set(Document)
    mime_type = Optional(str)


class Link(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    name = Required(str)
    url = Required(str)
    documents = Set(Document)


class Reference(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    document = Required(Document)
    created_at = Required(datetime, default=lambda: datetime.now())


class Folder(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    display_name = Optional(str)
    documents = Set(Document)
    parent_folders = Set('Folder', reverse='child_folders')
    child_folders = Set('Folder', reverse='parent_folders')
    spaces = Set('Space')


class Space(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    user = Required(User)
    documents = Set(Document)
    folders = Set(Folder)


class Access(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Required(User)
    type = Required(str)
    document = Required(Document)


