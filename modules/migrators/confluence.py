from email import message_from_bytes

from atlassian import Confluence

from .base import BaseMigrator


class ConfluenceMigrator(BaseMigrator):

    def confluence_spaces(self, **params):
        yield from self.confluence.get_all_spaces(**params)

    def confluence_pages(self, **params):
        yield from self.confluence.get_all_pages_from_space(**params)

    def convert_confluence_doc_to_html(self, source_doc, title=''):
        result = dict(
            title=title,
            content=''
        )
        source_bytes = message_from_bytes(source_doc)
        source_chunks = source_bytes.get_payload()
        if type(source_chunks) is not list:
            source_chunks = [source_bytes]
        for chunk in source_chunks:
            result['content'] += chunk.get_payload(decode=True)
        return result

    def migrate(self):

        result_pages = []

        for space in self.confluence_spaces():
            space_name = space.get('key')
            for page in self.confluence_pages(space=space_name):
                page_title = page.get('title')
                page_id = page.get('id')
                page_doc = self.confluence.get_page_as_word(page_id)
                page_html = self.convert_confluence_doc_to_html(page_doc, title=page_title)

                result_pages.append(page_html)

    def __init__(self, confluence_url='', confluence_username='', confluence_password=''):
        super().__init__(name="confluence")
        self.confluence = Confluence(
            url=confluence_url,
            username=confluence_username,
            password=confluence_password
        )

