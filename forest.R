# 2
library(readr)
# Importing the Dataset
forestfires <- read.csv('C:\\Users\\WIN10\\Desktop\\LEARNING\\DS\\Black Box (SVM)\\forestfires.csv', stringsAsFactors = TRUE)
summary(forestfires)
# Splitting the Data into train and test data
forestfires_train <- forestfires[1:256, ]
forestfires_test  <- forestfires[257:517, ]

# Training a model on the data 
# Begin by training a simple linear SVM
library(kernlab)
forestfires_classifier <- ksvm(size_category ~ ., data = forestfires_train, kernel = "vanilladot")

## Evaluating model performance ----
# predictions on testing dataset
forestfires_predictions <- predict(forestfires_classifier, forestfires_test)
table(forestfires_predictions, forestfires_test$size_category)
agreement <- forestfires_predictions == forestfires_test$size_category
table(agreement)
prop.table(table(agreement))

## Improving model performance ----
forestfires_classifier_rbf <- ksvm(size_category ~ ., data = forestfires_train, kernel = "rbfdot")
forestfires_predictions_rbf <- predict(forestfires_classifier_rbf, forestfires_test)
agreement_rbf <- forestfires_predictions_rbf == forestfires_test$size_category
table(agreement_rbf)
prop.table(table(agreement_rbf))
