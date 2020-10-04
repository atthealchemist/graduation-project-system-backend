from modules.publishers.sphinx import SphinxPublisher


class PublishManager:

    publishers = dict(
        sphinx=SphinxPublisher,
    )

    @classmethod
    def get_publisher(cls, name):
        return cls.publishers.get(name)
