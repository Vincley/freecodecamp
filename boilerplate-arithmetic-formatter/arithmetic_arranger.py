def arithmetic_arranger(problems, display = False):

    #If there are too many problems supplied to the function.
    if len(problems) > 5:
        return  "Error: Too many problems."

#Arithmetic Material (Operand, Operator, Formatter)
    top = ''
    bottom = ''
    dashes = ''
    result = ''
    arranged_problems = ''
    
    for x in problems:
        material = x.split()
        firstoperand = material[0]
        secondoperand = material[2]
        operator = material[1]

        #Each operand has a max of four digits.
        if len(firstoperand) > 4 or len(secondoperand) > 4:
            return "Error: Numbers cannot be more than four digits."
      
        #the function will accept only addition and subtraction.
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."
      
        #Each number (operand) should only contain digits.
        if firstoperand.isdigit() == False or secondoperand.isdigit() == False:
            return "Error: Numbers must only contain digits."

#Formatting Arithmetic Problems
        arrange = max(len(firstoperand), len(secondoperand))
        arranged = int(arrange)

        if operator == '+':
            solve = int(firstoperand) + int(secondoperand)
        else:
            solve = int(firstoperand) - int(secondoperand)
        
        if x != problems[-1]:
            top += firstoperand.rjust(arranged + 2) + "    "
            bottom += operator + secondoperand.rjust(arranged + 1) + "    "
            dashes += "-" * (arranged + 2) + "    "
            result += str(solve).rjust(arranged + 2) + "    "
        else:
            top += firstoperand.rjust(arranged + 2)
            bottom += operator + secondoperand.rjust(arranged + 1)
            dashes += "-" * (arranged + 2)
            result += str(solve).rjust(arranged + 2)
        

    if display == True:
        arranged_problems = str(top) + "\n" + str(bottom) + "\n" + dashes + "\n" + str(result)
    else :
        arranged_problems = str(top) + "\n" + str(bottom) + "\n" + dashes

    return arranged_problems