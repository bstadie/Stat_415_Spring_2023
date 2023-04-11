# Homework 2: Reccommender Systems 

This repository contains materials and instructions for Homework 2, in which you will be working with a dataset of restaurant reviews from Evanston IL. You will be tasked with taking this data and using it to build a reccommendation engine. 

The primary goal of the assignment is to gain insight into different systems of reccommendaiton. In particular, we will focus on popularity matching, content based filtering, and collaborative filtering methods. All three of these methods are important problems in the technology and data science communities. Broadly speaking, the outcome variable of interest in this dataset will be the user review score. We will at times do direct predictive modeling methods to predict the user review score from the data. However, much of our analysis will also focus on how to find similar restaurants and similar users across the dataset. Reccommendations can then be made by finding restaurants that are similar to other restaurants the user enjoyed. 




## Dataset

To access the dataset for this assignment, go to **Files > Homework Data** on the Canvas course page. There are two datasets. First, `Restaurants.csv' This file cotains information describing each of the restaurants in the dataset. For example, average cost and type of cusine. There is also a natural language description of each restaurant. The second file, 'Reviews.csv' contains user review scores for the restaurants. These reviews contain review text, dates of the review, and demographic data of the reviewer. This demographic data includes birth year, marital status, and vegetarian preferences. The outcome variable of interest for this assignemnt is the rating, which is a score from 1-5 of the restaurant. 


## Analysis Instructions

Your analysis should be presented in a clear, visually appealing PDF document, with appropriate visualizations that are properly labeled and annotated to aid in interpretation. You may use any Python libraries or tools that you find helpful, but your document should not include any code. Focus on presenting your findings in a clear, concise, and understandable way.

Please note that the questions provided in the homework assignment are meant to guide your analysis. Many of these questions are intended to be open-ended.  

In addition to the PDF document, please also submit a code file that includes all the code you used in your analysis.

The questions we would like you to consider can be broken into five categories: EDA, Popularity matching, content-based filtering, natural language analysis, and collaborative filtering. 

### EDA

1. Import and examine the data. Are there missing values? Do you care? 

2. Make some histograms to try and better understand the data distribution. For example, you might consider making histograms for has children, vegetarian, and weight, prefered mode of transport, average amount spent, and Northwestern student. Also consider making histograms for the restaurant types. Is the dataset properly balanced? 

3. Perform clustering on the user demographic data, using a clustering algorithm of your choice. You will need to transform the categorical variables into one-hot encodings. Are there any obvious clusters of users? 

4. Select 1 or 2 restaurants. For every cluster, compute the average review score of the chosen restaurant across users in the selected cluster. Are there any trends? Note, the answer to this question might be 'no there are no trends,' depending on what clustering algorithm you use and what restaurant you select.

### Popularity matching 

3. What is the most highly rated restaurant? What is the average review score? What is the median review score? Plot a histogram of review scores. 

4. What restaurant has received the largest quantitiy of reviews? What is the median number of reviews received?

5. What is the average number of reviews? 

6. Write a simple reccomendation engine wherein a user can input a cusine type and receive a reccommendation. Use this to give reccommendations for Spanish food, Chinese food, Mexican food, and Coffee. 

7. Implement a shrinkage estimator that shrinks reviews back towards the mean score, scaled by the number of reviews a restaurant has received. See the lecture slides for more details. What restaurant benefits the most from this shrinkage estimation? What benefit is hurt the most by it? 


### Content based filtering 



