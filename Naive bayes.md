# AAICIPY
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import math
from sklearn.metrics import confusion_matrix 
import seaborn as sns
import scikitplot.metrics as skplt

x=preprocessed_reviews[:95000]
y=filtered_data['Score']
z=y[:95000]

x_tr, x_cv, y_tr, y_cv = train_test_split(x, z, test_size=0.2) # 20 % data into cv, 80% in the tr
x_train, x_test, y_train, y_test = train_test_split(x_tr, y_tr, test_size=0.2) 

bow = CountVectorizer()
x_train=bow.fit_transform(x_train)
x_cv=bow.transform(x_cv)
x_test=bow.transform(x_test)

i_val=[]
auc_score=[]
auc_train_score=[]
for i in (10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 1, 10**1, 10**2, 10**3, 10**4, 10**5):
    clf=MultinomialNB(alpha=i)
    clf.fit(x_train, y_train)
    y_pred_cv=clf.predict_proba(x_cv)[:,1]
    y_pred_train=clf.predict_proba(x_train)[:,1]
    i_val.append(i)    
    auc=roc_auc_score(y_cv, y_pred_cv)
    auc_train=roc_auc_score(y_train, y_pred_train)
    auc_score.append(auc)
    auc_train_score.append(auc_train)
    print('auc for alpha={x} is {y}'.format(x=i, y=auc))

    
i_val=[math.log(i) for i in i_val]
plt.plot(i_val, auc_score, 'r', label='CV AUC')
plt.plot(i_val, auc_train_score, 'b', label='Train AUC')
plt.legend(loc='best')
plt.xlabel('Alpha log value')
plt.ylabel('AUC value')
plt.title('AUC chart')
plt.show()

a=max(auc_score)
b=auc_score.index(a)
c=i_val[b]

print('we got best accuracy={y} on alpha={x}, now lets calculate accuracy of test data on alpha={x}'.format(x=np.exp(c), y=a))

clf=MultinomialNB(alpha=a)
clf.fit(x_train, y_train)
y_test_pred=clf.predict_proba(x_test)[:,1]
y_test_predicted=clf.predict(x_test)
auc_test = roc_auc_score(y_test, y_test_pred)
print('AUC on test data for alpha={x} is {y}'.format(x=np.exp(c), y=auc_test))

#fpr, tpr, threshold= roc_curve(y_test, y_test_pred)
#plt.plot(fpr, tpr, 'r', label='test_roc')

fpr, tpr, threshold = metrics.roc_curve(y_test, y_test_pred)
fpr_tr, tpr_tr, threshold_tr = metrics.roc_curve(y_train, y_pred_train)
roc_auc = metrics.auc(fpr, tpr)
roc_auc_tr = metrics.auc(fpr_tr, tpr_tr)

plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC_test = %0.2f' % roc_auc)
plt.plot(fpr_tr, tpr_tr, 'g', label= 'AUC_train = %0.2f' % roc_auc_tr)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

skplt.plot_confusion_matrix(y_test ,y_test_predicted)
plt.plot()
