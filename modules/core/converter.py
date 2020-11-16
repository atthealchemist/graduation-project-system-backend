from pypandoc import convert_text


class Converter:

    @staticmethod
    def convert(source_format, target_format, content):
        return convert_text(content, to=target_format, format=source_format)
