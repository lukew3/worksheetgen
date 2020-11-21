# worksheetgen
A worksheet generator

## Installation
You can install worksheetgen via pip:
`pip install worksheetgen`

## Basic Usage
```
from worksheetgen.wg import Worksheet

# Instantiates the worksheet object and titles it
ws = Worksheet(title='Example Worksheet')
# Adds an instruction segment with the given text to the worksheet
ws.add_instruction('Evaluate the following math problems')
# Adds the problem given to the worksheet
ws.add_problem('What is 9 + 10?')
ws.add_problem('What is the square root of 9?')
ws.add_problem('f(x)=3x-4, f(2)=?', type='math')
# Export pdf to ws.pdf
ws.write_pdf()
```
This produces the following pdf:

![Image of output pdf](https://github.com/lukew3/worksheetgen/blob/main/ws.png)
## Documentation
