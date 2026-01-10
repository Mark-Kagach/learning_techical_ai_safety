# Goal
The goal for today is to practice explaining and applying learned concepts in chapter 6 of HOMLP. This is all about ensemble learning.

Afterwards, I want to go through past chapter exercises. Then re-explain main parts of ML.

# Debrief
1. Need to practice more recalling all ensemble methods, also hard, soft voting.
2. Random forest is a bagging method. Its randomness comes from both bagging and random input feature selection. Extra-trees add another layer of randomness by picking decision thresholds randomly.
3. OOB is 37%, not 39%.
4. Learned about adaboost using decision stumps by default, and that the idea is to use weak learners. 

# HOMLP Chapter 6 Exercises
1. If you have trained five different models on the exact same training data, and they all achieve 95% precision, is there any chance that you can combine these models to get better results? If so, how? If not, why? 

In training models on the same data you risk them doing the same errors.
Yet, you have trained 5 different models, so it is possible they are committing different errors. 
All models having 95% precision doesn't say whether the 5% errors are the same or different between models.
My guess is that training different models would make them do different errors, thus combining them in an ensemble model might lead to better performance as more types of errors will be covered.

🟢 => Generally correct. Make emphasis on training very different models.

--
2. What is the difference between hard and soft voting classifiers?

I don't recall how soft voting classifiers work. Yet I do remember that hard voting classifiers are just about picking option that had majority of votes. Can soft voting be about any other voting method that doesn't include majority?

> A hard voting classifier just counts the votes of each classifier in the ensemble and picks the class that gets the most votes. A soft voting classifier computes the average estimated class probability for each class and picks the class with the highest probability. This gives high-confidence votes more weight and often performs better, but it works only if every classifier is able to estimate class probabilities (e.g., for the SVM classifiers in Scikit-Learn you must set probability=True).

🟡 Got entirely wrong soft voting classifier. But method makes a lot of sense.

--
3. Is it possible to speed up training of a bagging ensemble by distributing it across multiple servers? What about pasting ensembles, boosting ensembles, random forests, or stacking ensembles? 

To answer that I need to remind myself what each one is. And before I do that I have to confess that I poorly remember them -- need more practice. 

- Random forest is an ensemble of decision trees. => ❓ Why then they are called random? Because we can introduce randomness by picking \sqrt n of input features and sometimes randomly pick thresholds for decision tree nodes?
- Stacking is when instead of simple voting functions like hard or soft we train model to do such aggregation.
- Gradient boosting is when we train first base model, like decision tree, and then all the rest ones to predict its residual errors recursively. Models predicting errors can be called correcting predictors (is it the name though?).
- Histogram based gradient boosting is best for huge datasets as it buckets continuous data, default 255 buckets, and then works on those histograms which significantly speeds up the training process, although not as accurate.
- is bagging when we randomly pick training data for each base model? And then we have out-of-bag examples for each base model which is around 39% of all training examples, and then we can do out-of-bag score (validation score) using it?
- and pasting is when we ... aha right. Both bagging and pasting randomly pick examples from training data for base models. Yet bagging does replacement, while pasting doesn't. Replacement is when you put back the chosen example into the dataset for the next pick. Think putting back chosen playing card from the deck, so you might pick it again.

❓Then how methods where you take all the training examples for base models is called?

And what's boosting... Right. Boosting is when you have weights on training examples. First base models have all weights the same, yet the next base models has higher weights for training examples that first one got wrong, so it pays more attention to them trying to get them right. You also can use learning rate to control the effect of next models, this is called shrinkage.

Now let's comeback to our question. It is possible to do parallel training for ensemble methods that don't require sequential training one after another. Methods that do sequential trainings are: boosting ensemble, gradient boosting, and histogram gradient boosting.

So all the rest, like random forests, stacking ensemble, pasting and bagging ensembles can be speed up by parallel training.
❓ Though isn't stacking ensemble just different method of voting, and we might use it for gradient boosting so we can't speed it up?

> It is quite possible to speed up training of a bagging ensemble by distributing it across multiple servers, since each predictor in the ensemble is independent of the others. The same goes for pasting ensembles and Random Forests, for the same reason. However, each predictor in a boosting ensemble is built based on the previous predictor, so training is necessarily sequential, and you will not gain anything by distributing training across multiple servers. Regarding stacking ensembles, all the predictors in a given layer are independent of each other, so they can be trained in parallel on multiple servers. However, the predictors in one layer can only be trained after the predictors in the previous layer have all been trained.

