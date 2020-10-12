from modules.migrators.confluence import ConfluenceMigrator


class MigrationManager:

    migrators = dict(
        confluence=ConfluenceMigrator,
    )

    @classmethod
    def get_migrator(cls, name):
        return cls.migrators.get(name)
