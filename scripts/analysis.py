import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
import os

output_directory = '/Users/victordashuaibi/Desktop/is477-fall2023-final-project/results'

#import dataset
col = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
df = pd.read_csv('/Users/victordashuaibi/Desktop/is477-fall2023-final-project/data/car.data',header=None,names=col)

#summary stat
summary_stats = df.describe()
output_file_path = os.path.join(output_directory, 'summary_statistics.csv')
summary_stats.to_csv(output_file_path)

#simple vis
plt.figure(figsize=(8, 6))
sns.countplot(x='class', data=df)
plt.title('Distribution of Car Classes')
plt.xlabel('Class')
plt.ylabel('Count')
output_file_path = os.path.join(output_directory, 'simple_vis.png')
plt.savefig(output_file_path)

#simple classification
encoder = LabelEncoder()
for col in df.columns:
    df[col] = encoder.fit_transform(df[col])
X = df.drop('class', axis=1)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
classification_report_text = classification_report(y_test, y_pred)
classification_report_text

output_file_path = os.path.join(output_directory, 'classification_report.txt')
with open(output_file_path, 'w') as file:
    file.write(classification_report_text)