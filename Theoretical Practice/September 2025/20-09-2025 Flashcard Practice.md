

Machine learning is about giving computer a learning algorithm through which it can learn to do some task that we can't code directly.

ML is about collecting data about some phenomena of nature, and applying an algorithm to it hoping that it could find some generalizable patterns/ regularities that we could use for new scenarios.

--

One could see ML algorithms along several dimensions:
1. Level of supervision during training 
2. Ability to re-learn incementally as new bits of data come in
3. Way to make predictions: model vs similarity based.

--

Level of supervision can be seen as a spectrum of whether or not training data has target labels. 

From that we can list it in such manner:
1. Supervised -- all training data has target labels.
2. Semi-supervised -- some training data has target labels.
3. Self-supervised -- one creates a supervised dataset from the unsupervised (e.g. masking for any picture dataset) (usually used further for transfer learning)
4.  unsupervised -- training data doesn't have target labels. 

--

Ability to learn incrementally (or on the fly) is about either:
1. Batch learning -- learning one time and having to relearn entirely whenever even one training instance is added to the dataset.
2. Online learning -- having the ability to tweak the weights slightly after main training as new instances are added.

--

How predictions are made is either about create a generalizable model based on the training data, that then is used for predictions. Or, using the training data directly to make any further predictions. That is, "memorize by heart" training data and make predictions, say based on the similarity ot it.

--

Test & validation

We hold out some collected data from being used during training to test the model on it, on how well it generalizes to new, unseen instances. 

We could have several models with different hyperparameters and choose the one that score the highest on the training set. 

Yet, this would lead to overfitting the training set, so we use another hold-out set of data to first choose which model to train: validation set. Only then to do the final testing to know how good the model would be.

Of course we could also overfit the validation set, so to counteract it we'd use cross-validation.

--

Regular ML project has 4 steps:
1. Start with understanding the problem space
2. Data: collecting, processing etc.
3. Model: finetuning etc.
4. Deployment: from production to presentation.

--

1. Problem space
Understanding the problem space is crucial and can save you a gazzilion amount of time because you'll know what are the absolute must-haves in a solution, and what are just nice-to haves. Deeply understanding the problem allows you to efficiently and comprehensively search the solution space: you'll likely search broad enough, and kill bad solutions fast enough.

2. Data
As you understand the problem, you'll know what exact nature's phenomena should you collect data about. Data step is about ensuring your data collection methodology is sound and won't lead to obvious errors. That phenomena you collected data on is senseful. That then you processed, selected and scaled the features appropriately to the model you'd try to use.

3. Model
Proper preparation of data should make choosing the model and its optimal hyperparameters a walk in the park. Your model will likely be able to find some useful generalizable patterns for the problem you're trying to solve from the data you collected and processed.

4. Deployment 
Deployment entails everything from preparing the model to be released and used publicly, to consistently monitoring and managing its performance, to presenting (communicating) it and the done work to others.

--

Main risks of any ml project is either poor phenomena to collect data on, poor collecting data methodology, or poor model choice for the collected data (problem at hand). 

--

The main libraries in data analysis/ ml are:

1. NumPy -- it provides a numpy multi-dimensional array data structure which allows to do faster operations with arrays than normal python
2. pandas -- useful data analysis library for python that makes frequent data analysis operations easy; uses series and dataframe data structures.
3. some libraries for data scrapping, but not my focus atm.
4. matplotlib -- allows to visualize graphs in python that are publish-ready.
5. scipy -- library that allows to do basic scientific computations in python.
6. scikit learn -- library for implementing basic ml algorithms
7. pytorch/ tensorflow-keras -- advanced libraries that make it easy to create deep learning applications.


