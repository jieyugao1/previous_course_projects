## Supervised Learning

In a supervised leanring task, the data sample would contain a target attribute y, also known as ground truth. The data with a target attribute is often called "labeled" data. 

Example:
    
    1. Classification. 
    2. Regression. 

Two common cases where the generated model does not fit well the data: **underfitting** and **overfitting**. Both cases imply that the model does not generalized well to the unseen data. 

    1. An underfitting model is the one that does not fit well with the training data, i.e. significantly deviated from the ground truth. One of the causes of underfitting could be that the model is over-simplified for the data, therefore it is not capable to capture the hidden relationship within the data. 
    2. An overfitting model is the one that fits well with the training data, i.e. little or no error, however it does not generalized well to the unseen data.Contrary to the case of underfitting, an over-complicated model that is able to fit every bit of the data, would fall into the traps of noises and errors. One common solution is **regularization**, i.e. penalizing the model that is over-complicated so that the algorithm is steered to generate a less complicated model while fitting the data.



## Unsupervised Learning

In contrary tot he supervised learning task, we do not have the ground truth in an unsupervised learning task. One is expected to learn the underlying patterns or rules from the data, without having the predefined ground trugh as the benchmark. 

Examples:
    
    1. Clustering: given a data set, one can cluster the samples into groups, based ont eh similarities among the samples within the data set. 
    2. Association: given a data set, the asosciation task is to uncover the hidden association patterns among the attributes of a sample. 

## Semi-supervised Learning

By combining both the supervised and unsupervised learning in a data set with few labels, one could exploit the data set to a better extend and obtain a better result than just applying each of them individually.

For example, one would like to predict the label of images, but only 10% of the images are labeled. By applying supervised learning, we train a model with the labeled data, then we apply the model to predict the unlabeled data. 

A better strategy could be to first cluster the images into groups (unsupervised learning), and then apply the supervised learning algorithm on each of the groups individually. The unsupervised learning in the first stage could help us to narrow down the scope of learning so that the supervised learning in the second stage could obtain better accuracy.


