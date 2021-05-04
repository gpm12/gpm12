# COMP 340HW5
#Geraldy Paul Mentor
import lexer
import parserr
import evaluator
while True:
    srcCode = input(">>> ")
    if srcCode == "poopoo":
        break
    tokSeq = lexer.tokenize(" "+srcCode+ " ")
    rootNode = parserr.parse(tokSeq)
    result = evaluator.evaluate(rootNode)
    print("The result is: ", result)
print("Now it is time to go poo poo.")