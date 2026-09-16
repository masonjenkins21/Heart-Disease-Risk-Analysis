# Physical Activity and Heart Disease Risk Analysis

## Project Overview

### Research Question

To what extent is physical activity associated with heart disease risk after controlling for demographic, lifestyle, and health-related factors?

Heart disease remains a leading cause of death in the United States. This project evaluates whether physical activity is associated with a reduced likelihood of heart disease using data from the CDC Behavioral Risk Factor Surveillance System (BRFSS).

### Dataset

The dataset was obtained from the CDC BRFSS and accessed through Kaggle (Centers for Disease Control and Prevention, n.d.; Pytlak, n.d.). The dataset contains hundreds of thousands of survey responses and includes variables related to heart disease, physical activity, age, sex, smoking status, diabetes status, general health, BMI, and sleep habits.

Because HeartDisease is a binary outcome (Yes/No), the project was framed as a binary classification problem.

## Tools and Technologies

- PostgreSQL  
- DBeaver  
- Python  
- Pandas  
- Scikit-learn  
- Matplotlib  
- Seaborn  

## Data Preparation

The dataset was imported into PostgreSQL and explored using SQL queries.

Data preparation included:

- Removing records containing missing values  
- Selecting variables relevant to the research question  
- Converting HeartDisease and PhysicalActivity into binary variables (1/0)  
- Applying one-hot encoding to categorical variables  
- Splitting the data into training and testing datasets  

## Methodology

A logistic regression model was developed to evaluate whether physical activity predicts heart disease while controlling for demographic and health-related variables.

Model evaluation included:

- Train-test split (80/20)  
- Confusion Matrix  
- Classification Report  
- ROC Curve  
- ROC-AUC Score  

## Results

### Confusion Matrix

| Actual / Predicted | No Heart Disease | Heart Disease |
|--------------------|------------------|--------------|
| No Heart Disease   | 58,042           | 325          |
| Heart Disease      | 5,278            | 314          |

### Classification Metrics

- Accuracy: 0.91  
- Precision (Heart Disease): 0.49  
- Recall (Heart Disease): 0.06  
- F1 Score (Heart Disease): 0.10  
- ROC-AUC: 0.82  

### Physical Activity Coefficient

- Coefficient: -0.04  

The model achieved an ROC-AUC score of 0.82, exceeding the project benchmark of 0.70.

The negative coefficient for PhysicalActivity indicates that engaging in physical activity was associated with a lower predicted likelihood of heart disease after controlling for other variables.

## Visualizations

### Heart Disease Rate by Physical Activity

A Seaborn bar chart was used to compare heart disease rates between individuals who reported engaging in physical activity and those who did not.

### ROC Curve

A Matplotlib ROC curve was used to evaluate model performance and visualize the ROC-AUC score.

## Conclusion

The analysis supports the hypothesis that physical activity is associated with a reduced likelihood of heart disease.

Although the model struggled to identify all positive cases due to class imbalance, it demonstrated strong overall discrimination with an ROC-AUC score of 0.82.

These findings are consistent with an association between physical activity and lower reported heart disease risk after accounting for the included demographic, lifestyle, and health-related variables. Because the analysis uses observational BRFSS data, the results should not be interpreted as establishing a causal effect.

## Repository Contents

- SQL scripts used for exploratory data analysis and preprocessing  
- Python code used for modeling and evaluation  
- Model outputs and performance metrics  
- Visualizations  

## References

Centers for Disease Control and Prevention. (n.d.). Behavioral Risk Factor Surveillance System (BRFSS). https://www.cdc.gov/brfss/index.html

Kamil Pytlak. (n.d.). Personal key indicators of heart disease [Data set]. Kaggle. https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease