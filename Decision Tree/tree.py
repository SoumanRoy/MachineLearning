from sklearn.datasets import *
from sklearn import tree
import graphviz

wine = load_wine()
clf = tree.DecisionTreeClassifier() # init the tree
clf = clf.fit(wine.data, wine.target) # train the tree
# export the learned decision tree
dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names=wine.feature_names,
                         class_names=wine.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("digit") # tree saved to wine.pdf
