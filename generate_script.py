import json
import markdown
import pathlib
import textwrap


class PennyArcade:
    matches = "https://www.penny-arcade.com/comic/*"

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

class Collector:
    def __init__(self):
        self.matches = set()
        self.code = ""

    def collect(self, site):
        self.matches.add(site.matches)
        self.code += site.code()


    def match_block(self):
        return "\n".join([f"// @match       {m}" for m in self.matches])

def main():
    c = Collector()
    c.collect(PennyArcade)

    print(textwrap.dedent(
        f"""
            // ==UserScript==
            // @name        Alevenymonkey
            // @namespace   Violentmonkey Scripts
            {c.match_block()}
            // @grant       none
            // @version     1.0
            // @author      -
            // @description 2/8/2025, 5:22:29 PM
            // ==/UserScript==
        """).lstrip())
    print(c.code)


if __name__ == "__main__":
    main()
