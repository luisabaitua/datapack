from .Attribute import Attribute
from .Dataset import Dataset
import numpy as np
def discretizeEW(self,num_bins):
    '''Dado un atributo devuelve la discretización EW en forma de vector categórico'''
    '''Dado un dataset devuelve un dataset con las variables numéricas discretizadas'''
    if isinstance(self,Attribute):
        if self.tipo!='Numeric':
            raise NameError('Not numeric attribute can not be discretized')
    #Calcula la anchura de los intervalos
        m=min(self.attribute)
        rango = max(self.attribute)-m
        anchura=rango / num_bins
        
    #Calcula los puntos de corte
        puntos=[min(self.attribute)+(i*anchura) for i in range(num_bins+1)]
        categorias = ["({},{}]".format(puntos[i], puntos[i + 1]) for i in range(num_bins)]
        
    #Calcula el intervalo de cada elemento
        indices = [int((ele - m) // anchura) for ele in self.attribute]
        indices=[i-1 if i==num_bins  else i for i in indices]
        x_discretized=[categorias[indices[i]] for i in range(len(self))]
        return(Attribute(x_discretized))
    if isinstance(self,Dataset):
        newds=Dataset(self.dataset.copy())
        for i in range(len(self.dataset)):
            if newds.dataset[i].tipo=='Numeric':
                newds.dataset[i]=discretizeEW(self.dataset[i],num_bins)
        return(newds)
    
def discretizeEF(self,num_bins):
    '''Dado un atributo devuelve la discretización EF en forma de vector categórico'''
    '''Dado un dataset devuelve un dataset con las variables numéricas discretizadas'''
    if isinstance(self,Attribute):
        if self.tipo!='Numeric':
            raise NameError('Not numeric attribute can not be discretized')
        #Calcula puntos de corte
        n=len(self)//num_bins #Número de elementos por intervalo
        k=len(self)%num_bins #Número de intervalos con n+1 elemenetos
        ordenado=sorted(self.attribute)
        puntos=[min(self.attribute)]
        for i in range(k):
            puntos.append(ordenado[(i+1)*n])
        for i in range(num_bins-k):
            puntos.append(ordenado[(i+k+1)*n-1])
        puntos=[min(self.attribute)]+puntos+[max(self.attribute)]
        #Calcula indices de cada elemento
        indices=[0]*len(self)
        for i in range(len(self)):
            j=0
            while self.attribute[i]>puntos[j]:
                j+=1
            indices[i]=j-1
        indices=[i+1 if i==-1  else i for i in indices]
        
        #Calcula intervalo de cada elemento
        categorias = ["({},{}]".format(puntos[i], puntos[i + 1]) for i in range(len(puntos)-1)]
        x_discretized=[categorias[indices[i]] for i in range(len(self))]
        return(Attribute(x_discretized))
    if isinstance(self,Dataset):
        newds=Dataset(self.dataset.copy())
        for i in range(len(self.dataset)):
            if newds.dataset[i].tipo=='Numeric':
                newds.dataset[i]=discretizeEF(self.dataset[i],num_bins)
        return(newds)
def discretize(self,puntos):
    '''Dado un atributo y los puntos de corte devuelve la discretización en forma de vector categórico'''
    '''Dado un dataset devuelve un dataset con las variables numéricas discretizadas'''
    if isinstance(self,Attribute):
        if self.tipo!='Numeric':
            raise NameError('Not numeric attribute can not be discretized')
        puntos=[-np.inf]+puntos+[np.inf]
        num_bins=len(puntos)-1
        #Calcula indices de cada elemento
        indices=[0]*len(self)
        for i in range(len(self)):
            j=0
            while self.attribute[i]>puntos[j]:
                j+=1
            indices[i]=j-1
        
        #Calcula intervalo de cada elemento
        categorias = ["({},{}]".format(puntos[i], puntos[i + 1]) for i in range(num_bins)]
        x_discretized=[categorias[indices[i]] for i in range(len(self))]
        return(Attribute(x_discretized))
    if isinstance(self,Dataset):
        newds=Dataset(self.dataset.copy())
        for i in range(len(self.dataset)):
            if newds.dataset[i].tipo=='Numeric':
                newds.dataset[i]=discretize(newds.dataset[i],puntos)
        return(newds)
