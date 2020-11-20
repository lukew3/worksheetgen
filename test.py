from worksheetgen import wg
from mathgenerator import mathgen

title = 'Worksheet test'
set = [
    ['This is the first problem', 'firstans'],
    ['This is the second problem', 'secondans'],
    ['This is a really really really really really really really really really really really really really really really really long problem', 'hi'],
]
# main.write_pdf(title, set)
set = []
for i in range(100):
    set.append(mathgen.genById(0)[0])
myTest = wg.Worksheet(title='Basic Test')
myprob = '9+10'
myTest.add_problem(myprob)
myoptions = [
'France',
'Mexico',
'Egypt',
'China'
]
myTest.add_problem('Where is the Eiffel Tower located?', 'France', type='mc', options=myoptions)
myTest.add_instruction('For problems 3-100, evaluate the equation')
myTest.add_problem('this is a test')
myTest.add_problem('This is a really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really long problem', 'secondans')
myTest.add_problems_list(set)
myTest.write_pdf()
