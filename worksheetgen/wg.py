from weasyprint import HTML
from shutil import copyfile
import os
import random

class Problem:
    def __init__(self, question, answer='', type='', options=[]):
        self.question = question
        self.answer = answer
        self.type = type
        self.options = options
        if self.options != []:
            print(self.options)


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
            lines[67] = '<h1 id="title">' + self.title + '</h1>\n'
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
            if problemObj.type == '':
                newlines = [
                '<div class="problem" >\n',
                '    <p class="problem_text">' + str(i) + ') ' + problemObj.question + '</p>\n',
                '    <p class="problem_answerline">' + str(i) + ')______________</p>\n',
                '</div>\n'
                ]
            elif problemObj.type == 'instruction':
                newlines = [
                '<div class="problem" >\n',
                '    <p class="problem_text"><b>' + problemObj.question + '</b></p>\n',
                '</div>\n'
                ]
            elif problemObj.type == 'mc':
                option_list = problemObj.options
                # Shuffle list
                random.shuffle(option_list)
                answer_index = option_list.index(problemObj.answer)
                problemObj.answer = chr(answer_index + 65)

                newlines = [
                '<div class="problem" >\n',
                '    <p class="problem_answerline">' + str(i) + ')______________</p>\n',
                '    <p class="problem_text">' + str(i) + ') ' + problemObj.question + '</p>\n',
                '    <ul>\n',
                '       <li class="mc_option">A) ' + option_list[0] + '</li>'
                '       <li class="mc_option">B) ' + option_list[1] + '</li>'
                '       <li class="mc_option">C) ' + option_list[2] + '</li>'
                '       <li class="mc_option">D) ' + option_list[3] + '</li>'
                '    </ul>\n'
                '</div>\n'
                ]
            return newlines

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

        # Remove working copy
        # os.remove(workingFile)

    def add_problem(self, problem, answer='', type='', options=[]):
        newprob = Problem(problem, answer, type=type, options=options)
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
