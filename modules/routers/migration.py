from typing import Optional

from fastapi import APIRouter

migration = APIRouter()


@migration.post('/{migrator}', tags=['migration'])
def migrate_from(migrator: str, confluence_url: str, pages_count: Optional[int] = 500):
    return dict(migrating=True, migrator=migrator)


@migration.get('/status', tags=['migration'])
def migration_status():
    migrators = [
        dict(migrator='confluence', status='migrating', docs_migrated=10, docs_total=2560)
    ]
    return dict(migrating=True, tasks=migrators)
