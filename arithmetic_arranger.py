import re

def arithmetic_arranger(problems,showResult = -1):
  # Get problems, test length, throw error
  if len(problems) > 5:
    return 'Error: Too many problems.'
  
  for i in problems:
  # Test if data is OK else error
    matchSymbol = re.findall('.+\s(\+|\-)\s.', i)
    if matchSymbol:
      pass
    else:
      return "Error: Operator must be '+' or '-'."

    match = re.findall('^[0-9]+\s.\s[0-9]+$', i)
    if match:
      pass
    else:
      return 'Error: Numbers must only contain digits.'


    matchFourDigits = re.findall('^[0-9]{1,4}\s.\s[0-9]{1,4}$', i)
    print(matchFourDigits)
    if matchFourDigits:
      pass
    else:
      return 'Error: Numbers cannot be more than four digits.'
    

  # Count number of data

  # assign variable for each in lines and x&y

  # Foreach x&y, take the largest number, add 2 (space and symbol)
  # We now have width of each calcul

  # Line 1 = (maxlen+2  - len(x1)) of spaces concat with (if there is x2) 4 spaces then same for x2... concat with \n
  #Then line 2


 # return arranged_problems