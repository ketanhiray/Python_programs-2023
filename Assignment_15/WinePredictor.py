import pandas as pd
# Scale numerical features
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# Load data from CSV
data = pd.read_csv("WinePredictor.csv")

# Handle missing values if necessary
data.dropna(inplace=True)

# Split data into features (X) and target (y)
X = data.drop("result", axis=1)  # Assuming "result" is the target column
y = data["result"]

# Encode categorical features if needed
X = pd.get_dummies(X)



scaler = StandardScaler()
X = scaler.fit_transform(X)



# Split the data into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Define a sample input for testing
sample_input = [[weather_value, temperature_value]]  # Replace with actual values

# Predict the result
result = knn.predict(sample_input)

# Display the result
if result[0] == 'Yes':
    print("The prediction is 'Yes'.")
else:
    print("The prediction is 'No'.")

from sklearn.metrics import accuracy_score

def CheckAccuracy(X_train, y_train, X_test, y_test, k):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

# Calculate accuracy for different values of K
k_values = [1, 3, 5, 7]  # Adjust as needed
for k in k_values:
    accuracy = CheckAccuracy(X_train, y_train, X_test, y_test, k)
    print(f"Accuracy for K={k}: {accuracy}")
