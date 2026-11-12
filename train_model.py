
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Step 1: Read dataset
data = pd.read_csv("dataset.csv")

# Step 2: Separate inputs and output
X = data.drop("final_score", axis=1)
y = data["final_score"]

# Step 3: Split training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Create ML model
model = LinearRegression()

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Make predictions
predictions = model.predict(X_test)

# Step 7: Evaluate the model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model Training Completed!")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))

# Step 8: Save trained model
joblib.dump(model, "model.pkl")

print("Model saved successfully!")