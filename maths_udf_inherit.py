class maths:
    def add(self,*args):
        s = 0
        for a in args:
            s = s+a
        print(s) 
    def sub(self,*args):
        s = 0
        for a in args:
            s = s-a
        print(s)
    
    def mul(self,*args):
        s = 1
        for a in args:
            s = s*a 
        print(s)
    
    def div(self,*args):
        s = 1
        for a in args:
            s = s/a
        print(s)


p = maths()
p.add(10,7,1)
p.sub(10,7,435)
p.mul(10,7)
p.div(10,7,345,65)
