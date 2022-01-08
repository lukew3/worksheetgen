import os
from pathlib import Path
from contextlib import contextmanager
from requests_file import FileAdapter
from requests_html import HTMLSession
import tempfile

import weasyprint
from domonic.html import *


class Element:
    def get_html_tag(self):
        raise NotImplementedError


class Problem(Element):
    def __init__(self, question, answer=None, number=None):
        self.question = question
        self.answer = answer
        if number is None:
            self._number = ""
        else:
            self._number = f"{number})"

    def get_html_tag(self):
        question_text = self._number + self.question
        answerline = self._number + "______________"
        return div(
            p(question_text, _class="problem_text"),
            p(answerline, _class="problem_answerline"),
            _class="problem"
        )


class Instruction(Element):
    def __init__(self, text):
        self.text = text

    def get_html_tag(self):
        return div(
            p(b(
                self.text
            )),
            _class="problem"
        )


class Whitespace(Element):
    def __init__(self, lines):
        self.lines = lines

    def get_html_tag(self):
        return div(
            *[br() for _ in range(self.lines)],
            _class="whitespace"
        )


class Section(Element):
    def __init__(self, children, name, description=None):
        self.children = children
        self.name = name
        self.description = description

    def get_html_tag(self):
        html_tag = div(_class="section")

        html_tag.append(
            center(h2(self.name))
        )

        if self.description:
            html_tag.append(h4(self.description))

        for child in self.children:
            html_tag.append(
                child.get_html_tag()
            )

        html_tag.append(hr())

        return html_tag


class Worksheet:
    def __init__(self, title):
        self.title = title
        self.prob_list = []

        # Temporary stack for sectioning, see method section() below.
        self._section_stack = []

    @property
    def number_of_problems(self):
        N = 0
        for elem in self.prob_list:
            if isinstance(elem, Problem):
                N += 1
        return N

    def _write_html(self):
        # Load the css style
        style_css_path = Path(__file__).parent.joinpath('style.css')
        with open(style_css_path) as f:
            style_css_string = "".join(f.readlines())

        # Create the root HTML and head
        doc = html(_lang="en", _dir="ltr")
        doc.append(
            head(
                meta(_charset="utf-8"),
                title(self.title),
                link(_href="https://fonts.gstatic.com", _rel="preconnect"),
                link(_href="https://fonts.googleapis.com/css2?family=Roboto&display=swap", _rel="stylesheet"),
                style(style_css_string),
                script(_type="text/javascript", _src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"),
                script(
                    '"MathJax.Hub.Config({'
                        'config: ["MMLorHTML.js"],'
                        'jax: ["input/TeX", "output/HTML-CSS", "output/NativeMML"],'
                        'extensions: ["tex2math.js", "tex2jax.js", MathMenu.js", "MathZoom.js"],'
                        '"HTML-CSS": { availableFonts: ["TeX"] }'
                    '});")',
                    _type="text/x-mathjax-config"
                )
            )
        )

        # Create the body tag
        body_tag = body(
            div(
                h1(self.title, _id="title"),
                h4("Name: ______________________", _id="name"),
                _id="header",
            ),
            hr()
        )

        # Create empty problems tag and
        # Iterate through list of elements
        problems_tag = div(_id="problems")
        for elem in self.prob_list:
            problems_tag.append(elem.get_html_tag())

        # Insert the tags respectively
        body_tag.append(problems_tag)
        doc.append(body_tag)

        return doc

    def write_pdf(self, outfile='ws.pdf'):
        doc = self._write_html()
        directory = Path(os.getcwd())

        # delete=False is to prevent errno 10054 on Windows,
        # see https://stackoverflow.com/questions/23212435 and
        # https://docs.python.org/3.9/library/tempfile.html#tempfile.NamedTemporaryFile
        with tempfile.NamedTemporaryFile(mode="w+", prefix='tmp_', suffix='.html',
                                         dir=directory, delete=False) as tmp:
            tmp.write(f"{doc}")

        with HTMLSession() as session:
            session.mount("file://", FileAdapter())
            site = session.get(f"file:///{Path(tmp.name).as_posix()}")
            site.html.render(timeout=15, keep_page=True)
            final_html = site.html.html

            # Release the file handle manually
            # This is to prevent errno 32 file in use
            site.raw.release_conn()

        # Delete the temporary file manually
        # Comment this line if you wish to not delete the HTML
        # for debugging purposes.
        Path(tmp.name).unlink()

        weasyprint.HTML(string = final_html).write_pdf(outfile)

    def add_problem(self, question, answer=None, whitespace_after=False):
        self.prob_list.append(Problem(question, answer, number=self.number_of_problems + 1))
        if whitespace_after:
            self.prob_list.append(Whitespace(lines=10))

    def add_whitespace(self, lines=10):
        self.prob_list.append(Whitespace(lines=lines))

    def add_instruction(self, instruction_text):
        self.prob_list.append(Instruction(instruction_text))

    @contextmanager
    def section(self, name, description=None):
        self._section_stack.append(self.prob_list.copy())
        self.prob_list = []

        yield

        section_children = self.prob_list.copy()
        self.prob_list = self._section_stack.pop()

        self.prob_list.append(Section(section_children, name=name, description=description))