from weasyprint import HTML
from shutil import copyfile
import os

class Problem:
    def __init__(self, question, answer=''):
        self.question = question
        self.answer = answer


class Worksheet:
    def __init__(self, title):
        self.title = title
        self.prob_list = []


    def write_pdf(self):
        # Make a working copy of the html template
        packagedir = str(__file__)[:-5]
        workingFile = packagedir + 'working.html'
        copyfile(packagedir + 'base.html', workingFile)

        # Change Title
        with open(workingFile, "r") as file:
            lines = file.readlines()
            lines[11] = '<h1 id="title">' + self.title + '</h1>'
        with open(workingFile, "w") as file:
            file.writelines(lines)

        # get location of first line and copy lines before and after that
        with open(workingFile, "r") as file:
            lines = file.readlines()
            line = lines.index('    <div id="problems">\n')
            upper = lines[:line + 1]
            lower = lines[line:]

        # Define write_prob function
        def write_prob(problemObj, i):
            newlines = [
            '<div class="problem" >\n',
            '    <p class="problem_text">' + str(i) + ') ' + problemObj.question + '</p>\n',
            '    <p class="problem_answerline">' + str(i) + ')______________</p>\n',
            '</div>\n'
            ]
            return newlines

        # write file
        with open(workingFile, "w") as g:
            i = 1
            g.writelines(upper)
            for problemObj in self.prob_list:
                g.writelines(write_prob(problemObj, i))
                i += 1
            g.writelines(lower)

        # export pdf
        HTML(workingFile).write_pdf('ws.pdf')

        # Remove working copy
        os.remove(workingFile)

    def add_problem(self, problem, answer='', type=''):
        newprob = Problem(problem, answer)
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
