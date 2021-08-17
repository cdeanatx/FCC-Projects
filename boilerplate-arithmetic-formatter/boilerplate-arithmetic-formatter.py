# Query: 
# ContextLines: 1

import re
def arithmetic_arranger(problems, show="false"):

  regbad = "[^\s\d+-/\*]"
  regoperator = "[+-/\*]"
  regoperand1 = "^\d+"
  regoperand2 = "\d+$"
  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""
  index = 0
  answerStr = ""

  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    bad = re.findall(regbad, problem)
    operand1 = re.findall(regoperand1, problem)
    operand2 = re.findall(regoperand2, problem)
    operator = re.findall(regoperator, problem)

    if bad:
      return 'Error: Numbers must only contain digits.'
    if operator[0] != '+' and operator[0] != '-':
      return "Error: Operator must be '+' or '-'."
    if len(operand1[0]) > 4 or len(operand2[0]) > 4:
      return 'Error: Numbers cannot be more than four digits.'
    
    if operator[0] == '+':
      answer = int(operand1[0]) + int(operand2[0])
    else: answer = int(operand1[0]) - int(operand2[0])

    if len(operand1[0]) > len(operand2[0]):
      operand2[0] = " " * (len(operand1[0]) - len(operand2[0]) + 1) + operand2[0]
      operand1[0] = " " * 2 + operand1[0]
    elif len(operand1[0]) < len(operand2[0]):
      operand1[0] = " " * (len(operand2[0]) - len(operand1[0]) + 2) + operand1[0]
      operand2[0] = " " + operand2[0]
    else:
      operand1[0] = " " * 2 + operand1[0]
      operand2[0] = " " + operand2[0]

    answerStr = " " * (len(operand1[0]) - len(str(answer))) + str(answer)
    #print(operand1[0] + "\n" + operator[0] + operand2[0])

    if index < len(problems) - 1:
      line1 = line1 + operand1[0] + " " * 4
      line2 = line2 + operator[0] + operand2[0] + " " * 4
      line3 = line3 + "-" * len(operand1[0]) + " " * 4
      line4 = line4 + answerStr + " " * 4
    elif index == len(problems) - 1:
      line1 = line1 + operand1[0]
      line2 = line2 + operator[0] + operand2[0]
      line3 = line3 + "-" * len(operand1[0])
      line4 = line4 + answerStr

    index += 1

  #print(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4)
  if show is True:
    return(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4)
  else: return(line1 + "\n" + line2 + "\n" + line3)
