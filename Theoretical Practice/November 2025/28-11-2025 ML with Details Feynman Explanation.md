# Goal

Now that I have my sexy-ass mental model for "forest" thinking about computers, coding and ML, let's talk trees and leaves.

?

## Questions
1. This specifies the flow of information.❓ => it does, but how would I tie it well?
2. 

## Answers

# Debrief

# Adding details to my past explanation

Alright, we have our learning algorithm, we have the general framework it follows of guess => feedback => update (and that humans follow similar loop). We have the understanding that models learn both the phenomena and transformations. And that similar process is done by humans during explicit coding (and yes implicit coding too). And that the need for such huge amounts of data is because of efficiency of learning algorithms we give to computers. We also have understanding that in giving data we want to accurately describe phenomena, which mainly comes down to capturing the most important parts, and giving enough samples both to learn the phenomena and learn generalizable transformations. We know that in choosing mathematical architecture for the ML model is the question of assumptions we make about phenomena/ problem at hand, and that based on our choice we'll create a hypothesis space which has to be just big enough to contain viable solution, but not too big for search to either take forever, or for data to be too noisy to give useful signal to find viable transformations. We have the understanding that implicit coding is just instructing computer at a higher abstractions level. 

Even with all that understanding probably the most useful next step is to describe step by step on an ML project (i.e. implicit coding project). And then use it as a structure to talk about other details.

1. So the first step as always (implicit coding, explicit coding or anything in life) is to deeply understand the problem. What is wanted from us? Do we need to solve that problem? What is the goal? What are the breakpoints? What is the starting position? What is the underlying phenomena that problem is about? 

