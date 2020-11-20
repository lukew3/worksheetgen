# worksheetgen
A worksheet generator

## Installation
You can install worksheetgen via pip:
`pip install worksheetgen`

## Basic Usage
```
from worksheetgen.wg import Worksheet

# Instantiates the worksheet object and titles it
ws = Worksheet(title='My Worksheet')
# Adds an instruction segment with the given text to the worksheet
ws.add_instruction('Evaluate the equations')
# Adds the problem given to the worksheet
ws.add_problem('What is 9 + 10?')
# Export pdf to ws.pdf
ws.write_pdf()
```

## Documentation
