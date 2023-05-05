# Homework 4: Explainability
In this homework, we will consider several methods for explaining the outputs of predictive models. We will focus on attribution methods, which try to weight the relitive importance of inputs with respect to making a prediction. It is important to note there are many methods for considering the interactions between variables. This assignment will not consider those methods, because they get complicated quickly. Instead, we will focus on attribution methods such as LIME, Shapley Values, and SmoothGrad. 




## Dataset

We will use two datasets for this assignment. First, we will consider the Pima Indians Diabetes Database. This tabular database has several health diagnostic measures such as blood pressure, and the goal is to predict if a patient has diabetes. 


## Analysis Instructions

### Tabular Data

Starting with the Pima Indians Diabetes Database. 

1. Investigate the balance of the dataset with respect to the outcome variable? Is the outcome variable of the patient being diabetic undersampled? You always want to check this with medical data. 

2. Run a linear model on this dataset with an L1 penalty. What features does the model select on? 

3. Run a random forest on the dataset using SciKitLearn. After training, this classifier will have a field named `feature_importances_' that you can access. For example, if your trained random forest is called 'rfc' then you can call 'rfc.feature_importances_' to access feature importance. You can also call 'rfc.feature_names_in_' to get feature names. Doing this, what features does the random forest select on? 

4. Use LIME on this dataset to explain the importance of each feature. You may wish to reference this [starter code](https://www.kaggle.com/code/prashant111/explain-your-model-predictions-with-lime)

5. How do LIME, Forest importance, and linear model weighting compare? Do they select similar features? 


### Predictive Modeling on Animal Images

We now turn our attention to the animal classification dataset. 

6. Train a linear model on the animal clasification dataset. Note that you will need to use PyTorch to train this model, since there is no way you'll be able to do the matrix inversion required to run OLS. Here is some [starter code](https://github.com/yunjey/pytorch-tutorial/blob/master/tutorials/01-basics/feedforward_neural_network/main.py)

7. Train a vanilla deep convolutional network on the animal classifcaiton dataset. 

8. Tune your neural network by adding batchnorm, more layers, better activations, improved learning rates, etc. Compare the accuracy of the linear model, the simple conv net, and the tuned conv net. Do this in part by making learning curves, which show the training epoch on the X-axis and the cross entropy loss on the Y-axis. Make a similar curve that shows the training epoch on the X-axis and the model accuracy on the Y-axis. What parameters are important? 


### Feature Atribution on Animal Images

9. Using the starter code [here](google.com), run SmoothGrad on one your convolutional model from step 8. Show a graphic similar to those in Lecture 10, which shows a heatmap of the gradient on the image demonstrating what pixels SmoothGrad is selecting on. See for example [here](https://www.semanticscholar.org/paper/SmoothGrad%3A-removing-noise-by-adding-noise-Smilkov-Thorat/f538dca4def5167a32fbc12107b69a05f0c9d832/figure/2).

10. Similarly, use LIME on images to generate an explanation of what features your convolutional net from step 8 is selecting on. See for example [here](https://raw.githubusercontent.com/marcotcr/lime/master/doc/images/images.png). Starter code is [here](google.com)

That's it! You're done with the HW for this class. 

