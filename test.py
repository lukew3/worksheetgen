from worksheetgen.wg import Worksheet
import requests, os
# Instantiates the worksheet object and titles it


# Instantiates the worksheet object and titles it
ws = Worksheet(title='Example Worksheet')
# Start section to the worksheet
ws.start_section('Section-1')
# Add problems
ws.add_problem('What is 9 + 10?')
ws.add_problem('What is the square root of 9?', whitespace=True)
ws.end_section()
ws.start_section(name='Section-2', description='This is section-2')
ws.add_problem('f(x)=3x-5, f(2)=?', type='math')
ws.add_whitespace()
ws.add_problem('f(x)=3x-5, f(2)=?', type='math', size_px=35)
#End section
ws.end_section()
#Add instructions
ws.add_instruction("That's for the Worksheet.")
# Export pdf to ws.pdf
ws.write_pdf()