Say you have really fucking understood the problem, it actually must be solved, you even actually can solve it with ML (from now on I'll just say ML not implicit coding cause its more convenient). You understand the inputs and wanted outputs. What now?

2. You'll have to collect data about the problem/ phenomena. It would have to be high-quality data. You might have to clean it, and do some feature engineering and scaling to make it easily digestable for the ML algorithms you'll use. This step would take most of the time. You might split the data to check generalizability of your ML algorithm.

3. You have your data ready, now let's talk model. You need to pick (usually short-hand first) the right model. I call that the right mathematical architecture: either linear regression, logistic regression, decision trees, support vector machines, basic neural networks, deep neural networks etc. (This specifies the flow of information.❓ => it does, but how would I tie it well?) 

In choosing this architecture you define the hypothesis space of possible transformations model could find. Hypothesis space is all space of all the weight combinations variables could take. Some of the weight combinations perform just the right transformatiotns that give us the desired output given the inputs. 

Then you'll probably start training the ML model. In training it you'll follow the learning algorithm. It will start by filling mathematical architecture wiht random weights. Then you feed this model sample input, and voila you have your first guessed output. You compare guessed output to the one you wish transformations produced for the given input. You use these two points of informations to give feedback on how well model (i.e. weights) have done. You use that feedback to update the weights accordingly (gradient descent). New weights make new predictions and so on until you find good transformations. This is all automated of course.

Here you can think of data as clues model uses to find right transformations in hypothesis space. To find useful transformations we need to collect high quality data for the problem we are solving, we might need to do some feature engineering with that data so that it is easy to manipulate for our learning algorithm. Data is also the __world__ in which our model operates. 

As we invent more and more powerful learning algorithms this engineering of data should decrease. 

In this description it is of no surprise that basic data science or machine learning professionals spend most of their time collecting, cleaning and engineering data. Why? Because invention of new useful learning algorithms is really hard! So in practice there are just a few cutting edge ones that are used for most of the problems, and problem then is to find and prepare the data to be used by those algorithms.

Once you have ran the learning algorithm and you have found the desired transformations you get to the last part.

4. Deployment. You understood the problem, you collected and prepared the data so learning algorithm could find desired transformations, you even checked and they work well on various cases. Now is the time to present your work and make it easily usable by common folks.

--

Just want to note that doing an ML project is not as linear as I describe it. Many times you might start with the model, and then collect or transform some data just for that model. You might go back to re-understanding the problem even after deployment, and many similar things. Just keep that in mind.

--

Alright, after that description of steps we could go in more details for each. 

For example the data steps is about collecting, cleaning and feature engineering data.

Model step is about really understanding assumptions you're making about the phenomena at hand, and what is the right level of hypothesis space to allow also given the available compute and time.

It is also about type of such models there are: supervised, unsupervised, and reinforcement learning.

And about how to make those model not learn data by heart and hence find no generalizable transformations, but also be not too simplistic and actually find useful patterns. So validation and testing. And then putting a number on those metrics and balancing them correctly -- performance measurement.

Deployment has a whole another world of dashboard and calls, keeping data and model up to date that I didn't go into yet.

== => Listening MLG.

Besides supervised, unsupervised and RL, we also have online and "non-online" learning? 

Is even unsupervised learning following the guess => feedback => update loop?


## v2 Explanation of Computers, Coding and ML

Alright, here's my last version after 5 days of explaining and clarifying about what computers are, and how ML connects to it all.

One of the most fundamental things about humans is that we are tool-makers. This is what we are known for in animal kingdom.

From the time some chimp have picked up a rock and used it to defend, attack or do anything else that was harder to do with its own body. From that moment we were on the trajectory of inventing better and better tools, and using them to achieve our goals. Tools are a leverage to our body which allows us to do more than we could on our own. It allows us to have transform the world in bigger and bigger ways.

In line with that grand trend of humanity, during Industrial revolution Charles Babbage created a tool to solve math equations. He was frustrated by the work that humans were doing, and just as chimp picked up a rock, Charles invented a tool so more equations could be solved, doing it more accurately and faster.

Turns out a tool that can solve math equations is an extremely powerful tool, because at its core it is about manipulating information -- a fundamental property of nature, just as fundamental as matter.

He called that tool computer -- the most powerful tool humanity has created.

Even since humanity was on a journey of improving that tool.

So how does it work?

You need input and output devices, to take in and give back information. You need instructions of how you would like to transform that information. You need to store those instructions, and store some preliminary information while doing transformations (anything that would come handy), you'd also need head to manipulate memory to derive outputs. And lastly you'll need energy to power it all.

We'll skip describing in details how memory is implemented (binary, arrays and linked lists), or how head can be of different kinds (cpus, gpus), or how because it is more convenient for computers to store information in binary form we needed to invent coding languages to instruct computer in a convenient manner for humans. We'll skip exciting inventions like internet which make computers talk between each other based on radio information (and at incredible pace thanks to speed of light), or that you can even use computers to code money!

In today's lesson we'll go more in depth about how we instruct computers -- coding.

For our purposes it is useful to differentiate two paradigms for doing that: explicit and implicit coding.

Let's start by saying that all what computers do is: input => transformations => output.

So coding is about: specifying what inputs to take in, and how to transform them. This was summarized by famous book name: "Programs = Data Structures + Algorithms" (I inverted the name order because I think it is easier to understand that way). Coders then have to decide how to structure inputed data, which fundamentally comes down to what transformations you want to do. All information is structured based on arrays and linked lists which are the two ways memory is actually physically implemented, all other structures from trees to hash tables is just a combination of those two. Once we chose structure, algorithms are general manipulations of this information which frequently occurs, the main buckets of algorithms are search and sorting.

Now that you have the basics let's talk about paradigms of instructing computer. In principles deep down they are similar, but in practice they are different and it is very useful to differentiate the two.

So the two paradigms are explicit and implicit coding.

Explicit is the good old way of instructing computer, you have some programmer that specifies step by step exactly what computer needs to do. 

Implicit is the new emerging way to instruct computer (arising from around 2010s), where you give computer an algorithm to learn how to do the task. 

So if previously programmer would specify by hand the transformations, now programmer gives an algorithm that learns the right transformations.

A helpful perspective is to see explicit programming as: inputs => transformations => outputs.
And implicit as: learning_algorithm(inputs=> transformations => outputs)

Where instead of programmer finding necessary transformations, learning_algorithm does that job.

How does the learning_algorithm do that? It follows the loop of: guess => feedback => update.

It makes a guess of what transformation could be, then gets the feedback of how good it is, and then updates transformation based on the feedback. A similar loop is follow by the programmer in explicit coding, but now it is done by the learning_algorithm.

Obviously, programmer still specifies the learning_algorithm, so there's no magic, in both cases programmer fully runs the show. But with implicit coding it is done at a higher level of abstraction:

Explicit coding: programmer(inputs => transformations => outputs)
Implicit coding: programmer(learning_algorithm(inputs => transformations => outputs))

Why bother with that additional function? Well, because in practice it can solve a unique set of problem which explicit coding can't. (Specifically it started working in 2010s.) Think of task of identifying whether image has a bee. In principle programmer could find transformations that would do that well => some stupendous number of if/else loops should do the job. But in practice no one can or knows how to do it. (But in principle both coding paradigms are turing complete -- they can solve all computable functions. It is just that in practice the set of problems they can solve is really different, and that really matters.)

(Addition of the learning_algorithm also rhymes with a big trend of going at a higher level of abstraction, giving humans bigger leverage. => I won't even bother finding out how to do that thing and telling it to computer, I'll just tell it the goal, and it should figure it out.)

The end-goal of this progression is that you have some extremely capable learning algorithm, where all you need to do is tell it some goal (ideally in simple language) and it would figure out all the rest of the details and implement it. For example: "Yo, go build dyson sphere" AI: "Oh boy, well I'll need time at least till Monday" Two days after: "Alright, here it is".

For better or worse we do not have such learning algorithms. (In fact the end-goal is not just powerful learning algorithm, but self-improving powerful learning algorithm.)

Current ML algorithms (ML from machine learning, exactly what learning algorithm is about!) are better than nothing but still nothing as great as the end-goal we're going for of self-improvement.

So, how do you do this implicit coding?

In my research I was delighted to find out that the underlying process is the same both in explicit and implicit coding. It is that just when computer does some of the parts, different things come on the front.

In implicit coding:
1. You understand the problem.
2. You choose appropriate mathematical architecture for model (transformations). (Dance between assumptions, limitations, hypothesis space and compute availability.)
3. You give it random weights (generating random transformations as first guess).
4. You feed the input information and generate a first guess of an output.
5. You compare that output to desired output and generate feedback.
6. You feed feedback to the model that uses it to update weights.
7. You repeat that loop until good transformations (specifically weights cause you decide the mathematical archicture) are found.

Because of our current learning algorithms, which is a combination of what mathematical archictectures (from logistic regressions to deep neural networks) we came up with, what weight search algorithm we use, what feedback algorithm we use, etc.

So because of all of that we need to collect a lot of data of what are the inputs and what outputs we'd like to see. It is not only that this is used by the learning algorithm to find the transformations. It is that learning algorithm in finding right transformations actually also has to understand the phenomena about which it does transformations (that actually takes most of compute), especially because it learns from scratch.

Let's give an example.

Say our problem is that we want to identify tumor based on MRI scans. So the information transformation we want is: MRI scan pixels => transformation => tumor yes/no

Once we understand what is wanted from us, in implicit coding we'll collect shit loads of MRI scans and map each one to whether it had tumor or not. Then we'd pick a model (probably some deep NNs, not logistic regressions because hypothesis space has to be big enough to have viable solution), and we'll start making guesses with it with first random weights, and eventually shifting them to those that predict tumor well.

Now you'll say that while you might agree that programmer do a similar thing of making guess about transformation, then getting feedback of how good it is, and updating it. By no means they collect all the data like ML models do.

But this is the delightful thing I found. Both implicit and explicit coding follow the same process, it is just that implicit coding outsources some part to computer.

Imagine I'll try to use good old explicit coding to predict tumor based on MRI scans. We'll one of the first things I'll do is understand what MRI scans are. Then what are patterns that consitutes tumor, and then I'll pray to be able to translate those intuitions onto computer accurately.

What I did is I first had to learn the phenomena underlying the problem I'm solving, what MRI scans are, what constitutes tumor and so on. Because I'm 21 I already know a lot about MRI scans, so didn't need to learn that from scratch. And if I were to have spend several decades prior being a radiologist, I wouldn't even need to learn what signals tumor on an MRI scan -- I'd already had that knowledge.

But that work of: understanding the phenomena, and then understanding what transformations to do, need to be done __**from scratch**__ by the ML model. It didn't have decades of study and millions of evolution. And also its learning algorithm is shit compared to whatever we have in our brain. So it needs much more data to model the phenomena, and then find the appropriate transformations. 

I previously was confused by that. I thought, well sure thing implicit and explicit coding are both just about instructing computer, but why the hell they look so different: What's up with all the stupendous amount of data? What's up with the guess, feedback, update loop?

But then I realized that implicit coding just outsources those steps to computer (of course humans is still in the loop), and because in explicit coding it was done by humans, and our learning algorithm is so efficient and so well generalizable we rarely had to see those pain points of collecting enough data and so on. Hence, we never saw those parts as vividly, but they always were there!

Once we create better learning algorithms for computers they might need less data, we might not even to painfully collecting it, we could just give them the camera and say: figure it out! But that is not so for now.

So that's my grand explanation of implicit and explicit coding and how they are deeply unified, and how it all is just a bigger trend of creating better and better tools, increasing the level of abstraction.

Phew mamma mia.

Now once we have a fucking great big-picture model of what computers are, and how ML plays into it all, we can do into all the nitty-griddy details of how it works.  

Excited! That is the work for my next submission!

(Remember to talk/ think through the idea that the progress that is happenning from hard-coded scripts to basic ml, to deep learning and beyond is the outsourcing of knowledge generation about how to solve problems to computers. This is done mainly by better and better learning algorithms, algorithms that are more sample efficient, less compute hungry, and better generalizable.)
