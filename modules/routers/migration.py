import json
from pathlib import Path

from fastapi import APIRouter

from modules.database import DatabaseManager
from modules.migrators.manager import MigrationManager
from modules.models.generated import Document
from modules.schemas.migrator import MigratorSchema

migration = APIRouter()


@migration.get('/{migrator_name}/fields', tags=['migration'])
def publisher_fields(migrator_name: str):
    schema_path = Path() / 'modules' / 'migrators' / 'schemas' / f"{migrator_name}.json"
    if not schema_path.exists():
        return dict(status="error", description=f"Schema path {schema_path} does not exists!")
    schema_dict = json.loads(schema_path.read_text())

    return dict(status="converted", fields=schema_dict.get('fields'))


@migration.post('/', tags=['migration'])
def migrate_docs(new_migrator: MigratorSchema):
    current_migrator_cls = MigrationManager.get_migrator(new_migrator.migrator_name)
    current_migrator_instance = current_migrator_cls(params=new_migrator.params)
    docs = current_migrator_instance.migrate()

    for doc in docs:
        DatabaseManager.add(
            Document,
            title=doc.get('title'),
            content=doc.get('content')
        )

    return dict(status='migrated', count=len(docs))


@migration.get('/status', tags=['migration'])
def migration_status():
    migrators = [
        dict(migrator='confluence', status='migrating', docs_migrated=10, docs_total=2560)
    ]
    return dict(migrating=True, tasks=migrators)
