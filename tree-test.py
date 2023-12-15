class binaryTree: # ADD ANY TYPE HINTS REQUIRED
    def __init__(self,nodeData,left=None,right=None):
        self.__nodeData = nodeData
        self.__left = left
        self.__right = right
    @property
    def NodeData(self):
        return self.__nodeData
    @NodeData.setter
    def NodeData(self,inputNodeData):
        self.__nodeData = inputNodeData
    @property
    def Left(self):
        return self.__left
    @Left.setter
    def NodeData(self,inputLeft):
        self.__left = inputLeft
    @property
    def Right(self):
        return self.__right
    @Right.setter
    def Right(self,inputRight):
        self.__right = inputRight
    def traverse(self):
        if self.Left != None:
            self.traverse(self.Left)
        if self.Right != None:
            self.traverse(self.Right)
        return self.NodeData