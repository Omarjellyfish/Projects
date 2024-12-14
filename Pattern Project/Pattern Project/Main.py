import sklearn
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.neighbors import KNeighborsClassifier as KNN 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA 
# load the dataset
dataset = pd.read_csv('Data.csv')

# Separate features and target also drop the unneeded columns
x = dataset.drop(columns=['Exercise Recommendation Plan', 'Gender', 'BMIcase'])
y = dataset['Exercise Recommendation Plan']

# Split the dataset into training and testing sets 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2) 
#gives us the mean and standard deviation of data using standard scaler
#because data in range 0->1000 would dominate the algorithm as opposed to 0->1
# so we scale properly
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Create an instance of the KNeighborsClassifier class
knn = KNN()

# Fit the classifier to the training data
knn.fit(x_train, y_train) #default value is 5
# Make predictions on the testing data
y_predict = knn.predict(x_test)
# Calculate accuracy
acc = accuracy_score(y_test, y_predict)

#using confusion matrix
confMatrix=confusion_matrix(y_pred=y_predict,y_true=y_test)
print(confMatrix)
# display the confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=confMatrix, display_labels=knn.classes_)
disp.plot(cmap=plt.cm.Blues) #making color shades of blue
plt.show()


print('KNN Accuracy: ', acc)

testDataFrame=pd.DataFrame({
    'Weight':[60,100,71],
    'Height':[150,190,173],
    'BMI':[26.7,27.7,23.7],
    'Age':[21,21,21],
    'gender':[0,1,1],
    'BMIclass':[4,4,1]
})
test_data_scaled = scaler.transform(testDataFrame)
predictions = knn.predict(test_data_scaled)
print("Predictions for test data:")
for i, prediction in enumerate(predictions):
    print(f"Sample {i+1}: Exercise Recommendation Plan {prediction}")