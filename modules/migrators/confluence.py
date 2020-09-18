from string import Template

from .base import BaseMigrator


class ConfluenceMigrator(BaseMigrator):

    def migrate(self):
        url_template = Template("https://$server/rest/api/content?limit=500&start=0")

        # client.get(url_template.safe_substitute(
        #   modules=self.confluence_url
        # ))

    def __init__(self, confluence_url):
        super().__init__(name="confluence")
        self.confluence_url = confluence_url

