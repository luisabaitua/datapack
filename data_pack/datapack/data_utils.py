import numpy as np
from .Attribute import Attribute
from .Dataset import Dataset
def norm(self):
    '''Returns the normalization of a numeric attribute'''
    if isinstance(self,Attribute):
        if self.tipo != 'Numeric':
            raise NameError('Non numeric attribute can not be normalized')
        m,M=min(self.attribute),max(self.attribute)
        normalised=Attribute([(self.attribute[i]-m)/(M-m) for i in range(len(self.attribute))])
        return(normalised)
    elif isinstance(self,Dataset):
        newds=Dataset(self.dataset.copy())
        for i in range(len(self.dataset)):
            if newds.dataset[i].tipo=='Numeric':
                newds.dataset[i]=norm(newds.dataset[i])
        return(newds)
def stan(self):
    '''Returns the standarization of a numeric attribute'''
    if isinstance(self,Attribute):
        if self.tipo != 'Numeric':
            raise NameError('Non numeric attribute can not be standarised')
        mean=np.mean(self.attribute)
        sd=np.std(self.attribute)
        standarised=Attribute([(self.attribute[i]-mean)/(sd) for i in range(len(self.attribute))])
        return(standarised)
    elif isinstance(self,Dataset):
        newds=Dataset(self.dataset.copy())
        for i in range(len(self.dataset)):
            if newds.dataset[i].tipo=='Numeric':
                newds.dataset[i]=stan(newds.dataset[i])
        return(newds)
def filtrate(ds,metric,threshold):
    '''For a dataset keeps only the attributes that have a metric greater than a given threshold'''
    metricas=metric(ds)
    filtr_attributes=[]
    for i in range(len(metricas)):
        if (metricas[i]==None):
            filtr_attributes.append(ds.dataset[i])
        elif(metricas[i]>=threshold):
            filtr_attributes.append(ds.dataset[i])
    return(Dataset(filtr_attributes))
