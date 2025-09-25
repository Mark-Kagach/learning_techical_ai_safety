# Exercises

1. Machine learning is about a different paradigm of giving instructions to computers. Mainly, it tackles problems to which it is hard to give explicit instuctions line-by-line (like in a usual programming). For example, how would you code for computer to indetify bees on the pictures? Pretty hard. 
We cannot specify the exact algorithm computer should follow to perform the task. Instead, we specify how computer should __learn__ that algorithm.
All computation is about data transformations, some data transformations are complex and can't be specified explicitly step-by-step (like bee identification), so instead we specify how to computer should learn needed to us data transformations. (We evaluate and correct it accordingly.)
🅰️ Machine Learning is about building systems that can learn from data. Learning means getting better at some task, given some performance measure.
➡️ Here is how I captured it in my notes: Machine Learning is about not giving explicit instructions to computer on how to do the task, but rather how to learn about it from the data we provide.

2. From any basic stat stuff like clustering data or linear regression, to more complex things like picture and sound processing (generation and identification).

3. When you have data examples and the correct answer attached to them. That way you can provide tight feedback loops to your model.

4. 🟡 Tasks where you have to either classify something (like digit identification), or predict something (like house prices).
🅰️ The two most common supervised tasks are regression and classification.

5. 🔴 Clustering, can be ?... 
🅰️Common unsupervised tasks include clustering, visualization, dimensionality reduction, and association rule learning
➡️ Association rule learning? Dimensionality reduction? Visualization Didn't get those entirely.

6. RL.

7. Unsupervised. K-fold clustering can do the job.

8. 🟡 Well, depends on the dataset you have? If you have spam assigned to training examples, then supervised.

9. System that can learn incrementally and doesn't have to be retrained from the start if you provide a bit of additional data to it.

10. When training data cannot fit on your computers memory, so you split it between several computers.

11. instance based one. It learns by heart training examples and compares them to new example, think k-fold.

12. 🔴 Model parameter? Not sure. But we have a mathematical model (say linear regression or NNs) we use to process our data, and its slight details (variations) are tweaked by hyperparameters.
🅰️ A model has one or more model parameters that determine what it will predict given a new instance (e.g., the slope of a linear model). A learning algorithm tries to find optimal values for these parameters such that the model generalizes well to new instances. A hyperparameter is a parameter of the learning algorithm itself, not of the model (e.g., the amount of regularization to apply).
➡️ Totally fucked this up, need to understand it better.

13. 🟡 They search for a generalizable pattern in the training data, they encode it, and use to make predictions about new instances.
🅰️ Model-based learning algorithms search for an optimal value for the model parameters such that the model will generalize well to new instances. We usually train such systems by minimizing a cost function that measures how bad the system is at making predictions on the training data, plus a penalty for model complexity if the model is regularized. To make predictions, we feed the new instance's features into the model's prediction function, using the parameter values found by the learning algorithm.

14. ML is about capturing some instance of nature and finding a useful regularity (pattern) that we can use to our advantage (usually through modelling the data). From that description, the main things that can go wrong in an ML project are: (a) poor data collection of the instance of nature, (b) poor choice of the instance of nature, (c) poor choice of the model which doesn't capture some pattern of nature.
🅰️ Some of the main challenges in Machine Learning are the lack of data, poor data quality, nonrepresentative data, uninformative features, excessively simple models that underfit the training data, and excessively complex models that overfit the data.

15. Overfitting. You can change model, fix hyperparameters (like regularization) or possibly your training data is non-representive.
🅰️ If a model performs great on the training data but generalizes poorly to new instances, the model is likely overfitting the training data (or we got extremely lucky on the training data). Possible solutions to overfitting are getting more data, simplifying the model (selecting a simpler algorithm, reducing the number of parameters or features used, or regularizing the model), or reducing the noise in the training data.

16. Test set is a set of data you hold from the model to use as the final test of how good the model performs on new instances. Like a last exam for students.

17. To evaluate which model & hyperparameters perform best before checking it on the test set. Think of it as the practice sheet for students before the final exam.

18. Imagine you collected a lot of training data that might not be representative, and you saved representative data for validation and test sets. Then suppose your model does poorly on the validation set. Is it because the model overfits the training data, or because training data is very noisy? To answer that you make another test to check whether model overfits on the training data called train-dev. This set should be taken directly from the training data distribution, not validation or test sets.

19. We can overfit the test set, that's why we need validation set. Yet we could overfit it too, that's why we have cross-validation technique, even though it could take some time when training.