🟡 => Was hard recalling all the methods, need more practice to remember. Got correct which methods can be sequentialized and which cannot be. There's nuance in stacking ensemble I don't understand.
How accurately I got ensemble methods:
1. Bagging/ Pasting Ensemble -- got right the replacement part, but entirely missed the main idea of these methods: training same model class (say decision trees) on different training data. 
2. Stacked Ensemble -- missed what it is about. Indeed, here we train different model classes on the same training data, but then instead of simple voting functions like hard or soft, we use another ml model to aggregate them. We can do these aggregations with several levels.
3. Random forests -- partially got wrong. Yes it is a collection of decision trees, that's why it is a forest, but we need to introduce randomness so we don't get just a bunch of same decision trees. We do that either by giving different input features, different training examples or even decision thresholds. And remember this is bagging-type of method.
4. Boosting methods -- got it right.

--
4. What is the benefit of out-of-bag evaluation? 

That we use all of the training examples?... OOB evaluation is taking the 39% of training examples that haven't been picked for each corresponding base model and using them as validation set (not test set, which we should have splitted prior). Not sure what other benefit there's to it.

> With out-of-bag evaluation, each predictor in a bagging ensemble is evaluated using instances that it was not trained on (they were held out). This makes it possible to have a fairly unbiased evaluation of the ensemble without the need for an additional validation set. Thus, you have more instances available for training, and your ensemble can perform slightly better.

🟢 Guess I got it.

--
5. What makes extra-trees ensembles more random than regular random forests? How can this extra randomness help? Are extra-trees classifiers slower or faster than regular random forests? 

Random forests are about different \sqrt n of input features used for decision tree nodes. Extra-trees as I recall is about using random decision thresholds. Extra-trees are faster because finding appropriate decision threshold is the most compute intensive part of making decision trees. Decision trees are prone to overfitting (high variance) because it is a powerful model. Adding randomness makes it less like to do so. Because afterwards we combine those trees in an ensemble we don't need to worry about bias (underfitting).

>  When you are growing a tree in a Random Forest, only a random subset of the features is considered for splitting at each node. This is true as well for Extra-Trees, but they go one step further: rather than searching for the best possible thresholds, like regular Decision Trees do, they use random thresholds for each feature. This extra randomness acts like a form of regularization: if a Random Forest overfits the training data, Extra-Trees might perform better. Moreover, since Extra-Trees don't search for the best possible thresholds, they are much faster to train than Random Forests. However, they are neither faster nor slower than Random Forests when making predictions.

❓Do random forests use different training examples? Are they bagging methods? => Yes they do that too. 

🟢 Got it right, had to clarify whether random forest are bagging.

--
6. If your AdaBoost ensemble underfits the training data, which hyperparameters should you tweak, and how? 

Let's start with recalling what adaboost is. Well boost means it must be about boosting :) right, it adaboost is about weighted training examples, and recursively increasing them for examples that past models got wrong, while also controlling how much these models impact the final prediction with learning rate (shrinkage).

So, underfitting means the model is too simple. The problem is I don't remember if adaboost uses specific base models like decision trees, or whatever goes. ❓ Regardless, I presume you put learning rate too low, so your non-first trees are not impacting the prediction enough. So you need to increase your learning rate.

> If your AdaBoost ensemble underfits the training data, you can try increasing the number of estimators or reducing the regularization hyperparameters of the base estimator. You may also try slightly increasing the learning rate.

🟡 Partially got right. Other answers make sense, didn't get I needed to answer with several ones. Lear

--
7. If your gradient boosting ensemble overfits the training set, should you increase or decrease the learning rate? 

Gradient boosting is about training models after the first one on the residual errors of the previous ones. If it overfits then it has memorized too well training data, this is because correcting models are having too much impact on the final prediction because they minimize the residual error to nearly zero. So, we need to decrease their effect, which means decreasing learning rate.

> If your Gradient Boosting ensemble overfits the training set, you should try decreasing the learning rate. You could also use early stopping to find the right number of predictors (you probably have too many).

🟢 got it right. Good addition about number of predictors, forgot about early stopping.

--
8. Load the MNIST dataset (introduced in Chapter 3), and split it into a training set, a validation set, and a test set (e.g., use 50,000 instances for training, 10,000 for validation, and 10,000 for testing). Then train various classifiers, such as a random forest classifier, an extra-trees classifier, and an SVM classifier. Next, try to combine them into an ensemble that outperforms each individual classifier on the validation set, using soft or hard voting. Once you have found one, try it on the test set. How much better does it perform compared to the individual classifiers? 

--
9. Run the individual classifiers from the previous exercise to make predictions on the validation set, and create a new training set with the resulting predictions: each training instance is a vector containing the set of predictions from all your classifiers for an image, and the target is the image’s class. Train a classifier on this new training set. Congratulations—you have just trained a blender, and together with the classifiers it forms a stacking ensemble! Now evaluate the ensemble on the test set. For each image in the test set, make predictions with all your classifiers, then feed the predictions to the blender to get the ensemble’s predictions. How does it compare to the voting classifier you trained earlier? Now try again using a StackingClassifier instead. Do you get better performance? If so, why?

