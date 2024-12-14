import sklearn
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.neighbors import KNeighborsClassifier as KNN 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA  # Import PCA
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Read the dataset
dataset = pd.read_csv('Data.csv')

# Separate features and target variable
x = dataset.drop(columns=['Exercise Recommendation Plan', 'Gender', 'BMIcase'])
y = dataset['Exercise Recommendation Plan']

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Scale the features
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# (experiment with different values)
n_components = 3 
# Create a PCA object
pca = PCA(n_components=n_components)
# Apply PCA to the training data 3 components
x_train_pca = pca.fit_transform(x_train)
# apply PCA to the testing data 
x_test_pca = pca.transform(x_test)

# Create an instance of the KNeighborsClassifier class
knn = KNN()

# Fit the classifier to the reduced-dimensionality training data
knn.fit(x_train_pca, y_train)

# Make predictions on the PCA-transformed testing data
y_predict = knn.predict(x_test_pca)

# Calculate accuracy
acc = accuracy_score(y_test, y_predict)
print('Accuracy with PCA: ', acc)


# Define the test DataFrame
testDataFrame = pd.DataFrame({
    'Weight':[60,100,71],
    'Height':[150,190,173],
    'BMI':[26.7,27.7,23.7],
    'Age':[21,21,21],
    'gender':[0,1,1],
    'BMIclass':[4,4,1]
})

# Scale the features of the test DataFrame using the same scaler object
test_data_scaled = scaler.transform(testDataFrame)

# Apply PCA transformation to the scaled test data
test_data_pca = pca.transform(test_data_scaled)

# Use the trained KNN classifier to predict the exercise recommendation plan for the test data
predictions = knn.predict(test_data_pca)

# Print the predictions
print("Predictions for test data:")
for i, prediction in enumerate(predictions):
    print(f"Sample {i+1}: Exercise Recommendation Plan {prediction}")