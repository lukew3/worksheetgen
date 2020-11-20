from worksheetgen.wg import Worksheet

# Instantiates the worksheet object and titles it
ws = Worksheet(title='Example Worksheet')
# Adds an instruction segment with the given text to the worksheet
ws.add_instruction('Evaluate the following math problems')
# Adds the problem given to the worksheet
ws.add_problem('What is 9 + 10?')
ws.add_problem('What is the square root of 9?')
# Export pdf to ws.pdf
ws.write_pdf()
