class myiter:
    def __init__(self, callable, initial, sentinel):
        self.value = initial
        self.callable = callable
        self.sentinel = sentinel

    def __iter__(self):
        return self

    def next(self):
        if self.value == self.sentinel:
            raise StopIteration
        else:
            # calculate next value from prev value
            self.value = self.callable(self.value) 
            return self.value

#if __name__ == '__main__':
    #call_iter = myiter(lambda x:x + 1, 0, 100)
def func():    
    #result = []
    for i in range(10):
	#result.append(i*i)
        #return result
        yield i*i

for i in func():
    print(i)
