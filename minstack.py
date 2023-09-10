# 155. Min Stack

class MinStack:

    def __init__(self):
        self.st=[] #stack
        self.min=None #min element

    def push(self, val):
        if len(self.st)==0:
            self.st.append(val)
            self.min=val
        else:
            if val>=self.min:
                self.st.append(val)
            else:
                self.st.append(2*val-self.min)
                self.min=val
                
    def pop(self):
        x=self.st.pop() 
        if x<self.min:
            self.min=2*self.min-x
    
    def top(self):
        x=self.st[-1]
        if x>=self.min:
            return x
        return self.min

    def getMin(self):
        return self.min
