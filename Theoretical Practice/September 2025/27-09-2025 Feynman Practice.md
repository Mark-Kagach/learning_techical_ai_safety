# Goal for this Practice
To briefly go over the known parts and go more in depth over the performance analysis parts.

# Debrief
Some mistakes with performance analysis, just a question of practice, I understand the concepts and why they are needed.
Also probably will use ML project steps as a scaffolding on which to put most of my ML knowledge.

---------------------------------------------------------------------------
ML is about implicitly coding computer, instead of saying to it how to do the task specifically step by step, we give it an algorithm of how it should learn to do some task.

This is because we cannot explicitly tell computer how to do it. As an example, think of trying to identify whether or not image has a bee. 
So instead we give it an instructions on how to learn, that's why I like to think and call that implicit coding.

--

ML is then fundamentally about collecting data on some phenomena of nature, then applying a mathematical model to it in hope that it will learn some useful patterns that could be applied to new cases.

--

Hence, we can say that the steps of an ML project are:
1. Deeply understand the problem space -- the most common mistake of engineers is optimizing something that shouldn't exist. Deeply understanding the problem helps because you can better see the solution space, and you can better understand what are the constraints for a viable solution, that makes it faster for you to trim the solution space. 
2. Data -- from defining what phenomena of nature to collect data on, to collection methodology, to nearly endless preprocessing, feature engineering, feature selection, scaling etc. in preparation for applying data to models.
3. Model -- from shortlisting, to doing performance analysis, to cross-validation, finetuning and choosing the decision threshold.
4. Production -- a unifying word for presenting ones findings, and then preparing the code for being deployed in production + monitoring and continuous maintenance.

--

From that we can also deduce what can go wrong in an ML project (i.e. the main risks):
1. You're solving/ optimizing the wrong problem.
2. Wrong phenomena of nature
3. Poor data collection methodology.
4. Bad data preprocessing
5. Overfitted/ underfitted model
6. bad presentation, deployment, monitoring, maintenance.

--

❓ If I use ML project steps as the foundational tree on which I put all the rest of my knowledge, then I can see that I need more structured explanations for the data process (production haven't studied yet), and maybe problem space.

For example talk about supervised learning, and how classification and regression are the most popular type type of ML problems ...

--

Now let's zoom in on the types of model we could use. In ML, we can broadly see them through 3 dimensions:
1. Training supervision -- whether training set has the desired end-goal features, not binary but rather a scare -- supervised, semi-supervised, self-supervised, unsupervised.
2. Way to make predictions -- model vs similarity (learned by heart) on the training set 
3. Learning way -- batch vs online learning => Can you incrementally add training data without the need to entirely retrain the model? 

--

Once we have the model, we need to consider in more detail how to evaluate it.

For that we have the test set, which we separate from the training data to get a somewhat independent assessment of how well our model will generalize to an unseen data. 
But if we want to choose between several models to then finetune and deploy one, we can't use test set as an evaluator, because we'll overfit it. Hence, we have validation set, but specifically k-fold cross-validation as otherwise we just overfit the validation set.

-- 

But besides this basic validation/ test set, we can do more complex performance analysis.

In particular this is useful for classifications.

(Here I should inject (or have explained before), that supervised learning are pretty popular type of problems, and 90% of them would be classifications and regressions.)

First, let's start with why. Say you have something that happens only in 5% of the cases, and you make a model that predicts that something never happens, then well we have great 95% accuracy!

So we need a better way to assess our models.

--

One way is to use confusion matrix which helps us to understand what type of mistake our model is making. 

Is it failing to identify a positive case, or it fails to identify a negative one?

Confusion matrix is usually a two by two grid of actual vs predicted positive vs negative cases. 

It would be useful to have the number for each type of mistake, but we probably want to know its ratios.

--

Specifically, we want to know the ratio of:
1. The correctly identified positive cases => Sensitiviy = Recall
2. The correctly identified negative cases => Specificity

For the first ratio we take the number of cases that are True Positive (correctly identied positive cases) and divided it by its sum with False Negatives (cases that are wrongly identified as positive, but actually are negative).

For the second ratio we take the number of True Negatives and divided by its sum with False Positives.

We might also want to know the ratio of true positives out of all positive predictions we made, so = TP/(TP+FP) => Precision

--

This is a lot of ratios, you might want some single metrics.

For that you can take the harmonic mean of recall and precision. Harmonic mean instead of a normal mean because it penelizes low values, so you can't end-up with a high number if any of your numbers is low. 

This is known as F1, and it could be used to compare several models between each other.

--

Besides comparing models, you might want to decide where to put the decision threshold in any one model. This would influence what type of mistakes you'd be making, you might want to favor one over the other. For example it is better to never miss a cancer, but give some people a scare, then to miss it sometimes with less people thinking for a day or two they have it.

To understand how changes in the decision threshold influence your models mistakes you could use plot the change of Recall vs False Positive Rate
🟡 Not sure of the fals positive rate. 
Is it : FP/(FP+TN) ?

🟡 Not intuitive how the ROC graph is plotted. Because it is about the changes of thersholds, but it is not on any of the axis?


You could then know the optimal decision threshold that would balance mistake types. And you could also calculate the area under the curve to use it to compare between the models.

