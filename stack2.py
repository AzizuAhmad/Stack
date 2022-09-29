

from inspect import stack


class Stack(object):
    def __init__(self, limit = 10):
        self.stack = []
        self.limit = limit

    # untuk menampilkan stack
    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    # untuk menambah isi stack dengan data
    def push(self, data):
        if len(self.stack) >= self.limit:
            print('penuh')
        else:
            self.stack.append(data)

    # untuk menghaspus data pada stack
    def pop(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()

    # untuk melihaat data paling atas pada stack
    def peek(self):
        if len(self.stack) <= 0:
           
            return -1
        else:
            
            print("data paling atas : ",self.stack[len(self.stack) - 1]) 
            

    # untuk mengecek stack kosong atau tidak
    def isEmpty(self):
        if self.stack == 0:
            print('data kosong')
        else :
            print('data tidak kosong')
       

    # untuuk mengetahui ukuran stack
    def size(self):
       
        print('Jumlah data : ',len(self.stack))
        

if __name__ == '__main__':
    myStack = Stack()
    for i in range(10):
        myStack.push(i)
    print(myStack)
    myStack.pop()           
    print(myStack)
    myStack.peek()          
    myStack.isEmpty()
    myStack.size()