import os, requests

def formula_as_file(formula, file):
    tfile = file
    r = requests.get('http://latex.codecogs.com/png.latex?\dpi{300} \huge %s' % formula)
    f = open(tfile, 'wb')
    f.write(r.content)
    f.close()

def write_problem(obj, probNum):
    newlines = [
    '<div class="problem" >\n',
    '    <p class="problem_text">' + str(probNum) + ') ' + obj.question + '</p>\n',
    '    <p class="problem_answerline">' + str(probNum) + ')______________</p>\n',
    '</div>\n'
    ]
    return newlines

def write_instructions(obj):
    newlines = [
    '<div class="problem" >\n',
    '    <p class="problem_text"><b>' + obj.question + '</b></p>\n',
    '</div>\n'
    ]
    return newlines

def write_multiple_choice(obj, probNum):
    option_list = obj.options
    # Shuffle list
    random.shuffle(option_list)
    answer_index = option_list.index(obj.answer)
    obj.answer = chr(answer_index + 65)

    newlines = [
    '<div class="problem" >\n',
    '    <p class="problem_answerline">' + str(probNum) + ')______________</p>\n',
    '    <p class="problem_text">' + str(probNum) + ') ' + obj.question + '</p>\n',
    '    <ul>\n',
    '       <li class="mc_option">A) ' + option_list[0] + '</li>'
    '       <li class="mc_option">B) ' + option_list[1] + '</li>'
    '       <li class="mc_option">C) ' + option_list[2] + '</li>'
    '       <li class="mc_option">D) ' + option_list[3] + '</li>'
    '    </ul>\n'
    '</div>\n'
    ]
    return newlines

def write_math(obj, probNum):
    #might need to loop a search for latex in case more than one use of latex is desired
    #find latex and store it as a string without markers
    latex_string = obj.question
    size = obj.size_px
    renderNum = 0
    new = False
    while new == False:
        out_file = str(__file__)[:-13] + 'temp/out' + str(renderNum) + '.png'
        if os.path.exists(out_file):
            renderNum +=1
        else:
            new = True
    formula_as_file(latex_string, out_file)
    newlines = [
    '<div class="problem" >\n',
    '    <p class="problem_answerline">' + str(probNum) + ')______________</p>\n',
    '    <div class="flex-parent">\n',
    '       <p class="problem_text">' + str(probNum) + ')</p>\n',
    '       <img src="out' + str(renderNum) + f'.png" class="math_image" style="height:{size}px">\n',
    '    </div>\n',
    '</div>\n'
    ]
    return newlines

def write_prob(problemObj, i):
    if problemObj.type == '':
        return write_problem(problemObj, i)
    elif problemObj.type == 'instruction':
        return write_instructions(problemObj)
    elif problemObj.type == 'mc':
        return write_multiple_choice(problemObj, i)
    elif problemObj.type == 'math':
        return write_math(problemObj, i)
