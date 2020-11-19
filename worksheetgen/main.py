from weasyprint import HTML
from shutil import copyfile
import os


def write_prob(probPair, i):
    newlines = [
    '<div class="problem" >\n',
    '    <p class="problem_text">' + str(i) + ') ' + probPair[0] + '</p>\n',
    '    <p class="problem_answerline">' + str(i) + ')______________</p>\n',
    '</div>\n'
    ]
    return newlines

def write_pdf(title, probAns_set):
    # Make a working copy of the html template
    packagedir = str(__file__)[:-7]
    workingFile = packagedir + 'working.html'
    copyfile(packagedir + 'base.html', workingFile)

    # Change Title
    with open(workingFile, "r") as file:
        lines = file.readlines()
        lines[11] = '<h1 id="title">' + title + '</h1>'
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
        for probPair in probAns_set:
            g.writelines(write_prob(probPair, i))
            i += 1
        g.writelines(lower)

    # export pdf
    HTML(workingFile).write_pdf('out.pdf')

    # Remove working copy
    os.remove(workingFile)
