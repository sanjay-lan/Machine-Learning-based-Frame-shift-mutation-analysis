#this is for feature selection of gene type in fs+1 
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import xgboost
from boruta import BorutaPy
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
import sklearn.metrics as metrics
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from pprint import pprint
from sklearn.model_selection import RandomizedSearchCV
from imblearn.under_sampling import RandomUnderSampler


from numpy import asarray
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report
scaler = MinMaxScaler()

plt.figure(0).clf()

#===========================================================================================

# FFS_8
data = pd.read_excel(r'/content/drive/MyDrive/fs/fs+1_o.xlsx')
file_path = "/content/drive/My Drive/fs/fs+1_o.xlsx"
df = pd.read_excel(file_path, index_col=0)
df.dropna(subset=['CAI'], inplace=True)

# n_c = len(df.columns)
# df1 = df.iloc[:, 2:n_c-1]
# #df2=(df1-df1.min())/(df1.max()-df1.min()) # minmax normalization
# X = (df1.iloc[:, 0:n_c-4])
# y = (list(df.iloc[:, n_c-1]))
data = data.drop('gene', axis=1)
data = data.drop('CAI', axis=1)
data = data.drop('GC%', axis=1)
data = data.drop('count', axis=1)
scaled = pd.DataFrame(scaler.fit_transform(data), columns=data.columns, index=data.index)
# scaled.dropna(subset=['CAI'], inplace=True)
#scaled = scaler.fit_transform(data)
X = scaled.drop('type', axis=1)


#print(X)

#print(X.shape)
y = scaled['type']

undersample = RandomUnderSampler(sampling_strategy='majority')
X_r, y_r = undersample.fit_resample(X, y)
X_resampled, y_resampled = undersample.fit_resample(X_r, y_r)

#print(y)
#class_names = ['essential', 'non-essential']
x_features = X.columns.tolist()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state = 43)
# fit model no training data

# from imblearn.over_sampling import SMOTE
# sm = SMOTE(random_state = 2)
# X_train_res, y_train_res = sm.fit_sample(X_train, y_train.ravel())
# # print('After OverSampling, the shape of train_X: {}'.format(X_train_res.shape))
# # print('After OverSampling, the shape of train_y: {} \n'.format(y_train_res.shape))
# print(X_train_res.shape)
# print(y_train_res.shape)
# print("After OverSampling, counts of label '1': {}".format(sum(y_train_res == 1)))
# print("After OverSampling, counts of label '0': {}".format(sum(y_train_res == 0)))
# print(type(X_train))
# print(type(y_train))
#print(X_train)
#print(y_train)

X_train = np.array(X_train)
# print(X_train)
y_train = np.array(y_train)
# print(y_train)
# print(type(X_train))
# print(type(y_train))
X_test = np.array(X_test)
y_test = np.array(y_test)



model = RandomForestClassifier(n_jobs=-1, class_weight='balanced', max_depth=5)
model.fit(X_train, y_train)
#print('RSCU \t' ,accuracy_score(y_test, model.predict(X_test)))
boruta_selector = BorutaPy(model, n_estimators='auto', verbose=0, random_state=1)
boruta_selector.fit(X_train, y_train)



# selected_rf_features = pd.DataFrame({'Feature':list(X_train.columns), 'Ranking':boruta_selector.ranking_})
selected_rf_features = pd.DataFrame({'Feature': x_features, 'Ranking': boruta_selector.ranking_})

# selected_rf_features.sort_values(by='Ranking', ascending=False)
a = selected_rf_features.sort_values(by='Ranking', ascending=True)
print(a)
a.to_csv("fs+1_type_selected_rf_features.csv", index=False)
