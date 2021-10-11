from weasyprint import HTML
import os
import shutil
import random
import requests
from .write_prob import write_prob

class Problem:
    def __init__(self, question, answer='', type='', options=[], size_px=30):
        self.question = question
        self.answer = answer
        self.type = type
        self.options = options
        # The size_px is only for the latex images
        self.size_px = size_px
        if self.options != []:
            print(self.options)


class Worksheet:
    def __init__(self, title):
        self.title = title
        self.prob_list = []


    def write_pdf(self):
        # Make a working copy of the html template
        packagedir = str(__file__)[:-5]
        tempdir = packagedir + "temp/"
        if not os.path.exists(os.path.join(packagedir, "temp")) :
        	os.mkdir(tempdir)
        else :
        	pass

        workingFile = tempdir + 'working.html'
        shutil.copyfile(packagedir + 'base.html', workingFile)

        # Change Title
        with open(workingFile, "r") as file:
            lines = file.readlines()
            lines[67] = '<h1 id="title">' + self.title + '</h1>\n'
        with open(workingFile, "w") as file:
            file.writelines(lines)

        # get location of first line and copy lines before and after that
        with open(workingFile, "r") as file:
            lines = file.readlines()
            line = lines.index('    <div id="problems">\n')
            upper = lines[:line + 1]
            lower = lines[line:]

        # write file
        with open(workingFile, "w") as g:
            i = 1
            g.writelines(upper)
            for problemObj in self.prob_list:
                g.writelines(write_prob(problemObj, i))
                if problemObj.type != 'instruction':
                    i += 1
            g.writelines(lower)

        # export pdf
        HTML(workingFile).write_pdf('ws.pdf')

        # Remove temp directory
        shutil.rmtree(tempdir)

    def add_problem(self, problem, answer='', type='', options=[], size_px=30):
        newprob = Problem(problem, answer, type=type, options=options, size_px=size_px)
        self.prob_list.append(newprob)

    def add_problems_list(self, problems_list):
        for item in problems_list:
            if isinstance(item, list):
                question = item[0]
                answer = item[1]
                try:
                    type = item[2]
                    newprob = Problem(question, answer, type)
                except:
                    newprob = Problem(question, answer)
            else:
                newprob = Problem(item)
            self.prob_list.append(newprob)

    def add_instruction(self, instruction_text):
        newprob = Problem(instruction_text, '', type='instruction')
        self.prob_list.append(newprob)
