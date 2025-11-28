# Goal
The goal of this practice is to really understand and have a framework of thinking about explicit and implicit coding. 

I can talk about each independently, but I am confused when trying to describe them together -- what are the unifying trends? What principles apply to both?

Both are about instructing computer, so treating them as alien things seems wrong, there's a way to perceive the two together, nicely and cohesively. I want to find, understand, and integrate that way.

## Questions

## Answers

# Debrief

# Explanation v2

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

![photo_5282867370051440005_y](https://github.com/user-attachments/assets/4bff01a0-86b7-45e0-9c1b-9cfd2070348d)
![photo_5282867370051440006_y](https://github.com/user-attachments/assets/7cf65440-ce84-4855-87c5-fe69e3723cbf)

# Explanation v1

If explicit coding is: input => transformations => output
Then I like to perceive implicit coding as: learning_algorithm(input => transformations => output)

Where learning_algorithm is trying to find the desired transformations. And the way it does that is by following the three step loop of: guess => feedback => update.

( Oh wow.
You could say that in explicit coding that transformation search of guess => feedback => update is done by programmer. => programmer_search(input => transformations => output)
Not sure how insightful that is. )

What I was confused by, is the staggering difference between the two when it comes to data demand. In explicit coding it is practically non-existent, where in implicit coding (ml) it is half of the whole thing. 

So where that whole half disappeared for explicit coding⁉️

After thinking for a bit and talking to some friends I think there's a good, pretty insightful explanation.

Let's consider two ways we could go about automating medical diagnosis. 

First imagine the implicit coding, we do the basic ml stuff: understand the problem, collect shit loads of good, representative data, choose the right model and train it. And voila we have automated medical diagnosis. Say tumor identification based on MRI scans.

Now let's consider how this would've been 
done with explicit coding. Say I will code that identificator, and I know nothing about tumors. Well it seems only reasonable that the first thing I'd need to do is to look at quite some number of scans, understand what signal tumor and what doesn't. Then I'll try to encode those ideas as code.

(Interestingly, I would need just as an ML algorithm a representative sample of the whole distribution, not just one small part of it. But the difference would be that I would need much less samples. Or is it that I wouldn't even need whole distribution because humans are SO great at generalization? Hm.)

So in both cases there's a need to understand the phenomena that problem is about. The difference is that whatever learning algorithm humans have in their head is light years more efficient (in practically all the ways) than what current machine learning techniques use.

So the step of understanding the phenomena rarely comes to be visible in explicit coding, but IT IS there. Hence, the difference in data demand is explained by (1) humans usually have all the needed knowledge about phenomena, so nothing is needed to be learned, (2) if it needed to learn, humans are so much more sample efficient and generalize so much better than machine that it is rarely so starkly visible.

So all the collected data does two huge jobs: first it __models the phenomena__, second it __helps to find the right transformation__ serving as clues.

In modeling phenomena, the data we feed into the ml model, is literally the whole world for the model. The better data is, the less noise there is, the better features are, the more samples, the more it is well-representative of the distribution, the better. As this artificial world generated for model is closer resembling the real world phenomena that we're interested in. Hence, it means that found transformations are likely to be useful in real life. 

It also serves as feedback about which guesses work, and which don't. Similar to coder trying different functions and seeing whether they work.

In this perspective, both coding paradigms deep down follow the same process, just depending on how much computer or human is involved different parts become more or less prominent.

So what is the underlying unifying process?

1. Start with understanding the problem (regardless explicit of implicit coding it is). For example, understand you're trying to identify tumors only by using MRI scans.
2. Collect the data or learn on your own to understand (model) phenomena the problem is about. Collect MRI scans with targets for ML model, or do the same to teach yourself what signals tumor (maybe read textbooks etc).
3. Start making guesses of solution (right transformation). ML model or explicit coding, you'll need feedback on how well your transformations are doing.
4. Run the guess => feedback => update loop until you get good transformations. This is true for ml just as much as for programmer.

Let's try again explaining.

Explicit or implicit coding, deep down they follow the same process. Broadly, it is about understanding the problem one is trying to solve, understanding the phenomena it is about, making guesses of solutions, receiving feedback, and updating those guesses until satisfactory solution is found.

Humans have a different learning algorithm than machines, so types of data, its amount, or its quality could be different from what one would collect for ML algorithms. But deep down programmer or ml model, are pursuing the same goals: they are trying to understand the phenomena, and they are trying to get feedback on their guesses. 

--

I've done some more research, and this separation of first understanding phenomena, and then finding transformations that solve the task is in fact what models do (https://www.perplexity.ai/search/goal-in-the-past-4-versions-i-0JoK9BwrRP..tPDjeGCOYQ#0):

> The evidence strongly supports that large data requirements in ML stem from a fundamental difference between explicit and implicit coding: models must learn the phenomena structure before they can find transformations, while programmers already have this knowledge encoded in their heads.

> Transfer learning provides the most direct proof of this separation. When you take a model pre-trained on ImageNet (trained on 14+ million images), it has already spent massive computational resources learning what images look like—the structure of natural visual phenomena. Early layers in this model encode edges, textures, shapes, and spatial relationships. When you then fine-tune this model on a new task with only hundreds of labeled examples, it doesn't need to re-learn the phenomena; it only needs to learn the transformation mapping those phenomena to your specific task labels. This is why pre-training reduces downstream data requirements from thousands to dozens.​
Few-shot learning confirms this principle. With only 2-5 labeled examples, models can adapt to new tasks if they've been pre-trained. One-shot learning (single example per category) and even zero-shot learning (no examples, just descriptions) work by relying on previously learned phenomena structure. This is impossible if the model still needs to discover what the world looks like—it only works because that discovery already happened during pre-training.


>   Phenomena modeling phase: Model discovers structure in data (manifolds, causal patterns, feature hierarchies). Requires substantial data because hypothesis space is immense. This is what pre-training accomplishes.
    Transformation search phase: Model finds the specific mapping from discovered phenomena to task outputs. Much more data-efficient because the structure is known. This is what fine-tuning or few-shot adaptation does.
    The data difference: Explicit coding front-loads phenomena knowledge (in programmer's head), so you only need data for transformation search (test cases, specification examples). Implicit coding must do both simultaneously from scratch, hence requiring vastly more data—unless you use transfer learning to reuse previously learned phenomena understanding.
    This explains why your radiologist example works: the radiologist brings phenomena knowledge (learned over decades), so coding can focus on transformations. ML models need both, which is why they're called "data hungry" for phenomena they've never seen, but become data-efficient once pre-trained on similar phenomena.


Or this alexnet example from grok(https://grok.com/share/bGVnYWN5_51affaf7-b502-427e-9d89-66f57a69bf38):

> Best concrete example to feel this viscerally
ImageNet classification (the classic benchmark that birthed deep learning).
Explicit coder approach (pre-2012):
Hand-design features (SIFT, HOG), then SVM on top. Worked okay (~75 % top-5 accuracy). The human who wrote SIFT already knew that edges, corners, textures matter — they baked the phenomenon understanding into the code.
Deep learning approach (AlexNet 2012 → modern):
Start with random weights. Show the net 1.2 million real images labeled with 1000 classes. Nothing else. After ~6 days of training it reaches 85 %+ accuracy and blows away all hand-engineered systems.
What happened in those 1.2 million images?
First ~30 % of training: the net learns basic phenomenon stuff — edges, colors, textures, parts of objects (this is what the lower layers converge to).
Remaining 70 %: it learns higher-level combinations — eyes + fur + whiskers → cat detector, wheels + windows → car detector, etc.
The exact same images are doing double duty: teaching “what images even look like” and “which parts belong to which class”.
If you pre-train the same network on 400 million unlabeled images first (like modern CLIP or DINO), then fine-tune on ImageNet, you suddenly need only ~10–50 images per class instead of ~1000. Because Phase 0 is already done.
That is the cleanest proof that your intuition is correct.
So your final synthesis should be:
Machine learning feels like it needs absurd data only because we historically forced models to learn the world from scratch at the same time as learning the task. Once we give them a proper Phase 0 (strong unsupervised world model), they become dramatically more data-efficient — often human-level or better on Phase 1. The “data heaviness” is not fundamental to implicit coding; it’s an artifact of poor separation of concerns. We’re finally fixing it.

or similar insight from claude (https://claude.ai/share/f3d2ec23-1cec-45d7-a513-1e349bddbe3c):
> The Key Insight You're Missing
Modern ML increasingly separates these concerns through pre-training and fine-tuning:
Pre-train on massive general data (building representations, like human childhood)
Fine-tune on specific task with much less data (like professional training)
When you do this, the amount of task-specific data needed drops dramatically - sometimes to human-like levels or even less.
So your dichotomy between "understanding phenomena" and "finding transformations" is actually describing the same thing at different levels of abstraction. The "transformations" the model learns early (in pre-training) ARE its "understanding of phenomena." The transformations it learns later (fine-tuning) are the task-specific mapping.

When ML model "models the phenomena" it is called representation learning?

I like this cursor synthesis:

> Data in ML serves three roles:
Defines the phenomena (what is a tumor? what patterns exist?)
Constrains the search (these weights work better than those)
Compensates for lack of priors (no built-in physics, causality, language)

> Humans need less data because:
Massive evolutionary priors (vision, physics, social reasoning)
Can receive compressed knowledge (language, diagrams, explanations)
Strong causal reasoning (can generalize from few examples)
Transfer learning (every experience informs every other task)

And besides conversation on why ML models are so data hungry, because they learn from scratch, learning algorithm is not as good as for humans, and they have to both understand the phenomena and then learn desired transformations (where most of compute is spend understanding phenomena interestingly). Explicit vs implicit coding difference in where "phenomena modeling" happens:

> **Explicit Coding:**
- **Learning happens in YOUR BRAIN** (before you write code)
- You observe the phenomenon, study examples, understand patterns
- You encode your understanding into explicit rules/algorithms
- Data is used for **understanding** (you look at it) and **validation** (you test your code on it)
- But the algorithm itself comes from your reasoning, not from the data directly

> **Implicit Coding (ML):**
- **Learning happens in THE COMPUTER** (during training)
- Computer observes the phenomenon through data, studies examples, finds patterns
- Computer encodes its understanding into weights/parameters
- Data is used for **learning** (computer extracts patterns from it) and **validation** (you test the model on it)
- The algorithm (weights) comes from the data directly, via the learning process

The question of whether code (explicit or implicit) always models phenomena of nature is useless. I err on the side that it always does, as any math is also part of nature.

