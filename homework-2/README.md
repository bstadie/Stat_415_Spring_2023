# Homework 2: Recommender Systems 

This repository contains materials and instructions for Homework 2, in which you will be working with a dataset of restaurant reviews from Evanston IL. You will be tasked with taking this data and using it to build a reccommendation engine. 

The primary goal of the assignment is to gain insight into different systems of reccommendaiton. In particular, we will focus on popularity matching, content based filtering, and collaborative filtering methods. All three of these methods are important problems in the technology and data science communities. Broadly speaking, the outcome variable of interest in this dataset will be the user review score. We will at times do direct predictive modeling methods to predict the user review score from the data. However, much of our analysis will also focus on how to find similar restaurants and similar users across the dataset. Reccommendations can then be made by finding restaurants that are similar to other restaurants the user enjoyed. 




## Dataset

To access the dataset for this assignment, go to **Files > Homework Data** on the Canvas course page. There is one excel file, 'RestaurantReviews.xlsx' , that contains two two sheets. First, `Restaurants.' This sheet cotains information describing each of the restaurants in the dataset. For example, average cost and type of cusine. There is also a natural language description of each restaurant. The second sheet, 'Reviews,'  contains user review scores for the restaurants. These reviews contain review text, dates of the review, and demographic data of the reviewer. This demographic data includes birth year, marital status, and vegetarian preferences. The outcome variable of interest for this assignemnt is the rating, which is a score from 1-5 of the restaurant. 


## Analysis Instructions

Your analysis should be presented in a clear, visually appealing PDF document, with appropriate visualizations that are properly labeled and annotated to aid in interpretation. You may use any Python libraries or tools that you find helpful, but your document should not include any code. Focus on presenting your findings in a clear, concise, and understandable way.

Please note that the questions provided in the homework assignment are meant to guide your analysis. Many of these questions are intended to be open-ended.  

In addition to the PDF document, please also submit a code file that includes all the code you used in your analysis.

The questions we would like you to consider can be broken into five categories: EDA, Popularity matching, content-based filtering, natural language analysis, and collaborative filtering. 

### EDA

1. Import and examine the data. Are there missing values? Do you care? 

2. Make some histograms to try and better understand the data distribution. For example, you might consider making histograms for 'has children', 'vegetarian', 'weight', 'prefered mode of transport', 'average amount spent', and 'Northwestern student'. Also consider making histograms for the 'cusine' in Restaurants.csv. Is the dataset properly balanced? 

Note that you do not need to include all the histograms in your final report, only the interesting ones. 

3. Perform clustering on the user demographic data, using a clustering algorithm of your choice. You will need to transform the categorical variables into one-hot encodings. Are there any obvious clusters of users? 

4. For every cluster, compute the average review score across the entire cluster. Are there any trends? Note, the answer to this question might be 'No. there are no trends,' depending on what clustering algorithm you choose and what hyper-parameters you select. The point of this exercise is to practice clustering real data. 

### Popularity matching 

5. What is the most highly rated restaurant? What is the average review score? What is the median review score? Plot a histogram of review scores. 

6. What restaurant has received the largest quantitiy of reviews? What is the median number of reviews received?

7. Write a simple reccomendation engine wherein a user can input a cusine type and receive a reccommendation based on popularity score. Use this to give reccommendations for Spanish food, Chinese food, Mexican food, and Coffee. 

8. Implement a shrinkage estimator that shrinks reviews back towards the mean score, scaled by the number of reviews a restaurant has received. See the lecture slides for more details. What restaurant benefits the most from this shrinkage estimation? What restaurant is hurt the most by it? Make a plot that demonstrates changes in review scores due to shrinkage estimation. For example, plot the top k-positive and negative changes in a bar chart. Feel free to make an alterative plot if you want. 


### Content based filtering 
9. Using the data in the restaurants.csv table, compute the euclidean distance between every restaurant. Note that you will need to compute a numeric embedding of the categocial variables. Use one-hot encodings. 

10. Repete the previous step, using cosine distance this time. 

11. Write a script that takes a user and returns a reccommendation using content based filtering. This script should take a user, find restaurants the user liked, and then find similar restaurants using euclidean and cosine distances. For one user and one selected restaurant, plot the top reccommendations by the system. Alternatively, you may show a simple table of the top reccommendations. The point is the show your system's output in some way. I don't care how you do it. 


### Natural language analysis 

12. Consider the 'brief description' column of the Restaurants dataset. Augement this description by attaching the restaurant's cusine type to the end of the description.  For example, with Tapas Barcelona the description is: 'Festive, warm space known for Spanish small plates is adorned with colorful modern art & posters.' The Cusine is 'Spanish.' The augemented description would thus be: 'Festive, warm space known for Spanish small plates is adorned with colorful modern art & posters. Spanish' Name this variable "Augmented Description." 


13. Compute the Jaccard matrix using the elements of Augemented Description. In the Jaccard matrix, entry d_ij should be the Jaccard distance between restuarant i's augmented description and restaurant j's augmented descirpiton.


15. Write code that takes as input a word. The code should take this word and compute the TF-IDF score for each restaurant's Augmented Description. Using this function, which restaurant has the highest TF-IDF score for the word 'cozy?' What about for the word 'Chinese?' 

15. Make a list of the 100 most popular words in the Augmented Description column. Write two nested for loops. First, loop over each of the restaurant descriptions. For each of the restaurant descriptions, also loop over every word in the 100 most popular words list. Compute the TF-IDF score for that word. The result should be 64 TF-IDF vectors of length 100, one for each restaurant. 

16. Similar to step 13, compute the TF-IDF distance matrix. In this matrix, d_ij is the distance between the TF-IDF vectors for restaurants i and j. 

17. Using BERT or Word2Vec, embed the restaurant descriptions into a vectorized representation. Similar to steps 13 and 16, compute an Embedding-Distance matrix, where d_ij is the distance between embedding vectors of restaurants i and j. 

18. Come up with a methd of comparing the reccommendations made by Jaccard distance, TF-IDF distance, and BERT/Word2Vec distance. Expalin why this method makes sense. What distance metric does the best under your proposed compairson method?

### Collaborative Filtering 
19. Using the demographic data in Reviews.csv, form a vector. This vector should include numeric representations of traits such as 'has children', 'vegetarian', 'weight', 'prefered mode of transport', 'average amount spent', and 'Northwestern student.' Form this vector for every reviewer. Watch out for double counting. Many reviewers have reviewed multiple restaurants. We only want unique reviewers. 

20. Using the vectors from the previous step, write a function that takes a user and computes the distance from that user to every other user. Use this function to create a reccommendation algorithm that takes a user and outputs a reccommendation made by a similar user.

21. Rather than finding users that are similar in terms of demographics, we want to find users that gave similar reviews. Select a user j who has given at least 4 reviews. To find users that have given the most similar reviews, you will want to form a 64 dimensioanl vector where entry i is the user's review of restaurant i. This vector will have many blank entries. What should you use to fill in these blanks? Hint: probably not 0. 

22. Using step 21, compute the 64-dimensional review vector for every user. Now, write code that takes a user and finds other users with similar review vectors. 

23. Compare the average quality of reccommendations made by steps 22 and 20. 

24. For every user, make a 'user profile' vector that contains both the user's demographic data and the user's review vector. Similar to step 3, perform clustering on this data. Are there any trends in these clusters? 

Note that you could use the results from step 24 to make reccommendations by finding a user's cluster and then reccommending well-liked restaurants within that cluster. However, we will not ask you to do this on this homework. But be aware this technique is extremely common in real reccommender systems. 

### Predictive modeling 

25. Write a linear model that takes demographic data, along with the cusine type for a restaurant, and tries to predict the restaurant score. 

26. Evaluate your linear model using a train/test split. 

27. Add an L1 penalty to your lienar regression model. Compare the test-set results with a standard lienar model. What features are selected on by this L1 model? In other words, when are the weights of the linear model large? When are they small or negative? Are certain demographics more predictive of review score?

28. Consider the column 'Review Text.' Embed the review text into a vector with one of Word2Vec, BERT, or TF-IDF. Using this embedding vector, try to predict the review score with a linear model. 

29. Repete step 25, only this time include the vector for the embedded review text from step 28. Does including the embdeed review text improve the predictive power of the model? Explicitly compare your resutls at this step to the results from step 25. 

30. Finally, we want to know what demographic features are useful for predicting coffee scores. There are 3 coffee shops in the dataset. For these three restaurants only, write a linear model that takes demographic data and predicts the score. 

31. Examine the weights produced by the linear model in step 29. What demographic features are selected on? In other words, when are the weights of the linear model large? When are they small or negative? Do certain groups of people like or dislike coffee? 


### Final 

32. Find at least 1 interesting thing in the dataset and write about it. For example, find a single user that hates every restaurant they review, or a trend among Northwestern students. When I did this exercise, I found 18 interesting trends in the data with minimial effort. So there should be plenty of things to find. 





