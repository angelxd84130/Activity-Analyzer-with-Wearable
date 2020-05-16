import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

x = ["Still", "Walking", "Run", "Bike", "Car", "Bus", "Train", "Subway"]

df = pd.read_csv("TRAIN_BIGDATA.csv")
df = df.sample(frac=True, random_state=1)
y = df['label']
del df['label']
df = df[df.columns[0:]].values
model = DecisionTreeClassifier()
model.fit(df, y)

test = pd.read_csv("TEST_BIGDATA.csv")
y_test = test['label']
del test['label']
test = test[test.columns[0:]].values
test_pre = model.predict(test)
print(accuracy_score(y_test, test_pre), "\n\n")
print(confusion_matrix(y_test, test_pre))


dot_data = StringIO()
export_graphviz(model, out_file='tree.dot')
from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])
Image(filename='tree.png')

