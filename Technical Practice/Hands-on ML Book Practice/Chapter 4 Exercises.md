# Goal
The goal is to practice chapter 4 exercises, integrating solidly its knowledge before studying new material. Chapter 5 exercises are next.

# Debrief
1. 

### Questions
1. Actually how much is usually taken out of all training set? I guess depends on how big it is, with millions of instances even 1% can be too big.
2. This raises interesting question: Are different scales bad because ml models get confused, or because training algorithms can't converge? Is that even a sensible question?
3. Actually I'm thinking. Can you do gradient descent where with time you increase the number of training examples it is being trained on, and decrease learning rate to find the exact optimal solution? Why there's no such way of training?


### Answers
1. It does.
2. Model doesn't get confused and in principle can learn appropriate weights for each feature. The problem is that it won't find these weights because of how gradient descent searches for them.
3. Find answer at the bottom of the doc, I asked cursor, and liked the full answer.

# Exercises
1. Which linear regression training algorithm can you use if you have a training set with millions of features? 
> If you have a training set with millions of features you can use Stochastic Gradient Descent or Mini-batch Gradient Descent, and perhaps Batch Gradient Descent if the training set fits in memory. But you cannot use the Normal Equation or the SVD approach because the computational complexity grows quickly (more than quadratically) with the number of features.

Hm, not sure where he is going with this question. 

🔴 => Alright, I was thinking he asks about some specific linear models: though which ones that could be?... Obviously he was referring to how we find feature values. 
Let's recall what each training algorithm stands for. 
Stochastic GD stands for when we pick randomly one training example and slightly adjust weights based on it.
Mini-batch GD is when we take a small part of all training examples, not 1, say a few percent, and adjust weights based on them. We pick that batch randomly.

Batch GD is when we use the whole training set for each adjustment.
Don't remember what SVD is, but I presume it is similar to closed-form solution. (=> kinda true)

❓ Actually how much is usually taken out of all training set? I guess depends on how big it is, with millions of instances even 1% can be too big. => It does!

---
2. Suppose the features in your training set have very different scales. Which algorithms might suffer from this, and how? What can you do about it? 
> If the features in your training set have very different scales, the cost function will have the shape of an elongated bowl, so the Gradient Descent algorithms will take a long time to converge. To solve this you should scale the data before training the model. Note that the Normal Equation or SVD approach will work just fine without scaling. Moreover, regularized models may converge to a suboptimal solution if the features are not scaled: since regularization penalizes large weights, features with smaller values will tend to be ignored compared to features with larger values.

Won't all ml models suffer from this? You should scale features, say based on their means.

🟡 => Again misinterpreting what he means when he says algorithm. I thought of ml models, he means training algorithms.
❓ This raises interesting question: Are different scales bad because ml models get confused, or because training algorithms can't converge? Is that even a sensible question?

---
3. Can gradient descent get stuck in a local minimum when training a logistic regression model? 
> Gradient Descent cannot get stuck in a local minimum when training a Logistic Regression model because the cost function is convex. Convex means that if you draw a straight line between any two points on the curve, the line never crosses the curve.

Hmmmm. I guess no because it is too simple of a model, gradient descent graphs looks like a bowl, it can't look any other way.

🟢 => yep.

---
4. Do all gradient descent algorithms lead to the same model, provided you let them run long enough? 
> If the optimization problem is convex (such as Linear Regression or Logistic Regression), and assuming the learning rate is not too high, then all Gradient Descent algorithms will approach the global optimum and end up producing fairly similar models. However, unless you gradually reduce the learning rate, Stochastic GD and Mini-batch GD will never truly converge; instead, they will keep jumping back and forth around the global optimum. This means that even if you let them run for a very long time, these Gradient Descent algorithms will produce slightly different models.

No! When we randomly pick training examples to speed up training it will differ. And if cost function is not convex depending on  initialized weights we might get stuck in local minima, while for others we won't.

🟢 correct.

