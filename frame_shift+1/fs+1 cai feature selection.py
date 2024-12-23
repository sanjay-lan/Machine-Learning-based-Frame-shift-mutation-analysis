#this code is for cai features in fs+1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import roc_curve, auc
from imblearn.under_sampling import RandomUnderSampler

file_path = "/content/drive/My Drive/fs/fs+1_o.xlsx"
df = pd.read_excel(file_path, index_col=0)
df.dropna(subset=['CAI'], inplace=True)

classifiers = [
    RandomForestClassifier(random_state=1234),
]

mean_fpr = np.linspace(0, 1, 100)

tpr_dict = {cls.__class__.__name__: {0: [], 1: [], 2: []} for cls in classifiers}
auc_dict = {cls.__class__.__name__: {0: [], 1: [], 2: []} for cls in classifiers}

num_iterations = 1

mean_importance_scores = []

for _ in range(num_iterations):
    bins = [0, 0.3, 0.6, 1.0]
    class_labels = [0, 1, 2]

    X = pd.get_dummies(df.drop(columns=['CAI','type','count','GC%']), drop_first=True)
    y = pd.cut(df['CAI'], bins=bins, labels=class_labels)
    undersample = RandomUnderSampler(sampling_strategy='majority')
    X_r, y_r = undersample.fit_resample(X, y)
    X_resampled, y_resampled = undersample.fit_resample(X_r, y_r)
    # print(y_resampled)
    for cls in classifiers:
        for current_class in range(3):
            #print(y_resampled)

            y_binary = (y_resampled == current_class).astype(int)


            X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_binary, test_size=0.20, random_state=1234)
            
            model = cls.fit(X_train, y_train)
            y_pred = model.predict_proba(X_test)
            y_pred_class = model.predict(X_test)

            feature_importance_scores = model.feature_importances_
            mean_importance_scores.append(feature_importance_scores)

mean_importance_scores = np.mean(mean_importance_scores, axis=0)
mean_importance_df = pd.DataFrame({'Feature': X.columns, 'Mean Importance': mean_importance_scores * 100})
mean_importance_df = mean_importance_df.sort_values(by='Mean Importance', ascending=False)
print("Mean Feature Importance Scores:")
print(mean_importance_df)
