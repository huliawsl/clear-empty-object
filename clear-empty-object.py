doc = MQSystem.getDocument()

numO = doc.numObject

for i in range(numO):
    obj = doc.object[i]
    obj.typeName = "Object"

def checknF(n):
    obj = doc.object[n]
    numV = obj.numVertex
    MQSystem.println(str(numV))
    if numV == 0:
        return 1
    else:
        return 0
for i in range(numO):
    obj = doc.object[i]
    numV = obj.numVertex
    backr = checknF(i)
    if backr == 1:
        doc.removeObject(doc.object[i])
        doc.deleteObject(i)

