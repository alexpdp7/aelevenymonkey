import datetime
import json
import markdown
import pathlib
import textwrap


class PennyArcade:
    matches = ["https://www.penny-arcade.com/comic/*"]

    @staticmethod
    def data():
        data = {}
        for t in pathlib.Path("transcripts").glob("www.penny-arcade.com/comic/*/*/*/*"):
            data["https://" + "/".join(t.parts[1:]).removesuffix(".md")] = markdown.markdown(t.read_text())
        return data

    @staticmethod
    def code():
        code = pathlib.Path("www.penny-arcade.com.js").read_text()
        return f"penny_arcade_data = {json.dumps(PennyArcade.data())};\n\n{code}\n"


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
            // @name        Alevenymonkey
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
        """).lstrip())

    print(c.code)


if __name__ == "__main__":
    main()
