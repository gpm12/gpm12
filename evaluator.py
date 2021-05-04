def evaluate(rootNode):
    if rootNode.lChild==None and rootNode.rChild==None:
        return float(rootNode.value)
    elif rootNode.type=="PLUS":
        return evaluate(rootNode.lChild)+evaluate(rootNode.rChild)
    elif rootNode.type=="MINUS":
        return evaluate(rootNode.lChild)-evaluate(rootNode.rChild)
    elif rootNode.type=="MULTIPLICATION":
        return evaluate(rootNode.lChild)*evaluate(rootNode.rChild)
    elif rootNode.type=="DIVISION":
        return evaluate(rootNode.lChild)/evaluate(rootNode.rChild)
    return "Error"