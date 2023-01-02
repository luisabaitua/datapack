
import numpy as np
from data_pack.datapack import data_utils,attrutils,Dataset,Attribute,discretization,metrics,graphics
def test_all():
    """Executes the tests to verify the installation has ben successfull"""
    ds=Dataset.Dataset([Attribute.Attribute([1.,2.,5.,6.,4.9,7.]),Attribute.Attribute([False,False,True,True,True,False]),Attribute.Attribute(['a','b','v','a','a','a']),Attribute.Attribute([1.2,3.5,6.1,-1.2,-8.,22.])])
    y=Attribute.Attribute([1.,2.3,4.,-1.5,-3.7])
    ##############
    discretization.discretizeEF(y,2)
    discretization.discretizeEF(ds,2)
    discretization.discretizeEW(y,2)
    discretization.discretizeEW(ds,2)
    discretization.discretize(y,[-1,5])
    discretization.discretize(ds,[-1,5])
    ###
    metrics.var(y)
    metrics.var(ds)
    ycat=Attribute.Attribute(['a','b','a'])
    metrics.entropy(ycat)
    metrics.entropy(ds)
    metrics.roc(([1,2,5,6,7]),Attribute.Attribute([False,False,True,True,True]))
    metrics.auc(Attribute.Attribute([1,2,5,6,7]),Attribute.Attribute([False,False,True,True,False]))
    metrics.auc_ds(ds,Attribute.Attribute([False,False,True,True,False,True]))
    graphics.plotroc(Attribute.Attribute([1,2,5,6,7]),Attribute.Attribute([False,False,True,True,True]))
    data_utils.stan(y)
    data_utils.stan(ds)
    data_utils.norm(y)
    data_utils.norm(ds)
    data_utils.filtrate(ds,metrics.entropy,1.1)
    data_utils.filtrate(ds,metrics.var,5)
    metrics.correlation(ds.dataset[0],ds.dataset[3])
    metrics.correlation(ds.dataset[1],ds.dataset[2])    
    metrics.correlation(ds.dataset[2],Attribute.Attribute([False,False,False,False,False,False]))
    at1=Attribute.Attribute([1,3.2,4,1.6,1.7,-0.1,5])
    at2=Attribute.Attribute([1,3.2,4,1.6,1.7,-0.1,10])
    at3=Attribute.Attribute([-1,-3.2,-4,-1.6,-1.7,-0.1,-10])
    at4=Attribute.Attribute([-2,-6.2,-4,-3.6,-3.4,0.2,-20])
    ds_num=Dataset.Dataset([at1,at2,at3,at4])
    metrics.correlation_matrix(ds_num)
    graphics.plot_correlation_matrix(ds_num)
if __name__=='__main__':
    test_all()
