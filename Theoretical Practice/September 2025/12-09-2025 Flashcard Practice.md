training supervision is about whether or not training data has target labels attached to it. It is not that binary, rather more of a scale:
    supervised -- all training data had targets
    non-supervised -- no targets
    semi-supervised -- some training instances had targets
    self-supervised -- making a supervised dataset from an unsupervised one, say by masking 

--

testing and validations are for checking the generalizability of the model. We need to use validation set because we might overfit to the testing one when choosing the model and hyperparameters. And we might overfit the validation set so we should use crossvalidation.    

--

ML projects are about capturing some phenomena of nature and running an algorithm (model) on it to find some useful pattern that could be applied to cases outside of collected data.

Thus what can go wrong is either poor choice of phenomena (say white noise), poor data collection, or poor model that can't find the pattern.

--

online learning is about models being able to work when adding incremental training data and slightly changing their model. While batch learning is starting from scratch and retraining the model even if one new training instance is added.

--

While the main value of python as a programming language is that it's syntax is simple, it actually unlocks an even bigger value of having strong library ecosystem which also makes language very powerful (as simple syntax allows more people to learn it and more people means more possibility for niches and adding functionality by someone).

The important libraries for data science and ml are:

1. numpy which provides an ndarray which is a multideminsional array that allows to do faster and more efficient array computations than normal python arrays.
2. pands which allows to manipulate complex data (tabular or relational) in a simple way. It was optimized for "data science". Has its own data structures of series and dataframe.
3. matplotlib -- does great plots of data that are of publishable quality
4. sklearn does basic ml functionality 
5. pytorch and tensorflow (& keras!) are libraries focused on deep learning and more complex operations on matrices and possibly spreading the load between many gpus/tpus

