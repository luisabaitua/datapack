from .Attribute import Attribute
def isdataset(lista):
    '''Checks that a list has attributes of the same length'''
    for x in lista:
        if (type(x)!=Attribute):
            raise NameError('Not all the elements in the list are attributes')
        if (len(x)!=len(lista[0])):
            raise NameError('The attributes are not of the same length')
    return(True)
class Dataset:
    def __init__(self,lista):
        if isdataset(lista):
            self.dataset=lista
        self.size=(len(lista[0]),len(lista))
    def __str__(self):
        st=''
        for atributo in self.dataset:
            st=st+str(atributo)+'\n'
        return(st)
    def __repr__(self):
        st=''
        for atributo in self.dataset:
            st=st+str(atributo)+'\n'
        return(st)
    def tipos(self):
        tipos=[]
        for atributo in self.dataset:
            tipos.append(atributo.tipo)
        return(tipos)
