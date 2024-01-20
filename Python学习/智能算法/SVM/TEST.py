from sklearn import svm

x = [[-3  , -1],
     [0   , -2],
     [-2.5,  2],
     [-1  , -1],
     [3   ,  5],
     [-5  ,  3],
     [-3  , -3]]

y = [0, 1, 0, 1, 1, 0, 1]

clf =svm.SVC(kernel='linear').fit(x,y)

cc = clf.predic([[2, 4]])

print(cc)