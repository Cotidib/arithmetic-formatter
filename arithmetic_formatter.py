def arithmetic_arranger(problems, displayed = False):
    allowed_operations = {"+": "+", "-":"-"}
    
    if len(problems)>5:
        print ("Error: Too many problems.")
        
    
    linea = ""
    linec = ""
    linedash = ""
    lineresult = ""
    
    for operation in problems:
        opsp = operation.split()
        a = opsp[0]
        b = opsp[1]
        c = opsp[2]

        if len(a)>4 or len(c)>4:
            print ("Error: Numbers cannot be more than four digits.")
            
            
        elif b not in allowed_operations:
            print ("Error: Operator must be '+' or '-'.")
            
            
        elif not a.isdigit() or not c.isdigit():
            print ("Error: Numbers must only contain digits.")
            
            
        else:
            result = eval(a + b + c,{"__builtins__": {}}, allowed_operations)

            maxvalue = max(len(str(a)),len(str(c)))
            dash = '-' * maxvalue + '--'

            aligna = " " * (len(dash) - len(a))
            alignc = " " * (len(dash) - len(c) - 1)
            alignresult = " " * (len(dash) - len(str(result)))

            linea += aligna + a + "    "
            linec += b + alignc + c + "    "
            linedash += dash + "    "
            lineresult += alignresult + str(result) + "    "
 
    if displayed == True:
        arrange = linea.rstrip() + "\n" + linec.rstrip() + "\n" + linedash.rstrip() + "\n" + lineresult.rstrip()
    elif displayed == False:
        arrange = linea.rstrip() + "\n" + linec.rstrip() + "\n" + linedash.rstrip()  
    
    arranged_problems = print(arrange)
            
    return arranged_problems

arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], True)
