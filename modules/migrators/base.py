
class BaseMigrator:

    def migrate(self):
        pass

    def __init__(self, name):
        self.migrator_name = name
