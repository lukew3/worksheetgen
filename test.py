from worksheetgen.wg import Worksheet
import requests, os
# Instantiates the worksheet object and titles it


ws = Worksheet(title='Example Worksheet')
# Adds an instruction segment with the given text to the worksheet
ws.add_instruction('Evaluate the following math problems')
# Adds the problem given to the worksheet
ws.add_problem('What is 9 + 10?')
ws.add_problem('What is the square root of 81?')
ws.add_problem('f(x)=9x-12', type='math')
# Export pdf to ws.pdf
ws.write_pdf()


def formula_as_file(formula, file):
    tfile = file
    r = requests.get('http://latex.codecogs.com/png.latex?\dpi{300} \huge %s' % formula)
    f = open(tfile, 'wb')
    f.write(r.content)
    f.close()

# formula_as_file( r'f(x)=2+x', 'output.png')
