# Imports for data import/manipulation, numerical computing, predictive modeling, and visualization

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import(
     confusion_matrix,
     classification_report,
     roc_auc_score,
     roc_curve
)

df = pd.read_csv("heart_disease_data.csv")



# View first 5 rows of dataset to verify if dataset imported correctly

print(df.head())


# Check size of dataset

print(df.shape)


# Check data types

df.info()


# Check for and drop nulls

df = df.dropna()
print(df.isnull().sum())


# Since logistic regression require binary, we convert values to 1s (yes) and 0s (no)

df["PhysicalActivity"] = df["PhysicalActivity"].map({
	"Yes" : 1,
	"No" : 0,
})


# One-hot coding for categorical variables

df = pd.get_dummies(
	df,
	columns=[
		"Smoking",
		"Diabetic",
		"AgeCategory",
		"Sex",
		"GenHealth"
	],
	drop_first = True    # Prevents multicollinearity in the regression model
)


# Convert HeartDisease

df["HeartDisease"] = df["HeartDisease"].map({
	"Yes": 1,
	"No": 0
})


# Define y as target variable

y = df["HeartDisease"]


# Define x as everything except target variable (features)

X = df.drop("HeartDisease", axis = 1)


# ML Train/Test Split for predictive analysis

X_train, X_test, y_train, y_test = train_test_split(
	X,
	y,
	test_size = 0.20,
	random_state = 42

)


# Implement logistic regression model

model = LogisticRegression(max_iter = 1000)

model.fit(X_train, y_train)


# Generate predictions

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]


# Evaluate predictions

	# Confusion Matrix
print(confusion_matrix(y_test, y_pred))

	# Classification Report
print(classification_report(y_test, y_pred))

	# ROC-AUC
print("ROC-AUC:", roc_auc_score(y_test, y_prob))


# Examine feature importance (Negative coefficients suggest an
# association with lower predicted risk of heart disease)

coefficients = pd.DataFrame({
	"Feature": X.columns,
	"Coefficient": model.coef_[0]
})

print(
	coefficients.sort_values(
	by = "Coefficient",
	ascending = False
	)
)

# Create readable labels for plotting only
df["PhysicalActivity_Label"] = df["PhysicalActivity"].map({
    1: "Physical Activity",
    0: "No Physical Activity"
})


# Visualizations of key findings

	# Heart Disease by Physical Activity
sns.barplot(x="PhysicalActivity_Label", y="HeartDisease", data=df)
plt.title("Heart Disease Rate by Physical Activity")
plt.xlabel("Physical Activity")
plt.ylabel("Heart Disease Rate")
plt.show()


	# ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_prob)
auc = roc_auc_score(y_test, y_prob)

plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {auc:.2f})")
plt.plot([0, 1], [0, 1], linestyle="--", label="Random Classifier")

plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()

plt.show()
