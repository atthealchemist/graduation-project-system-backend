from pathlib import Path
from sphinx.cmd.quickstart import generate as sphinx_generate_docs
from sphinx.cmd.make_mode import run_make_mode as sphinx_make_docs

from modules.publishers import BasePublisher
from modules.utils import load_config, get_os


class SphinxPublisher(BasePublisher):

    def publish(self):
        # First, we're creating our docs path
        conf = load_config()
        os = get_os()

        docs_path = Path(conf['paths']['data'][os]) / conf['publish']['docs']['path']

        if not docs_path.exists() or not docs_path.is_dir():
            print("Creating docs path @ {}".format(docs_path))
            docs_path.mkdirs()

        # Then we're launching up our quickstart
        try:
            sphinx_generate_docs(self.params, overwrite=False, templatedir='_templates')
            published = True
        except Exception as ex:
            print("Sphinx generate docs error: {}".format(ex))
            published = False

        source_dir = Path(docs_path) / 'source'
        build_dir = Path(docs_path) / 'build'

        # Make docs
        result_code = sphinx_make_docs(['html', f"{source_dir}", f"{build_dir}"])

        print("Sphinx docs successfully published! (result code: {})".format(result_code))
        return published

    def __init__(self, params):
        super().__init__(params=params)

