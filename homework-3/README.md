# Homework 3: Predictive Modeling

This homework is much more simple than the first two. We will be looking at some predictive modeling techniques. Your primary goal will be to compare the performance random forrests, linear models, and deep models. 




## Dataset

The dataset for this assignment consists of US Demographic data. There are two files. First, raw_state_data_drunk_driving.csv. This dataset has various demographic measures across all 50 States in the US. This data is mostly taken from the US census. For example, percentage of rural population, median income, total number of car accidents, and obesity rate. The target outcome variable in this dataset is percentage of fatal accidents involving drunk driving. 

Unfortauntely, making predictions on a dataset with only 50 points is quite difficult. Thus, we will also consider a second dataset, census-tracts-dataset.csv. This dataset uses clustered census tracts to form patches of the country that mimic US states in their demographic distributions. Bootstrapping in this way, we are able to bring together 20,000 datapoints that resemble the underlying distribution of the 50 States in the US. I have handled missing values for you in this dataset, at times using imputation. Thus, any strange occurances, such as demographic percentages totaling over 100 when summed, should be thought of as a byproduct of the bootstrap process. You should not worry about this for your analysis. You're welcome to "fix" this with softmax normalization, but it shouldn't impact your final results and you won't get any credit for doing so. 


## Analysis Instructions

### Linear Models

Starting with the census-tracts-dataset.csv. 
The target variables is percentage of drunk driving accidents. Be sure to set aside a validation set. 

1. Train a linear model that takes all of the columns in the dataset and tries to predict the percentage of drunk driving accidents. [Note, you don't want to use the ID column in this analysis]. Make a histogram of the drunk driving percentage in the dataset. Compare this histogram to the predictions made by your linear model. 

2. Make a histogram of the linear model errors. How are they distributed? 

3. Tune your linear model with L1 and L2 regularization. Does this improve the MSE at all? It might not. 

### Random Forrest 

5. Train a random forrest model on the same dataset. Report the MSE. 

6. Make a histogram of the forrest outputs vs the true data distribution. How do they compare? You can also consider making overlapping density plots instead of histograms, if you prefer. 

7. Tune your random forrest. Can you improve it? Are any parameters important? 

### Neural Networks 

8. Using PyTorch, train a 3 layer neural network with Sigmoid activations on this dataset. Report the MSE. You might find [this resource](https://github.com/yunjey/pytorch-tutorial/blob/master/tutorials/01-basics/feedforward_neural_network/main.py) helpful.

9. Look at the distribution of outputs of your neural network. Compare it to the true distribution. Neural networks are well known to converge to the mean output. Is this happening to you? If it does happen, try to retrain your net from scratch. Is it a consistent problem?

10. Tune your net by adjusting the optimizer, the number of layers in the net, and the activation functions you use. If you want, you can also try adding dropout and regularization, although this might not help much. Are you able to make any improvements? 

### Transfer Learning 
We now turn our attention to raw_state_data_drunk_driving.csv. 


11. Train a linear model, a neural net, and a random forrest on the data from raw_state_data_drunk_driving.csv. How do the results compare to the results you achieved on the larger dataset? 

12. Try your best to achieve some transfer learning. Take a linear model and train it on the data from census-tracts-dataset.csv. Then, take that trained linear model and try to make predictions on the data from raw_state_data_drunk_driving.csv. Does your trained linear model transfer? 

13. Let's try to achieve some transfer via training. First, train a neural network on census-tracts-dataset.csv. Then, once this first training is done, fine-tune the network by training on the data from raw_state_data_drunk_driving.csv. Note, you might want to only train on raw_state_data_drunk_driving.csv for a few iterations, since it is small and you risk overfitting if you train for a long time. How do your results compare to the results from 11? Does transfer help at all?

Note that actually achieving transfer is rather difficult. You won't be penalized if you can't get this section to work fully, so long as you make an honest attempt. I had to use a 9 layer neural network to get it to work reliably. 

### Visualization 

14. Construct a Choropleth map of the US States. States should be colored by the percentage of drunk driving accidents in that state. 

15. Construct a second Choropleth map. This time, pick one of your predictive models and plot its errors on the map. Each state should be color coded by the magnitude of your estimator's error. What states are the easiest to predict? What states are the hardest? 
