# Goals
1. I want to specifically pratice recalling and explaining performance analysis concepts.
2. Explain main data science/ ML libraries.

# Debrief
1. Still struggle with intuitively explaining ROC.
2. Am I mixing up precision recall tradeoff curve for decision threshold with DT for ROC?

### Re-explaining Debrief
1. We could plot the ROC curve either by shifting one by one and connecting it as many points (continuous curve), or we could also look only at decision thresholds that get new results and just connect those points. Regardless, we go through the range of decision threshold values that produce 1,1 and 0,0 coordinates on the ROC. We don't need to change decision threshold any more as results won't change.
2. Recall/Presion graph and tradeoff does the same job as ROC curve: it tries to show what tradeoffs we are making by changing the decision threshold of the model.

Okay, I feel better about the topic. ROC curve can just be drawn with precision instead of false positive rate on the x-axis and they're doing +- the same job of trying to find the optimal decision threshold or compare models via area under the curves.

-----------------------------------------------------------------------
# Performance Analysis

So, imagine you have a classification problem. You need to assess how well your model does.

The issue is that using simple accuracy score is doesn't give the complete picture.

Imagine you are trying to classify cancer, and in your dataset it happens in 5% of cases. Then, model that says people never get cancer would get a great result of 95% !

So we need a new way to measure such classification models.

--

One way is to use confusion matrix which tells you the type of problem your models are making, and from which you then can calculate a bunch of useful ratios.

Confusion matrix is usually a 2x2 grid where on the x axis you have predicted negative and predicted positive cases, and on the y axis you have actual positive and negative cases.

Then you can see what cases where predicted correcly: true positives, true negatives. And what cases where predicted wrongly: false positives, false negatives.

--

But right now you just have number of cases in each quadrant. Obviously we'd want some ratios.

We could calculate the ratio of correctly predicted positive cases, and correctly predicted negative cases.

Sensitivity/ Recall = TP/(TP+FN)
Specificity = TN/(FP+TN)

We could also calculate what are true positives out of all positive cases predicted, this is called Precision = TP/(TP+FP).

--

Using sensitivity and specificity we can tell the ratios of the type of mistakes we are making.

1-sensitivity tells us how much false negative mistakes we're making
1-specificity tells how much false positive mistakes we are making.

--

We could decide to trade off one type for the other and make model more biased to it.

For example, it is much better to identify all patients with cancer, but give some people a false scare they have one. Then to have no people with false scare, but miss some.

In this case we making more false positive mistakes (saying someone has cancer, but in reality they don't), then false negatives (saying they don't have it, when in reality they do).

--

We can use confusion matrix and specificty/senstitivity ratios to compare models, yet having several ratios is cumbersome.

We can combine recall (= sensitivity) and precision as a harmonic mean to get a single value called F1 of how well our model performs. Harmonic mean instead of normal mean because it gives more weight to lower values, so we can't have high F1 without both numbers being high.

--

Once we have compared the models and settled on one or two, we might want to change its decision border to trade off some false positive and false negative mistakes as we have discussed before.

We could change the decision threshold bit by bit and make many confusion matrices to compare it. Or we can make a unifying graph to know what are the optimal decision thresholds for this model.

For that we plot false positive rate (= FP(TN+FP) ) (aka 1-specificity) on the x-axis (and how it changes with shifting decision threshold) vs recall(sensitivity) on the y-axis. This graph is known as the ROC.

This create a curve that ideally stays far away from the diagonal, as diagonal is the worst which means model is doing no better then a random guess.

We could then calculate the Area Under the Curve for that curve (which would always be less than 1), and use it as a metric to compare between the models.

Once again this curve also signals where decision threshold could be.

--

Well, I think this is mainly it, now let's evaluate.


---------------------------------------------------------------------------
# Main data science/ ML libraries.

In describing main data science & ml python libraries we must start with numpy.

🟡 Numpy provides a more efficient array (vector) to do basic array computations (linear algebra)

=> it is a multidimensional array, i.e. can be a matrix.

Its numpy array is the fundamental data structure on which all data analysis and ml rests in python.

Then we have pandas that is a useful library that helps to do popular data analysis/ science operations. It also has its own data structures of series (array) and dataframe (matrix).

One easily converts from pandas data structures to numpy arrays.

Then we also have matplotlib to make graphs of data.

We have a few scapping libraries I don't remember atm and thankfully don't need to remember atm.

We have scipy which does basic scientifi computation

then we have sklearn which does basic ml operations 

and then deep learning // NN focused libraries of TF and keras and pytorch.

They have their own matrix data structures to do matrix multiplications faster and also it all is optimized for parallel computing. All in the name of deep learning!



