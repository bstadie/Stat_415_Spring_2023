# Homework 1: Credit Card Fraud Data Wrangling and EDA

This repository contains materials and instructions for Homework 1, in which you will be working with a dataset of credit card transactions to perform exploratory data analysis and data cleaning.

The primary goal of the assignment is to gain insights into the predictors of credit card fraud, which is an important problem in the financial industry. While this assignment focuses on data preparation and analysis, it's worth noting that the insights gained from this work can be used to build predictive models for credit card fraud detection. As such, throughout this assignment, we will be treating the fraud status as our outcome variable, with the understanding that it would serve as the target variable in a predictive model built at a later stage.

## Dataset

To access the dataset for this assignment, go to **Files > Homework Data** on the Canvas course page. The dataset simulates credit card transaction info resembling that of a financial institution's customers. Check out the [Dataset Description](#dataset-description) section below for more details on the variables in the dataset.

Please note that while the dataset looks similar to real transaction data, all its contents are entirely fictional. No identities of people, places, or things were affected while creating this dataset.

## Analysis Instructions

Your analysis should be presented in a clear, visually appealing PDF document, with appropriate visualizations that are properly labeled and annotated to aid in interpretation. You may use any Python libraries or tools that you find helpful, but your document should not include any code. Focus on presenting your findings in a clear, concise, and understandable way.

Please note that the questions provided in the homework assignment are meant to guide your analysis and help you explore the dataset. However, you are not limited to answering these questions alone. Feel free to explore any other aspects of the data that you find interesting or relevant, and include any additional insights or findings in your analysis.

In addition to the PDF document, please also submit a code file that includes all the code you used in your analysis.

Here are the data wrangling and EDA questions we'd like you to address as part of this assignment:

1. Perform preliminary data quality checks, such as identifying duplicated columns and columns with entirely missing data. Discuss any issues or concerns that may arise during the analysis, and consider how these issues could impact the overall quality or validity of the results.

2. Pay close attention to outliers in numerical variables when exploring the data. Discuss methods for detecting outliers, and explain how to handle them. Document your approach to identifying and dealing with outliers as part of your data wrangling process.

3. Identify columns with missing values and determine how to manage them. Justify your approach and reasoning for handling missing values in the dataset.

4. Investigate the time variables in the dataset, and identify any potential issues that may arise when working with them. For example, you may need to convert the variables into a different format or conduct additional cleaning to ensure consistency and usability for analysis.

5. Certain columns in the dataset may require special treatment during data wrangling due to their unique characteristics (e.g., `cardCVV`, `enteredCVV`, `cardLast4Digits`). Explore alternative methods for integrating these variables into your analysis, and document any decisions made during this stage.

6. Analyze the relationship between the columns `cardCVV`, `enteredCVV`, and `cardLast4Digits` and the target variable, `isFraud`, using an appropriate visualization (such as a grouped bar chart). Discuss the insights gained about the relationship between these variables and credit card fraud. Determine if any patterns or trends suggest a relationship between these columns and fraudulent transactions.

7. Visualize the distribution of `transactionAmount` using an appropriate plot, such as a histogram or density plot. Provide a brief analysis of the observed pattern and discuss any insights or trends you can infer from the visualization.

8. Investigate the relationship between `isFraud` and categorical predictors, such as `merchantCategoryCode`, `posEntryMode`, `transactionType`, `posConditionCode`, and `merchantCountryCode`, by creating suitable visualizations like bar charts to display the fraud rate for each category. Describe the patterns you observe and their potential implications for creating a predictive model for fraudulent transactions.

9. Further explore the relationship between `isFraud` and `transactionType` conditioned on `merchantCategoryCode` by generating a grouped bar chart or another suitable visualization to display the fraudulent rates by merchant category code and transaction type. Share any additional insights you have.

10. Construct conditional probability density plots (or other suitable visualizations) for the numerical variables in the dataset to help understand the relationships between these variables and the target variable, `isFraud`. Identify any patterns or trends suggesting a relationship between the numerical variables and fraudulent transactions.

11. Programmatically identify multi-swipe transactions and the conditions under which they occur (e.g., same amount within a short time span). Estimate the percentage of multi-swipe transactions and the percentage of total dollar amount for these transactions, excluding the first "normal" transaction from the count. Were any interesting findings uncovered? 

12. Examine the class imbalance in the `isFraud` outcome variable and discuss the potential implications of these patterns for the development of a predictive model for credit card fraud detection.

13. Implement a method of your choice to mitigate class imbalance in the isFraud outcome variable. Describe the method you used and report its effects on the class distribution. How might addressing class imbalance impact the effectiveness and performance of a predictive model for credit card fraud detection?

## Dataset Description

The following variables are included in the dataset:

- `accountNumber`: a unique identifier for the customer account associated with the transaction
- `customerId`: a unique identifier for the customer associated with the transaction
- `creditLimit`: the maximum amount of credit available to the customer on their account
- `availableMoney`: the amount of credit available to the customer at the time of the transaction
- `transactionDateTime`: the date and time of the transaction
- `transactionAmount`: the amount of the transaction
- `merchantName`: the name of the merchant where the transaction took place
- `acqCountry`: the country where the acquiring bank is located
- `merchantCountryCode`: the country where the merchant is located
- `posEntryMode`: the method used by the customer to enter their payment card information during the transaction
- `posConditionCode`: the condition of the point-of-sale terminal at the time of the transaction
- `merchantCategoryCode`: the category of the merchant where the transaction took place
- `currentExpDate`: the expiration date of the customer's payment card
- `accountOpenDate`: the date the customer's account was opened
- `dateOfLastAddressChange`: the date the customer's address was last updated
- `cardCVV`: the three-digit CVV code on the back of the customer's payment card
- `enteredCVV`: the CVV code entered by the customer during the transaction
- `cardLast4Digits`: the last four digits of the customer's payment card
- `transactionType`: the type of transaction
- `echoBuffer`: an internal variable used by the financial institution
- `currentBalance`: the current balance on the customer's account
- `merchantCity`: the city where the merchant is located
- `merchantState`: the state where the merchant is located
- `merchantZip`: the ZIP code where the merchant is located
- `cardPresent`: whether or not the customer's payment card was present at the time of the transaction
- `posOnPremises`: whether or not the transaction took place on the merchant's premises
- `recurringAuthInd`: whether or not the transaction was a recurring payment
- `expirationDateKeyInMatch`: whether or not the expiration date of the payment card was entered correctly during the transaction
- `isFraud`: whether or not the transaction was fraudulent

