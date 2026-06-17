-- Get total row count for dataset

SELECT COUNT(*)
FROM Heart_Disease_Data;


-- Show first 10 rows of dataset

SELECT *
FROM Heart_Disease_Data
LIMIT 10;


-- Explore HeartDisease and check expected values (yes or no)

SELECT "HeartDisease", 
       COUNT(*) as "Count"
FROM Heart_Disease_Data
GROUP BY "HeartDisease";


-- Explore PhysicalActivity and check expected values (yes or no)

SELECT "PhysicalActivity", 
       COUNT(*) as "Count"
FROM Heart_Disease_Data
GROUP BY "PhysicalActivity";


-- Check for missing values to evaluate completeness of data

SELECT COUNT(*) AS "TotalRows",
       COUNT("BMI") AS "BMI_NotNull",
       COUNT("HeartDisease") AS "Heart_Disease_NotNull",
       COUNT("PhysicalActivity") AS "PhysicalActivity_NotNull"
FROM Heart_Disease_Data;


-- Get number of cases and percentages for reported physical activity vs heart disease statuses

SELECT "PhysicalActivity", 
       COUNT(*) as "TotalPeople",
       SUM(CASE WHEN "HeartDisease" = 'Yes' THEN 1 ELSE 0 END) AS  "HeartDiseaseCases",
       ROUND(
             100.0 * SUM(CASE WHEN "HeartDisease" = 'Yes' THEN 1 ELSE 0 END)
             /COUNT(*), 
             2
       ) as "Heart_Disease_Rate"
FROM Heart_Disease_Data
GROUP BY "PhysicalActivity"
ORDER BY "PhysicalActivity";


-- Investigate important control variables

SELECT "Smoking",
       COUNT(*) as "Count"
FROM Heart_Disease_Data
GROUP BY "Smoking";

SELECT "Diabetic",
       COUNT(*) as "Count"
FROM Heart_Disease_Data
GROUP BY "Diabetic";

SELECT "AgeCategory",
       COUNT(*) as "Count"
FROM Heart_Disease_Data
GROUP BY "AgeCategory"
ORDER BY "AgeCategory";


-- Check for class imbalance

SELECT
    "HeartDisease",
    COUNT(*) AS "Count",
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS "Percentage"
FROM Heart_Disease_Data
GROUP BY "HeartDisease";


-- Create the dataset to be used for modeling

SELECT "HeartDisease",
       "PhysicalActivity",
       "BMI",
       "Smoking",
       "Diabetic",
       "AgeCategory",
       "Sex",
       "SleepTime",
       "GenHealth"
From Heart_Disease_Data;

