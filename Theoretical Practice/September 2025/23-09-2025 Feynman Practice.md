
Machine learning is about "implicit coding" of computer to do some task we can't explicitly code step by step. 

Some problems can not be solved through specifying exactly line by line what computer should do. Some problems can be solved by specifying what algorithm should computer use to learn about how to solve the task. 

We can't instuct computer step by step, yet we can give it a "learning manual", through which it would arrive at the algorithm that actually solves the task.

Machine learning is fundamentally about new kind of problem, and a new kind of solution to them: implicit coding.

(For example, consider how would you teach computer to identify a bee in a photo.)

-- 

Fundamentally, such machine learning problems come down to:
1. Collecting some data about a phenomena of nature
2. Preparing the collected data to be used by model
3. Applying the model to the prepared data 

The model hopefully finds some regularities/ patterns that could be used to successfully solve new, unseen tasks. 

Hopefully, the model learned something fundamental about the data (phenomena of nature) it saw which we then can use.

--

This also reveals what are the steps or a usual ML project:

1. Understand the problem space
You first need to properly understand the problem. The better you understand the problem, the better you'll be able to first expand the solution space, and then trim it based on the constraints. Deeply understanding the problem is actually the most important step of any ML project, as many times you'll find out you don't even need to solve anything. Over-optimization of something that shouldn't exist is the most popular mistake engineers make. Deeply understanding the problem helps you to avoid it.

2. Data (from collection to processing)
As you understand the problem, you realize ML could solve it. You then would need to collect data about some phenomena of nature that is relevant to the problem and could help to solve it.
You need to make sure the phenomena is not bs (say white noise), and that your methodology of collecting its data is not bs too.
As you have collected data, all the fun is only beginning. Then, you need to properly prepare the data to be used by ML models/ algorithms. This means: feature selection, feature engineering, data imputation, feature scaling, outlier handling ...

3. Model
Say you actually understand the problem, you actually collected the data from the right phenomena, and your methodology is sound, and even, all your proceeding data preparation for the model is not bs. Well, you're nearly there. Now you actually need to apply the model/ algorithm to analyze/ learn about the data and construct a model out of it that could be used on new instances.

You can do k-fold cross-validation for shortlisting and eliminating models, and then finetune the 1-2 most promising ones. Lastly you can test how good your model is on a test set which was never seen by the model to get a good view of how good your model generalizes.

4. Deployment
Say your model does good enough to share it with others: you actually solve the problem! Well, then you need to prepare your model, and the data preparation you do to be deployed, and you need to present your results. If successful, you'll need to monitor and maintain model in production.

--

In explaining the main steps of an ML project we can also tell what are the main risks of it:
1. THE MOST IMPORTANT AND LIKELY: Solving the problem that shouldn't be solved, or understanding it not deeply enough to properly see and trim the solution space.
2. Poor choice of nature's phenomena to collect data on, not relevant to problem.
3. Poor data collection methodology.
4. Poor data preparation.
5. Poor model choice and its finetuning, overfit etc.
6. Poor deployment, presentation, monitoring.

--

As we have clarified the general stuff about ML, let's go a bit more in-depth.

When talking about the model one can choose, we can group models/ learning algorithms based on 3 dimensions:

1. Supervision during training -- does training data have the target feature (desired output) or not. This is not binary, but rather a spectrum:
    a. supervised -- yes, all training instances have targets
    b. semi-supervised -- some training instances have targets
    c. self-supervised -- we make a supervised dataset from an unsupervised (for example via masking)
    d. unsupervised -- training instances do not have targets.

2. Batch vs online learning -- can the model take in new training instances one at a time and slightly tweak its weights, or it has to re-train completely from scratch. Online learning it can, batch learning it cannot.

3. 🔴 => Very hard to remember this one. But I managed to recall.
How algorithms makes predictions -- does it create a generalizable model based on the training data which it then uses to make new predictions, or does it memorize by heart training instances, and compares new examples with them to make a prediction (similarity search, say like KNN)

-- 

Now we also need to talk about testing how well our model works.

For that we first split the collected data into training and test sets. On test set we could then test our model to understand how well it generalizes to new unseen examples.

Choosing between models (and their hyperparameters) based on how well they do on the test set is a bad idea, because you'll overfit to this specific test set, and not choose a better, more generalizable model.

So, to control for that we split the training set to validation and training sets, where validation is used as the preliminary test set for models and hyperparameters before the final test set. 

Yet, we run into the same problem: we'll just overfit the validation set now! To fix this, we use k-fold cross validation, where training data is split into (say 10) equal parts and model is trained on all parts but one, where the last part is used for validation. Then we do that 10 times for all parts and take the mean of result to evaluate how good the model was. 

--

Now, we should talk more in-depth about the performance evaluation of the model.

Sometimes it is easy, but that is not always the case.

Let's consider a popular example. One of the most popular models are supervised learning. Supervised learning generally solves two types of problems: regression and classification.

For regression everything is rather straightforward: you take the predict number and substract it from the target one, take the mode, sum-up those differences and voila you have a check of how well your model does.

With classification not so simple. If you have binary classification, like dead or alive then your model could be making either False Positive, or False Negative type of errors.

False positive is when the instance is actually positive (alive), yet model predicted it wrong. While false negative is when instance is actually negative (dead), but model predicted it is alive.

Depending on collected, processed data and how you trained your model it could do more of one or the other. In fact, depending on the problem it is trying to solve you might want to do one mistake much more than the other. For example predicting whether person has (positive) cancer or not (negative). You much rather scare some (predict they have it (positive), when in fact they don't: false negative) people but not miss the cancer (false positive: the cancer is there, but you guessed it isn't).

-
🔴🔴 I again mixed false positive and false negatives. Word positive or negative means model's prediction, not what actually is true. That's why saying false positive makes sense, it is a false prediction model made, positive or negative. So reverse all that was said before. Have to finally fucking remember the difference in names. 

False positive is when model predicts there's cancer, while there actually isn't. False negative is when model predicts there's no cancer, while there actually is.
-

So, false positive and false negatives are one way to classify errors the model could be making. 

We can put them in percentages, and we can also put them into one metric called 🔴F1, which is a harmonic mean of the two (harmonic mean is different from a normal mean by giving more weight to lower values, so you can't have one high value and one low, and get high harmonic mean, while you can with normal mean.)

There is also precision and recall.
And frankly, I absolutely don't remember what one or the other stands for. So: 🔴🔴

-
First off, I got F1 wrong. It is not harmonic mean of false positives and false negatives, but of precision and recall.

Now, precision calculates the accuracy of positive __predictions__ = True Positives / (True Positives + False Positives)

Recall (aka sensitivity) calculates the ratio of positive instances that are identified correctly = TP/ (TP + False Negatives )
-

Precision and Recall have are at a direct tradeoff with each other (🟡 something I should work on more to understand deeply and intuitively).

Besides comparing models, we might want to decide the decision threshold of the model. To do that we could create a bunch of confusion matrices, or we can plot ROC curve.

ROC curve plots recall (aka sensitivity) vs false positive rate. AUC is the area under the curve graph which can be used then as a single metric to compare between the models.
