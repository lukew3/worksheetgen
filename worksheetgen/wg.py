from weasyprint import HTML
import os
import shutil
import random
import requests
from pathlib import Path
from contextlib import contextmanager

from .write_prob import write_prob, write_whitespace


class Element:
    def get_html_tag(self):
        raise NotImplementedError


class Problem(Element):
    def __init__(self, question, answer=None):
        self.question = question
        self.answer = answer


class Instruction(Element):
    def __init__(self, text):
        self.text = text


class Whitespace(Element):
    def __init__(self, lines):
        self.lines = lines


class Section(Element):
    def __init__(self, children, name, description=None):
        self.children = children
        self.name = name
        self.description = description


class Worksheet:
    def __init__(self, title):
        self.title = title
        self.prob_list = []

        # Temporary stack for sectioning, see method section() below.
        self._section_stack = []

    def write_pdf(self):
        # Make a working copy of the html template
        packagedir = Path(__file__).parent
        tempdir = packagedir / "temp"
        tempdir.mkdir(exist_ok = True)
        workingFile = tempdir / "working.html"

        shutil.copyfile(packagedir / "base.html", workingFile)

        # Change Title
        with open(workingFile, "r") as file:
            lines = file.readlines()
            lines[67] = '<h1 id="title">' + self.title + "</h1>\n"
        with open(workingFile, "w") as file:
            file.writelines(lines)

        # get location of first line and copy lines before and after that
        with open(workingFile, "r") as file:
            lines = file.readlines()
            line = lines.index('    <div id="problems">\n')
            upper = lines[: line + 1]
            lower = lines[line:]

        # write file
        with open(workingFile, "w") as g:
            i = 1
            g.writelines(upper)
            for problemObj in self.prob_list:
                if type(problemObj) == type("str") :
                    g.writelines(problemObj)
                    continue
                g.writelines(write_prob(problemObj, i))
                if problemObj.type not in ["instruction", "whitespace"]:
                    i += 1
            g.writelines(lower)

        # export pdf
        HTML(workingFile).write_pdf("ws.pdf")

        # Remove temp directory
        shutil.rmtree(tempdir)

    def add_problem(self, question, answer=None, whitespace_after=False):
        self.prob_list.append(Problem(question, answer))
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