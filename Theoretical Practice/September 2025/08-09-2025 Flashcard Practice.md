# Flashcards


Broadly ML algorithms can be categorized along 3 dimensions:
1. supervised vs unsupervised -- (to be precise it is rather scale than binary) is about whether the training data has labels with the desired output for each.
2. 🔴online vs increment based learning -- Can model learn in bit by bit, with adding of new information, or it has to be retrained entirely everytime you want to add any new training data?
➡️ batch not increment learning.

3. how model makes predictions -- instance based vs model based. Instance based learn training examples by heart and compares them to new instances by similarity and makes predictions. Model based is trying to create a generalizable model (some meaningful trend/ pattern in the data) and use that model to make new predictions.

--
🟡 Training supervision is about whether or not training data has labels. 

🅰️ it can be supervised, unsupervised
semisupervised - when only part of the training set is labeled.
Self-supervised - when you generate a labeled dataset from an unlabeled one (say by doing masking etc.), and this is usually to do transfer learning afterwards
reinforcement learning -- when an agent observes environment and performs actions to get rewards.

predictions can be instance or model based. Whenever you choose a model, you make assumptions about the trend and data you might be capturing, this means limitations.

online learning vs batch is about whether or not model can continuously take in new training data without having to be retrained entirely.

--

ml project is about capturing some instance of nature, and modelling it in order to hopefully capture some useful trend (pattern) that we can use to our advantage.

ML is like any other computation it is about taking data and applying algorithm (transformations) to it.

Thus, the main risk of any ml project is that it either has bad data or bad algorithm.
I like to say that it is either we capture a useless instance of nature that has no helpful trends (think of white noise), or we capture a useful instance but do it poorly (a lot of noise, poor features), or the algorithm we have chosen is unable to find/ learn the useful pattern.

🟡 Bad data comes down to two main problems: either the sampling noise where our methodology is perfect, but the sample is so small it creates random noise; 
or sampling bias where our methodology is faulty and poorly represents the whole population we study.

🟡 bad model comes down to either being too complex, or too simplistic. Too complex means it overfitted to the data -- it learned useless patterns and "memorized" training data too close to heart -- so it won't generalize.
Underfit means that model didn't learn meaningfully useful patterns and can't make useful predictions. Because say the real patterns are more intricate than what model can simulate (capture).

--

Testing and validating is about checking how well model can make generalizable predictions.

With any data we can choose many models with many hyperparameters -- how to choose which one?
We can start with basic useful assumptions about the data and land on just a few models to consider. But it becomes much harder to choose that way meaningful hyperparameters. So, we could train several (or same) models with different hp and see which one performs better on a test set.
The problem is that we'll likely overfit and choose the model that specifically performs best on that test set.
To fix that we can create a validation set and test our models on it, and then check them on the test set to see how well our models have learned to generalize.
Yet, we can overfit validation set too. Here comes the cross validation technique that fixes it by training and testing on different parts of the training set and taking the average of all trials.

--

Fundamentally, ml is another coding paradigm, where instead of giving specific step by step instructions to computer of how to transform data (i.e. an algorithm), we specify how it should learn the algorithm.
This is usually because of the nature of the problem: how exactly you explicitly code to recognize bees.

ML then, is about collecting data about some instance of nature, and using the right model that can find a useful pattern (trend) in the data which we can use to our advantage -- like making predictions on the new unseen examples.







