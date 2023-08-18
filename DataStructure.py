class SNode:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data
    
    @property
    def nextNode(self):
        return self._nextNode
    
    @nextNode.setter
    def nextNode(self, newNextNode):
        if isinstance(newNextNode, SNode):
            self._nextNode = newNextNode
        elif newNextNode != None:
            self._nextNode = SNode(newNextNode)
        else:
            self._nextNode = None

    def __str__(self) -> str:
        return str(self.data)
    
class DNode(SNode):
    def __init__(self, data, prevNode=None, nextNode=None):
        super().__init__(data, nextNode)
        self.prevNode = prevNode
    
    @property
    def prevNode(self):
        return self._prevNode
    
    @prevNode.setter
    def prevNode(self, newPrevNode):
        if isinstance(newPrevNode,DNode):
            self._prevNode = newPrevNode
        elif newPrevNode != None:
            self._prevNode = DNode(newPrevNode)
        else:
            self._prevNode = None

class SLList:
    def __init__(self):
        self._head = None
        self._end = None
        self._len = 0
    
    @property
    def head(self):
        return self._head
    
    def append(self, data):
        newNode = SNode(data)
        if self._head == None:
            self._head = newNode
            self._end = newNode
        else:
            self._end.nextNode = newNode
            self._end = newNode
        self._len += 1
    
    def insert(self, data, index=None):
        if index != None:
            if isinstance(index, int):
                if len(self) > index:
                    if index >= 0:
                        pivot = self.head
                        indexPivot = 0
                        prevNode = None
                        while indexPivot < index:
                            prevNode = pivot
                            pivot = pivot.nextNode
                            indexPivot += 0
                        newNode = SNode(data)
                        if prevNode != None:
                            prevNode.nextNode = newNode
                        newNode.nextNode = pivot
                        self._len += 1
                    else:
                        raise IndexError("SLList no admite indices negativos.")
                else:
                    self.append(data)
            else:
                raise ValueError('"index" debe ser un numero entero.')
        else:
            newNode = SNode(data)
            newNode.nextNode = self.head
            self._len += 1

    
    def __len__(self):
        return self._len
    
    def __str__(self):
        pivot = self.head
        string = '['
        while pivot != None:
            string += str(pivot.data) + ', '
            pivot = pivot.nextNode
        if string != '[':
            string = string[:len(string)-2]
            string += ']'
            return string
        else:
            return "[]"

class Stack:
    def __init__(self):
        self._top = None
        self._len = 0
    
    def push(self, data):
        newNode = DNode(data)
        if self._top != None:
            self._top.nextNode = newNode
            newNode.prevNode = self._top
        self._top = newNode
        self._len += 1
    
    def pop(self):
        if self._top != None:
            data = self._top.data
            if self._top.prevNode != None:
                self._top = self._top.prevNode
                self._top.nextNode = None
            else:
                self._top = None
            self._len -= 1
            return data
        else:
            raise IndexError("La pila se encuentra vacia.")
    
    def peek(self):
        if self._top != None:
            return self._top.data
        else:
            raise IndexError("La pila se encuentra vacia.")
    
    def isEmpty(self):
        return self._top == None
    
    def search(self, target):
        index = 0
        pivot = self._top
        while index < self._len and pivot.data != target:
            index += 1
            pivot = pivot.prevNode
        if index < self._len:
            return index
        else:
            return -1
    
    def copy(self):
        copy = Stack()
        if self._top != None:
            nextNode = DNode(self._top.data)
            copy._len += 1
            top = nextNode
            pivot = self._top.prevNode
            while pivot != None:
                prevNode = DNode(pivot.data)
                nextNode.prevNode = prevNode
                prevNode.nextNode = nextNode
                nextNode = prevNode
                pivot = pivot.prevNode
                copy._len += 1
            copy._top = top
        return copy
    
    def clear(self):
        while self._top != None:
            self.pop()
    
    def equalityCheck(self, compare):
        if isinstance(compare, Stack):
            if len(compare) == len(self):
                pivot1 = self._top
                pivot2 = compare._top
                while pivot1 != None and pivot1.data == pivot2.data:
                    pivot1 = pivot1.prevNode
                    pivot2 = pivot2.prevNode
                if pivot1 == None:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    @staticmethod
    def postfix(expression):
        try:
            stack = Stack()
            elements = expression.split()
            for element in elements:
                if element.isdigit():
                    stack.push(int(element))
                else:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    if element == '+':
                        stack.push(num1+num2)
                    elif element == '-':
                        stack.push(num2-num1)
                    elif element == '*':
                        stack.push(num1*num2)
                    elif element == '/':
                        stack.push(num2/num1)
                    else:
                        raise TypeError("Esta funcion solo opera sobre '+,-,*,/'")
            if len(stack) == 1:
                return stack.pop()
            else:
                raise TypeError(f"La expresion en notacion matematica postfix {expression} no es valida.")
        except TypeError as error:
            print(error)
            return -1
        except IndexError as error:
            print(f"La expresion en notacion matematica postfix {expression} no es valida.")
            return -1
    
    def __len__(self):
        return self._len
    
    def __str__(self):
        copy = self.copy()
        string = 'stack is Empty'
        pivot = self._top
        if len(self) != 0:
            string = ''
            while pivot != None:
                string += f'{pivot.data} > '
                pivot = pivot.prevNode
            string = string[:len(string)-2]
        return string