---
5. Suppose you use batch gradient descent and you plot the validation error at every epoch. If you notice that the validation error consistently goes up, what is likely going on? How can you fix this? 
> If the validation error consistently goes up after every epoch, then one possibility is that the learning rate is too high and the algorithm is diverging. If the training error also goes up, then this is clearly the problem and you should reduce the learning rate. However, if the training error is not going up, then your model is overfitting the training set and you should stop training.

the model is overfitting, we need early stopping.

🟡 => correct, but didn't mention learning rate. Also didn't think of training error as an indicator, good point.

---
6. Is it a good idea to stop mini-batch gradient descent immediately when the validation error goes up? 
> Due to their random nature, neither Stochastic Gradient Descent nor Mini-batch Gradient Descent is guaranteed to make progress at every single training iteration. So if you immediately stop training when the validation error goes up, you may stop much too early, before the optimum is reached. A better option is to save the model at regular intervals; then, when it has not improved for a long time (meaning it will probably never beat the record), you can revert to the best saved model.

No, mini-batch is random, sometimes you have this peak but maybe it decreases after some time? Kind of sure saying that, but also not too much.

🟢 => correct.

---
7. Which gradient descent algorithm (among those we discussed) will reach the vicinity of the optimal solution the fastest? Which will actually converge? How can you make the others converge as well? 
> Stochastic Gradient Descent has the fastest training iteration since it considers only one training instance at a time, so it is generally the first to reach the vicinity of the global optimum (or Mini-batch GD with a very small mini-batch size). However, only Batch Gradient Descent will actually converge, given enough training time. As mentioned, Stochastic GD and Mini-batch GD will bounce around the optimum, unless you gradually reduce the learning rate.

batch will actually converge, stochastic will reach vicinity the fastest, but using one training example it will always meaninfully oscilate, mini-batch works best. By decreasing learning rate you make it less bouncy, but not actually converging.

❓ Actually I'm thinking. Can you do gradient descent where with time you increase the number of training examples it is being trained on, and decrease learning rate to find the exact optimal solution? Why there's no such way of training?

🟢 => correct, was a bit confused how he used converging as terminology. all random picking gd methods bounce, and will small learning rate bounce less, but none ideally converge as batch gd does.

---
8. Suppose you are using polynomial regression. You plot the learning curves and you notice that there is a large gap between the training error and the validation error. What is happening? What are three ways to solve this?

great question. and I need to spend more time integrating all performance measures stuff. Large gap could mean either training error is high, validation is low, or the other way around.
Training high, valid low means... well, not sure what it means. high training signals bouncing around, so too high learning rate, low validation error means we have kind of a good solution? ... but shouldn't then training error be low? ..

Let's try the other case. Validation error high, so we're poorly learning, training error is low, well that means we're underfitting, right?

Can high training error, with low validation means we're overfitting and use a very powerful model? But wouldn't it then have low validation as it doesn't generalize?

Now about three ways to solve it. well, answering that well depends on the cases above, which I'm not really getting.

aha, right. I'm using polynomial regression. Does that tell me something? Can it also be that there are no cases where we have high training error and low validation error. Maybe. 

If that's kind of the case, then solutions would be about adding degrees of freedom, unregularizing our dear model. 

> If the validation error is much higher than the training error, this is likely because your model is overfitting the training set. One way to try to fix this is to reduce the polynomial degree: a model with fewer degrees of freedom is less likely to overfit. Another thing you can try is to regularize the model—for example, by adding an ℓ₂ penalty (Ridge) or an ℓ₁ penalty (Lasso) to the cost function. This will also reduce the degrees of freedom of the model. Lastly, you can try to increase the size of the training set.

🔴 => dead wrong! Partially*

When training error low and validation error high, we are overfitting. We have memorized training data, making no mistakes on it, but failed to generalize to validation error.

Indeed, high training error low validation error doesn't really happen. If it does it is some extraordinary bug.

