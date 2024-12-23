#this for fs-1 cai feature selection 
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

df = pd.read_excel(r'/content/drive/MyDrive/fs/fs-1cai.xlsx')
# file_path = "/content/drive/My Drive/fs/fs-1cai.xlsx"
# df = pd.read_excel(file_path, index_col=0)
# df.dropna(subset=['CAI'], inplace=True)

bins = [0, 0.3, 0.6, 1.0]
class_labels = [0, 1, 2]

X = pd.get_dummies(df.drop(columns=['CAI','gene', 'type','GC%','count']), drop_first=True)
y = pd.cut(df['CAI'], bins=bins, labels=class_labels)

undersample = RandomUnderSampler(sampling_strategy='majority')
X_r, y_r = undersample.fit_resample(X, y)
X_resampled, y_resampled = undersample.fit_resample(X_r, y_r)
# scaled = pd.DataFrame(scaler.fit_transform(data), columns=data.columns, index=data.index)
# # scaled.dropna(subset=['CAI'], inplace=True)
# #scaled = scaler.fit_transform(data)
# X = scaled.drop('CAI', axis=1)
y_resampled.to_csv('y_resampled.csv', index=False)

x_features = X_resampled.columns.tolist()

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.30, random_state = 43)

print(type(X_train))
print(type(y_train))


X_train = np.array(X_train)
print(X_train)
y_train = np.array(y_train)
print(y_train)
print(type(X_train))
print(type(y_train))
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
a.to_csv("fs+1_cai_selected_rf_features.csv", index=False)
