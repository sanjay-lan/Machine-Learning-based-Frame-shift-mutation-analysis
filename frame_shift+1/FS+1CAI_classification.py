#this
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
    LogisticRegression(max_iter=10000, random_state=1234),
    GaussianNB(),
    # KNeighborsClassifier(),
    # SVC(probability=True, random_state=1234),
    DecisionTreeClassifier(random_state=1234),
    RandomForestClassifier(random_state=1234),
    AdaBoostClassifier(random_state=1234),
    GradientBoostingClassifier(random_state=1234),
    XGBClassifier(random_state=1234)
]

mean_fpr = np.linspace(0, 1, 100)

tpr_dict = {cls.__class__.__name__: {0: [], 1: [], 2: []} for cls in classifiers}
auc_dict = {cls.__class__.__name__: {0: [], 1: [], 2: []} for cls in classifiers}

num_iterations = 50

for _ in range(num_iterations):
    bins = [0, 0.3, 0.6, 1.0]
    class_labels = [0, 1, 2]

    X = pd.get_dummies(df.drop(columns=['CAI', 'type']), drop_first=True)
    y = pd.cut(df['CAI'], bins=bins, labels=class_labels)
    undersample = RandomUnderSampler(sampling_strategy='majority')
    X_r, y_r = undersample.fit_resample(X, y)
    X_resampled, y_resampled = undersample.fit_resample(X_r, y_r)
    X_resampled.to_csv('1.csv')
    y_resampled.to_csv('0.csv')
    # print(y_resampled)
    for cls in classifiers:
        for current_class in range(3):
            y_binary = (y_resampled == current_class).astype(int)
            # print(y_binary)
            X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_binary, test_size=0.20, random_state=1234)
            y_test.to_csv("11.csv")
            model = cls.fit(X_train, y_train)
            y_pred = model.predict_proba(X_test)
            y_pred_class = model.predict(X_test)
            fpr, tpr, _ = roc_curve(y_test, y_pred[:, 1], pos_label=1)
            # tprs.append(np.interp(mean_fpr, fpr, tpr))
            # tprs[-1][0] = 0.0

            interp_tpr = np.interp(mean_fpr, fpr, tpr)
            interp_tpr[0] = 0.0

            tpr_dict[cls.__class__.__name__][current_class].append(interp_tpr)
            auc_value = auc(fpr, tpr)
            auc_dict[cls.__class__.__name__][current_class].append(auc_value)


mean_tpr_dict = {}
mean_auc_dict = {}

for cls_name in tpr_dict:
    mean_tpr_dict[cls_name] = {}
    mean_auc_dict[cls_name] = {}
    for current_class in range(3):
        mean_tpr_dict[cls_name][current_class] = np.mean(tpr_dict[cls_name][current_class], axis=0)
        mean_auc_dict[cls_name][current_class] = np.mean(auc_dict[cls_name][current_class])


plt.figure(figsize=(21, 8))

for current_class in range(3):
    plt.subplot(1, 3, current_class + 1)
    plt.title(f'ROC Curve - Class {current_class}')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])

    for cls_name in mean_tpr_dict:
        mean_tpr = mean_tpr_dict[cls_name][current_class]
        mean_auc = mean_auc_dict[cls_name][current_class]
        plt.plot(mean_fpr, mean_tpr, lw=2, alpha=0.8, label=f'{cls_name} (AUC = {mean_auc*100:.2f})')

    plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r', label='Chance')
    plt.legend(loc='lower right')

plt.tight_layout()
plt.show()
