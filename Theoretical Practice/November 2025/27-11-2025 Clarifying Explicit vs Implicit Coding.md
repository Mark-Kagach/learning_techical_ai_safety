# Goal
The goal of this practice is to really understand and have a framework of thinking about explicit and implicit coding. 

I can talk about each independently, but I am confused when trying to describe them together -- what are the unifying trends? What principles apply to both?

Both are about instructing computer, so treating them as alien things seems wrong, there's a way to perceive the two together, nicely and cohesively. I want to find, understand, and integrate that way.

## Questions

## Answers

# Debrief

# Explanations

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

Now let's consider how this would've been done with explicit coding. Say I will code that identificator, and I know nothing about tumors. Well it seems only reasonable that the first thing I'd need to do is to look at quite some number of scans, understand what signal tumor and what doesn't. Then I'll try to encode those ideas as code.

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


![photo_5280615570237754568_y](https://github.com/user-attachments/assets/4ddd9ff5-ebee-4a09-8957-b710941fd430)
![photo_5280615570237754567_y](https://github.com/user-attachments/assets/a7f5118d-010e-41d7-9046-0dd2a48b19ed)
![photo_5280615570237754566_y](https://github.com/user-attachments/assets/3d202c92-df76-496e-9214-9309229b3582)
![photo_5280615570237754565_y](https://github.com/user-attachments/assets/d3b65fc2-6909-41f3-8c5f-80f932f4add4)
![photo_5280615570237754564_y](https://github.com/user-attachments/assets/069f6867-5e60-479a-8249-7d45fda5d1b7)
![photo_5280615570237754563_y](https://github.com/user-attachments/assets/05e40a1e-6a62-4365-a70e-2e6f3d6f8f5e)
![photo_5280615570237754562_y](https://github.com/user-attachments/assets/686ece83-4ee7-4b5f-9a5e-2a08444196cc)
