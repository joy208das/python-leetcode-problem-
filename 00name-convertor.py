class nobodong(object):
    def lulu(self,a):
        b=list(a)
        for i in range(len(b)):
            if b[i]==" ":
                b[i]="_"
                
        # return "".join(map(str,b))
        return "".join(b)
    

a=input('enter problem name:')
x=int(input('enter problem no: '))

a=a.lower()
out = nobodong()
output= out.lulu(a)


print(f"{x}-{output}.py")