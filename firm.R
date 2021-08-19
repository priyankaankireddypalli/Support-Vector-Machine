# 1
library(readr)
# Importing the Dataset
Test <- read.csv('C:\\Users\\WIN10\\Desktop\\LEARNING\\DS\\Black Box (SVM)\\SalaryData_Test (1).csv', stringsAsFactors = TRUE)
Train <- read.csv('C:\\Users\\WIN10\\Desktop\\LEARNING\\DS\\Black Box (SVM)\\SalaryData_Train (1).csv', stringsAsFactors = TRUE)
summary(Test)
summary(Train)
# Training a model on the data
# Begin by training a simple linear SVM
install.packages("kernlab")
library(kernlab)
salary_classifier <- ksvm(Salary ~ ., data = salary_Train, kernel = "vanilladot")
# Evaluating model performance ----

# Predictions on testing dataset
salary_predictions <- predict(salary_classifier, salary_Test)
table(salary_predictions, salary_Test$Salary)
agreement <- salary_predictions == salary_Test$Salary
table(agreement)
prop.table(table(agreement))

## Improving model performance ----
salary_classifier_rbf <- ksvm(Salary ~ ., data = salary_Train, kernel = "rbfdot")
salary_predictions_rbf <- predict(salary_classifier_rbf, salary_Test)
agreement_rbf <- salary_predictions_rbf == salary_Test$Salary
table(agreement_rbf)
prop.table(table(agreement_rbf))
