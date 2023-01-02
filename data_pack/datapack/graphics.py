import matplotlib.pyplot as plt
from .metrics import roc,correlation_matrix
def plotroc(self,bool_attribute):
    #Given a numeric attribute and a boolean attribute plots the ROC curve
    ROC=roc(self,bool_attribute)
    plt.plot([x[0] for x in ROC], [x[1] for x in ROC])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.show()
def plot_correlation_matrix(ds):
    ''' plots the correlation matrix for a dataset with attributes of the same type'''
    cor_matrix=correlation_matrix(ds)
    plt.imshow(cor_matrix)
    plt.title('Correlation matrix')

    plt.show()
