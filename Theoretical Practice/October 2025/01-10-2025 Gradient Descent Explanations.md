# Goals
1. Well fellas, today is the day. In every man's life there's a moment where they pop the gradient descent explanation cherry, and today is such day for me.
2. I also want to explain how models learn in general.

## Arose Questions
1. We calculate gradient, slope or derivative?
2. "It gives us the gradient for the steepest slope?"
3. Gradient * -1?
4. The formula is w_new = w_old - gradient * alpha_learning_rate
5. Alpha learning rate vs how strongly we take new/ old information
6. how gradient values change as we get to the minima?

# Debrief
1. So the general explanations are correct, yet need to revisit a bit math with gradients and derivatives. For multivariate equation we calculate gradient, while for single variable derivative.
2. Gradients can be of any values, not just between 1 and 0, same for slope. 
3. The magic of calculus is that to calculate gradient we don't need other points, we use chain rule. I don't remember this at all so this is for future learning. 
3.5 Okay, Cece (my friend who studies AI) explained that they don't use one point, they add h which is an extremely small number using which we calculate the slope for that point on a loss function vs weight values graph. And now when we have the multivariate equation, each derivative of parameter's weight all together makes us a gradient vector. And when you add them all together you get a direction towards the minima. 

--------------------------------------------------------

So, first we'll start with ML and general steps of any ML project, from there we'll move on to models and gradient descent.

In general, I want to use ML project steps as the branches on which I "hang" most of my explanations. Like a christmas tree, only it has 3 branches and on each branch is an overkill number of toys (explanations) hanging on.

ML is an implicit coding of computers, where we don't code computers step by step, but rather give an algorithm of how it should learn to do the task. It is a subset of Artificial Intelligence that is rapidly consuming all other parts of AI due to its huge success, which is mainly driven by prolifiration of data and compute.

So.

A regular ML project has 4 steps:
1. Understanding the problem.
2. Data, from collecting to preprocessing.
3. Model, from shortlisting to finetuning.
4. Deployment, from production code and presentation to maintenance.

If I were doing a holistic overview of my knowledge I would start with explaining step 1, then step 2 and so on. Today we'll just focus on step 3. (And of step 4 I know little atm.)

--

So, models.

How models actually learn? What is an actual process?

Well, surprisingly or not (given the universality of epistemology), ML models follow a vaguely similar process to as what would animals or humans do.

First, the model makes a prediction (inference). Second, the model gets feedback (loss/error). And third, it adjusts based on the feedback (train/ learn).

Let's get more concrete.

First, ML engineer specifies the mathematical model (architecture) that computer should use to transform inputs into outputs (think linear regression, logistic regression or nn's), like an skeleton. 

But skeleton without any internals, because right now this model has random weights corresponding to each parameter. The data transformations this model does are useless as they're random.

ML engineer sets some random weights because the model need to start with some prediction to learn, regardless of how inaccurate it is.

--

So, our models does a prediction given the training instances (for the sake of explanation assume we're doing supervised learning).

Now we can evaluate them (give feedback) using the loss function and target values.

Before that ML engineer chose a loss function. Loss function helps us to grade how well the model does by comparing its predictions with target values. 

When you think of a scientist, when they do an experiment, reality is what gives them the feedback. For our ml model things are easier, the whole "reality" (world) is compressed into a loss function and target values of a training set.

Loss function returns a number that tells how well the model did, because it is a loss function, the lower the number the better. Basically it is like a error sum of the model predictions vs target values.

(What is interesting, is that we use loss function to test how well our model does, yet it is different from the final performance measure we'll use for our model, i.e. our test set and how ever we'll evaluate it. While loss function and final performance measure should be similar, they're doing different jobs, so they are slightly different. Ideally, final perfomance measure is as close to the problem we're trying to solve in real life, while loss function should be close, but mainly fast to compute.)

(So we are calculating a loss function of our model vs? ... Well, depending on our algorithm it would be either the whole training set, one random instance, or some small random batch of the training set. But about that in a minute.)

--

So we have received the feedback our how well or bad our model does, now we need to update based on it.

How do we do that?

Well, now we get to the real deal. 

What we will be updating is our mathematical model's weights. We can define the problem as: Find model weights that minimize the loss function for the training set (but also don't overfit etc...).

This is an optimization problem given some constraints.

Sometimes, we can tell what are the minimizing weights right away by computing an analysis equation, but this is rare and only for the simplest cases like linear regression.

So instead, what we usually do is follow a gradient descent algorithm that helps us to solve all kinds of optimization/constraint problems.

Let me describe how it works.

--

The problem is that we want to find model weights that will minimize the loss function for the training set. 

To do that we get our randomly generated weights and make a prediction. Then we calculate the loss function. It gives us some value.

Now, we plot that value on the y-axis, where on the x-axis is the weight value for some model parameter. (For this example assume our model has one paramater and this is the only thing we are optimizing. Like a one variable linear regression, no bias term.)

🔴 Then we calculate a derivative (not gradient or slope right?)

🔴 It gives us the gradient for the steepest slope?

🔴 Because this is a loss function, we want to go down, not up, so we take a change in our model's weights in exactly the opposite direction from the gradient. (i.e. gradient*-1 ?)

Alright, so we are now updating our model's weights. But by how much and how exactly?

🟡 The formula is w_new = w_old - gradient * alpha_learning_rate

Where we specify the alpha learning rate which tells us how big a change should we make to our model's weights. The bigger the alpha, the more we change model's weights. (but also gradient decreases as we approach the minima)

Then we repeat this process until we hit the bottom/ plateau and gradient becomes zero.

And voila, this is how we solve the optimization/ constraints problem and find model weights that minimize the loss function for our training data!

--

Now let's make that explanation closer to reality. First, instead of one parameter, it is 20-50-10000 dimension graph. We can't imagine more than 3 dimensions so just hang in there, but at the end of the day is the same hill and ball going down.

There are different gradient descent type, where the loss function is either calculated on the whole training set (which you can imagine takes forever). So instead we also can use a single random instance (but then we never settle and always oscilitate around the minimum (because gradient is never zero)). Or we use a random small batch of instances and, it is more precise in finding the minimum, takes a bit more computational resources and also never settles on the minimum (mini-batch gradient descent).

Moreover, we can play with how much we change model weights, for example with first recursions changing a lot (as we're probably far away from the minima), but with time making less changes (as we're probably approaching minima). But this is beyond todays practice.

Also, It is important to choose a mathematical model that could capture trends in data and do useful transformations, some math models (architectures) are just not powerful enough and no weight will make it useful. Think of using linear regression to predict weather or do computer vision.
The useful part about neural networks is that they can learn any mathematical function, i.e. they can do any processing to data that is allowed by our laws of physics.

--

Alright, what else could I be forgetting? Broadly that's it, let's do feedback! Just like our dear model!


