import numpy as np
from .Attribute import Attribute
from .Dataset import Dataset
def var(self):
    #Calcula la varianza de un attributo numérico
    if isinstance(self,Attribute):
        if self.tipo!='Numeric':
            raise NameError('Not numeric attribute has not variance')
        return(np.var(self.attribute))
    
    #Calcula la varianza de los atributos numéricos de un dataset
    if isinstance(self,Dataset):
        varianzas=[None]*len(self.dataset)
        for i in range(len(self.dataset)):
            if self.dataset[i].tipo=='Numeric':
                varianzas[i]=var(self.dataset[i])
        return(varianzas)    
def entropy(self):
    #Calculaa la varianza de un attributo numérico
    if isinstance(self,Attribute):
        if self.tipo=='Numeric':
            raise NameError('Entropy can not be computed for numeric attribute')
        value,counts = np.unique(self.attribute,return_counts=True)
        if len(value)<=1:
            return 0
        else:
            p=counts/len(self)
            return(np.sum(-p*np.log2(p)))

    if isinstance(self,Dataset):
        entropys=[None]*len(self.dataset)
        for i in range(len(self.dataset)):
            if self.dataset[i].tipo=='Categorical' or  self.dataset[i].tipo=='Boolean':
                entropys[i]=entropy(self.dataset[i])
        return(entropys)
def roc(self,bool_attribute):
    #Given a numeric attribute and a boolean attribute returns the points in the ROC curve
    if isinstance(self,Attribute):
        if self.tipo!='Numeric' and bool_attribute!='Boolean':
            raise NameError('The attributes are not numeric and boolean')
        roc=[0]*len(self)
        ordenada=sorted(self.attribute)
        for i in range(len(self)):
            prediccion=[el>ordenada[i] for el in self.attribute]
            TP=np.sum([(prediccion[j]==True and bool_attribute.attribute[j]==True) for j in range(len(self))])
            TN=np.sum([prediccion[j]==False and bool_attribute.attribute[j]==False for j in range(len(self))])
            FP=np.sum([prediccion[j]==True and bool_attribute.attribute[j]==False for j in range(len(self))])
            FN=np.sum([prediccion[j]==False and bool_attribute.attribute[j]==True for j in range(len(self))])
            TPR=TP/(TP+FN)
            FPR=FP/(FP+TN)
            roc[i]=(FPR,TPR)
        roc=[(1,1)]+roc
        return(roc)
def auc(self,bool_attribute):
    #Given a numeric attribute and a boolean attribute returns the area under the roc curve
    if isinstance(self,Attribute):
        if self.tipo!='Numeric' and bool_attribute!='Boolean':
            raise NameError('The attributes are not numeric and boolean')
        ROC=roc(self,bool_attribute)
        auc=np.sum([ROC[i][1]*(ROC[i][0]-ROC[i+1][0]) for i in range(len(ROC)-1)])
        return auc
def auc_ds(self,bool_attribute):
    if isinstance(self,Dataset):
        aucs=[None]*len(self.dataset)
        for i in range(len(self.dataset)):
            if self.dataset[i].tipo=='Numeric':
                aucs[i]=auc(self.dataset[i],bool_attribute)
        return(aucs) 
import math
def correlation(self,attribute2):
    '''Calculates the correlation between two numeric attributes or mutual information between two categorical attributes'''
    if isinstance(self,Attribute) and isinstance(attribute2,Attribute):
        if len(self)!=len(attribute2):
            raise NameError('The attributes do not have the same length')

        if self.tipo=='Numeric' and attribute2.tipo=='Numeric':
            mean_x,mean_y,sd_x,sd_y=np.mean(self.attribute),np.mean(attribute2.attribute),np.std(self.attribute),np.std(attribute2.attribute)
            return(np.sum([(self.attribute[i]-mean_x)*(attribute2.attribute[i]-mean_y) for i in range(len(self))])/(sd_x*sd_y))
        
        if (self.tipo=='Categorical' or self.tipo=='Boolean') and (attribute2.tipo=='Categorical' or attribute2.tipo=='Boolean'):
                mutual_info = 0
                p_x={}
                p_y={}
                p_xy={}
                for i in range(len(self)):
                    x=self.attribute[i]
                    y=attribute2.attribute[i]
                    if x in p_x:
                        p_x[x]+=1
                    else:
                        p_x[x]=1
                    if y in p_y:
                        p_y[y]+=1
                    else:
                        p_y[y]=1
                    if (x,y) in p_xy:
                        p_xy[x,y]+=1
                    else:
                        p_xy[x,y]=1
                    
                for (i,j) in p_xy.keys():
                        mutual_info += -p_xy[(i,j)] * math.log2(p_xy[(i,j)] / (p_x[i] * p_y[j]))
                return mutual_info
def correlation_matrix(ds):
    '''calculates the correlation matrix for a dataset with attributes of the same type'''
    cor_matrix=np.zeros((len(ds.dataset),len(ds.dataset)))
    for i in range(len(ds.dataset)):
        for j in range(len(ds.dataset)):
            cor_matrix[i,j]=correlation(ds.dataset[i],ds.dataset[j])
    return(cor_matrix)
