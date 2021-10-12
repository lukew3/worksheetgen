from worksheetgen.wg import Worksheet
import requests, os
# Instantiates the worksheet object and titles it


# Instantiates the worksheet object and titles it
ws = Worksheet(title='Example Worksheet')
# Adds an instruction segment with the given text to the worksheet
ws.add_instruction('Evaluate the following math problems')
# Adds the problem given to the worksheet
ws.add_problem('What is 9 + 10?')
ws.add_problem('What is the square root of 9?', whitespace=True)
ws.add_problem('f(x)=3x-5, f(2)=?', type='math')
ws.add_whitespace()
ws.add_problem('f(x)=3x-5, f(2)=?', type='math', size_px=35)
# Export pdf to ws.pdf
ws.write_pdf()