But why low training error means overfitting, my intuition about underfitting was clearly wrong. I just didn't think it through frankly, it makes total sense that underfitting means high training error.

Solutions to overfitting are all known to me.

---
9. Suppose you are using ridge regression and you notice that the training error and the validation error are almost equal and fairly high. Would you say that the model suffers from high bias or high variance? Should you increase the regularization hyperparameter α or reduce it? 

First, I don't really remember what ridge regression is. But both high training and validation error based on my past exercise analysis means model is underfitting, so you need to decrease regularization.

> If both the training error and the validation error are almost equal and fairly high, the model is likely underfitting the training set, which means it has a high bias. You should try reducing the regularization hyperparameter α.

🟢 => correct.

---
10. Why would you want to use: 
    a. Ridge regression instead of plain linear regression (i.e., without any regularization)? 
    b. Lasso instead of ridge regression? 
    c. Elastic net instead of lasso regression? 

a. I'm not getting the question, as I don't remember what ridge reg. is. But I presume he's asking why would I want to use regularization. Well, because the model overfits!
b. Don't remember the difference...
c. elastic net. hm.. no clude what that is either :)

> A model with some regularization typically performs better than a model without any regularization, so you should generally prefer Ridge Regression over plain Linear Regression.
> Lasso Regression uses an ℓ₁ penalty, which tends to push the weights down to exactly zero. This leads to sparse models, where all weights are zero except for the most important weights. This is a way to perform feature selection automatically, which is good if you suspect that only a few features actually matter. When you are not sure, you should prefer Ridge Regression.
> Elastic Net is generally preferred over Lasso since Lasso may behave erratically in some cases (when several features are strongly correlated or when there are more features than training instances). However, it does add an extra hyperparameter to tune. If you want Lasso without the erratic behavior, you can just use Elastic Net with an l1_ratio close to 1.

🟡 => I didn't remember all those difference because I didn't consider them important. But I'm reconsidering. I'll practice them more.

---
11. Suppose you want to classify pictures as outdoor/indoor and daytime/nighttime. Should you implement two logistic regression classifiers or one softmax regression classifier? 

ah. It's bad I neither remember what softmax is about, I should've practice flashcards and feynman stuff before doing exercises. I guess two logistic regressions.

> If you want to classify pictures as outdoor/indoor and daytime/nighttime, since these are not exclusive classes (i.e., all four combinations are possible) you should train two Logistic Regression classifiers.

🟡 => ...

---
12. Implement batch gradient descent with early stopping for softmax regression without using Scikit-Learn, only NumPy. Use it on a classification task such as the iris dataset.

very good task, which I'll do separately.

# Appendix

Answer to 3 question by cursor:
**Answer**: This is actually a **valid and interesting idea**! Similar approaches do exist, though they're not the standard approach. Here's why:

**Why it could work:**
- Start with small batches (like Stochastic GD) → fast initial progress, get to the vicinity quickly
- Gradually increase batch size → more stable gradients, less noise
- Decrease learning rate → fine-tune to exact optimum
- This combines the speed of Stochastic GD with the stability of Batch GD

**Why it's not commonly used:**
1. **Mini-batch GD with learning rate decay is already very effective** - It's simpler and works well in practice
2. **Computational cost** - Larger batches require more computation per step, so increasing batch size over time can be expensive
3. **Diminishing returns** - The benefits of this hybrid approach may not justify the added complexity
4. **Other techniques exist** - Momentum, Adam, and other optimizers achieve similar goals (fast convergence + stability) without needing to change batch size

**Similar approaches that do exist:**
- **Progressive batch training** - Some research explores this, especially for large-scale training
- **Curriculum learning** - Gradually increasing difficulty/complexity of training examples
- **Warm-up strategies** - Starting with smaller learning rates, then increasing (opposite direction but similar philosophy)

**TL;DR**: Your idea is theoretically sound and similar techniques exist, but in practice, fixed mini-batch size with learning rate decay is simpler and works well enough that the added complexity isn't usually worth it.
