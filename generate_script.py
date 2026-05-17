import abc
import datetime
import json
import markdown
import pathlib
import textwrap


class GenericMarkdown(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def transcripts_pattern(cls):
        raise NotImplemented()

    @classmethod
    @abc.abstractmethod
    def script(cls):
        raise NotImplemented()

    @classmethod
    def data(cls):
        data = {}
        for t in pathlib.Path("transcripts").glob(cls.transcripts_pattern()):
            data["https://" + "/".join(t.parts[1:]).removesuffix(".md")] = markdown.markdown(t.read_text())
        return data

    @classmethod
    def code(cls):
        code = pathlib.Path(cls.script()).read_text()
        return f'data["{cls.__name__}"] = {json.dumps(cls.data())};\n\n{code}\n'


class PennyArcade(GenericMarkdown):
    matches = ["https://www.penny-arcade.com/comic/*"]

    @classmethod
    def transcripts_pattern(cls):
        return "www.penny-arcade.com/comic/*/*/*/*"

    @classmethod
    def script(cls):
        return "www.penny-arcade.com.js"


class Xkcd:
    matches = ["https://www.xkcd.com/*", "https://xkcd.com/*"]

    @staticmethod
    def code():
        return pathlib.Path("www.xkcd.com.js").read_text()


class Collector:
    def __init__(self):
        self.matches = set()
        self.code = ""

    def collect(self, site):
        self.matches.update(site.matches)
        self.code += site.code()


    def match_block(self):
        return "\n".join([f"// @match       {m}" for m in self.matches])

def main():
    c = Collector()
    c.collect(PennyArcade)
    c.collect(Xkcd)

    print(textwrap.dedent(
        """
            // ==UserScript==
            // @name        aelevenymonkey
            // @namespace   Violentmonkey Scripts
        """).lstrip())

    print(c.match_block())

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")

    print(textwrap.dedent(
        f"""
            // @grant       none
            // @version     {timestamp}
            // @author      -
            // @description Tries to improve accessibility of specific websites
            // ==/UserScript==

            data = {{}};
        """).lstrip())

    print(c.code)


if __name__ == "__main__":
    main()
