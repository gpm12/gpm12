# COMP 340HW5
#Geraldy Paul Mentor
class token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


def tokenize(srcCode):
    tokSeq = []
    while srcCode != "":
        char = srcCode[0]
        if char=="+":
            newToken = token("PLUS", char)
            tokSeq.append(newToken)
        if char == "-":
            newToken = token("MINUS", char)
            tokSeq.append(newToken)
        elif char=="(":
            newToken = token("LPAREN", char)
            tokSeq.append(newToken)
        elif char == ")":
            newToken = token("RPAREN", char)
            tokSeq.append(newToken)
        elif char == "*":
            newToken = token("MULTIPLICATION", char)
            tokSeq.append(newToken)
        elif char == "/":
            newToken = token("DIVISION", char)
            tokSeq.append(newToken)
        elif char==" ":
            pass
        elif char>='0' and char<='9' :
            char = srcCode[0]
            numberStr=""
            while(char>='0' and char<='9'):
                srcCode = srcCode[1:]
                numberStr+=char
                char = srcCode[0]
            srcCode = char+srcCode
            newToken = token("NUMBER", numberStr)
            tokSeq.append(newToken)
        srcCode = srcCode[1:]
    return tokSeq
