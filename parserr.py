import lexer

class treeNode:
      def __init__(self,type,value,precedence):
            self.type = type
            self.value = value
            self.precedence = precedence
      parent = None
      lChild = None
      rChild = None
def getPrecedence(type):
      precedence = 0
      if type == "PLUS" or type == "MINUS":
            precedence = 1
      elif type == "MULTIPLICATION" or type == "DIVISION":
            precedence = 2
      return precedence

def createTreeNodeList(tokSeq):
      treeNodeList = []
      x=0
      newSeq = replaceUnary(tokSeq)
      while len(tokSeq) != len(newSeq):
          tokSeq = newSeq
          newSeq = replaceUnary(tokSeq)
      for token in tokSeq:
          if (token.type == "RPAREN"):
              x -= 4
          elif (token.type == "LPAREN"):
              x += 4
          else:
              treeNodeList.append(treeNode(token.type, token.value,getPrecedence(token.type)+ x))
      return treeNodeList


def cutParen(tokSeq,index):
    count=0
    start =index
    for index in range(start,len(tokSeq)):
        if(tokSeq[index].type=="RPAREN"):
            count -= 1
        if (tokSeq[index].type == "LPAREN"):
            count += 1
        if count==0:
            return tokSeq[start:index+1],tokSeq[index+1:]

def replaceUnary(tokSeq):
    treeNodeList = []
    previous=None
    index=0
    result=[]
    prev=None
    prevPrev=None
    index=0
    for item in tokSeq:
        if(item.type=="NUMBER" or item.type=="LPAREN"):
            if(prev!=None):
                if (prev.type == "MINUS"):
                    detected = False
                    if  prevPrev==None :
                        detected=True
                    elif(not(prevPrev.type=="NUMBER" or prevPrev.type=="LRPAREN")):
                        detected = True
                    if detected:
                        result = tokSeq[:index - 1]
                        if (item.type == "NUMBER"):

                            result.append(lexer.token("LPAREN", "("))
                            result.append(lexer.token("LPAREN", "("))
                            result.append(lexer.token("NUMBER", 0))
                            result.append(lexer.token("MINUS", "-"))
                            result.append(lexer.token("NUMBER", 1))
                            result.append(lexer.token("RPAREN", ")"))
                            result.append(lexer.token("MULTIPLICATION", "*"))
                            result.append(item)
                            result.append(lexer.token("RPAREN", ")"))
                            return result+tokSeq[index+1:]
                        if (item.type == "LPAREN"):
                            cut,tail=cutParen(tokSeq,index)
                            result.append(lexer.token("LPAREN", "("))
                            result.append(lexer.token("LPAREN", "("))
                            result.append(lexer.token("NUMBER", 0))
                            result.append(lexer.token("MINUS", "-"))
                            result.append(lexer.token("NUMBER", 1))
                            result.append(lexer.token("RPAREN", ")"))
                            result.append(lexer.token("MULTIPLICATION","*"))
                            result+=cut
                            result.append(lexer.token("RPAREN", ")"))
                            result += tail
                            return result
        index+=1
        prevPrev=prev
        prev=item
    return tokSeq

def parse(tokSeq):
      rootNode = None
      treeNodeList = createTreeNodeList(tokSeq)
      parsing(treeNodeList)
      rootNode = findRoot(treeNodeList)
      return rootNode

def parsing(treeNodeList):

    dummyNode = treeNode("DUMMY","",0)
    treeNodeList.insert(0,dummyNode)
    treeNodeList.append(dummyNode)
    for index in range(len(treeNodeList)):
        node = treeNodeList[index]
        if node.type == "NUMBER":
            lOp = treeNodeList[index-1]
            rOp = treeNodeList[index+1]
            if rOp.precedence > lOp.precedence:
                #Right
                rOp.lChild = node
                node.parent = rOp
                if lOp.type != "DUMMY":
                    lOp.rChild = rOp
                    rOp.parent = lOp
            else:
                #Left
                lOp.rChild = node
                node.parent = lOp
                if rOp.type != "DUMMY":
                    while lOp.parent != None:
                        if lOp.parent.precedence < rOp.precedence:
                            break
                        lOp = lOp.parent
                    if lOp.parent != None:
                        lOp.parent.rChild = rOp
                        rOp.parent = lOp.parent
                    rOp.lChild = lOp
                    lOp.parent = rOp

def parsing1(tokSeq):
    treeNodeList = []
    x=0
    newSeq=replaceUnary(tokSeq)
    while len(tokSeq)!=len(newSeq):
        tokSeq=newSeq
        newSeq = replaceUnary(tokSeq)

    for token in tokSeq:
        if(token.type=="RPAREN"):
            x-=4
        elif (token.type == "LPAREN"):
            x += 4
        else:
            treeNodeList.append(treeNode(token.type,token.value,x))


    dummyNode = treeNode("DUMMY", "", 0)
    treeNodeList.insert(0, dummyNode)
    treeNodeList.append(dummyNode)
    for index in range(len(treeNodeList)):
        node = treeNodeList[index]
        if node.type == "NUMBER":
            lOp = treeNodeList[index - 1]
            rOp = treeNodeList[index + 1]
            if rOp.precedence > lOp.precedence:  # Right
                rOp.lChild = node
                node.parent = rOp
                if lOp != None:
                    lOp.rChild = rOp
                    rOp.parent = lOp
            else:            #Left
                lOp.rChild = node
                node.parent = lOp
                if rOp.type != "DUMMY":
                    while lOp.parent != None:
                         if lOp.parent.precedence <   rOp.precedence:
                             break
                         lOp = lOp.parent
                    if lOp.parent != None:
                        lOp.parent.rChild = rOp
                        rOp.parent = lOp.parent
                    rOp.lChild = lOp
                    lOp.parent = rOp
    return findRoot(treeNodeList)
def findRoot(treeNodeList):
      if len(treeNodeList)==3:
        return treeNodeList[1]
      rootNode = None
      for node in treeNodeList:
            if node.parent == None and node.type != "DUMMY":
                  rootNode = node
                  break
      return rootNode

def printHelper(rootNode):

    if rootNode!=None:
        if(rootNode.type=="DUMMY"):
            result = printHelper(rootNode.lChild)
            result += str(rootNode.value)
            result += printHelper(rootNode.rChild)
            return result
        if(rootNode.lChild==None and rootNode.rChild==None):
            return str(rootNode.value)
        else:
            result="("
            result+=printHelper(rootNode.lChild)
            result+=str (rootNode.value)
            result+=printHelper(rootNode.rChild)
            result+=")"
            return result
    return ""

def printTree(rootNode):
    print(printHelper(rootNode))
