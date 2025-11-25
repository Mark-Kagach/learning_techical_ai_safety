# v3

# Goal
The goal is to revisit all studied ML.
I'll first try to re-explain everything I remember from scratch, then I'll go on and do flashcards to see what I missed.

This is the third version of this document. I'm trying to get right the broad framework (hanger if you may) for my understanding of ML. Once I get this framework right, it is much easier to then add the details and knowledge like types of models, mathematical theories and so on. 

I'll do now last round of re-explanations, and then add details like type of models and math if needed. After that I'll do flashcards to revisit anything I forgot.

--

Alight, have done a bit more working through the broad framework, but much more work to go. We'll continue with v3 later today.

--

## Questions of v1
1. What is the set of problems that you can solve with traditional, explicit coding? How is it different from emerging, implicit coding? Is it true that the implict coding problem set is more important?
2. Is explicit and implicit coding the same in the limit because they're both turing complete? But just different practically?
3. How information theory is related to laws of physics, how deep is it?
4. Is it fair to say that in explicit coding the decision policy is explicitly written by us (basically the code we write?) whereas in implicit coding (ml) we give algorithm by which computer has to arrive at the decision policy. And is it then fair to say that the decision policy is basically a mathematical model which means some models are unfit to solve some problems (do certain information transformations due to being turing incomplete)
5. What is the balance between making models (decision policy frameworks) universal (turing complete?) to find the solution in the solution space and constraining them so the computation required for finding the solution doesn't take forever? How is computation is general related to solution space, search, how universal is it? 
6. How sparsity of feedback (noise to signal?) plays a role in finding solutions in solution space (i.e. creating useful models)?

## Questions of v2
1. Is it fair to say they have the turing complete search space? Does that make sense? (the deep nn type of math models)

## Questions of v3
1. Are all tools fundamentally about giving person more power? Yes, bigger set of transformations?
2. When I think of the hypothesis space, is it fair to say that it starts with all the computable functions? Then one could apply some practical constraints of compute, time and (probably) data, and then we could continue constraining it based on math base equations we choose etc? 
3. Turing completeness vs software/ hardware. And turing completeness vs universal approximators.
4. When I talk about search and that it takes time and compute, how it relates to data? Is it fair to say that with bigger hypothesis space we need more data because data is signal whether you're on the right track or not? Right data and feedback are the cues to finding solution, without enough cues computer won't find solution?
5. And when we speak of compute here, what do we really mean? Just running the calculation of different math formulas, from making a guess (inference), to calculating the feedback function, the updating function and so on. This all takes time which is another resource. But how all this relates to data? Data is information/ clues to use to find the solution?

## Answers
1. 

--

# Debrief
1. How I think of hypothesis space (and how it would apply to humans) is different from how it applies to ml models. For humans I think of a sequence of actions, for models it is weight options, which is practically the final solution, there is no "walking" as there's with human actions, but actually you can say gradient descent walks.
2. When explaining things it is usually better to start from a problem that some idea/ technology is trying to solve, it makes things clearer. For ML especially it seems better to me to start with some problem you might want to solve, not with "we have a bunch of data...".
3. Spend more time understanding the difference between turing completeness and universal approximation, also how turing completeness relates to hardware and software. Because it is about simulating whatever turing machine can do, I presume it is about both, not any one in particular. Have too limiting hardware, you'll be incomplete, have too limiting software will be incomplete just as well. => For now I'll just think of limiting hypothesis space depending on the mathematical base equation we choose for our model, and that doesn't seem wrong. 

# v3

To start at the absolute start we have to talk about tools.

It all started when some chimp lifted up a rock or bone to use as a tool to either defend, attack or do something else. EXACTLY like that scene from Space Odyssey.

Humans descend from that chimp, and our defining unique characteristic compared to other animals is the __use of tools__.

Tools give you leverage, if something was hard to do with your body, we use tools to make it easier. Think about transportation on your two legs vs bicycle, plane or rocket. (=> Are all tools fundamentally about giving person more power? Yes, bigger set of transformations?)

Tools help to do different kinds of things. Some tools are about transportation, like trains and planes. Others are about construction, like hammer or bulldozer, or violence like guns. 

Thousands of years of human evolution, from fire to pyramids to industrial evolution, all lead to some british dude during industrial revolution called Charles Babbage. 

--

So we're in industrial revolution, britain is rocking and stuff. They have to sail a lot, and as you can imagine its pretty fucking hard to sail accurately without GPS. So sailors would calculate their position based on angles of celestial spheres. To do that calculation besides finding the angles of stars, they also need some complex math like logarithms, polynomial equations, trigonometry and so on.

Obviously sailors didn't do that math. It was all calculated to give a huge tables put in a book as a reference so sailor could use it to calculate their positions.

Calculating this table was an extremely tidious repetitive task. Obviously, a lot of mistakes were made. And this is pretty important mistakes, as even small mistake in navigation could lead to missing the island and hundreds of people dying.

--

So, now we come back to our british dude Charles Babbage. He was doing this calculations and he was real frustrated about the mistakes of others and tidiousness of the task. So, following the grand tradition of our chimp picking up a rock, he decided to create a tool that could do these calculations for humans (and also print those pages as there were many mistakes in transcription too...).

First he designed a tool to calculate several mathematical functions like polynomials, but this tool couldn't calculate all computable functions there are (a subset of all mathetical functions there are that can be solved by following some algorithm). This is still a crazy invention, but then in a decade or so he created a design that could calculate all computable functions, i.e. he designed a turing complete computer! In around 1830! Fucking hell! And moreover, eventually his designed was built, and it fucking worked! If only he was a better builder we could've had computers 100 years earlier.

Anyways. This tool that calculates mathematical functions for humans follows the grand tradition of our dear chimp picking up and using a rock. Only while rock is used say for violence, this tool of calculating math function is a tool of information. Fundamentally, calculating math functions is about transforming information. He called that tool a computer.

Computer thus, is a tool for transforming information. !

--

Turns out transforming information is insanely fundamental, it is deep to the laws of physics deep.

Hammer and rock is nice, plane is even nicer, but nothing is as powerful as computer -- the information transformer.

So what do we mean when we say trnasforming information? Well, all the obvious stuff. You give some information, you say how you want to change it, and then computer changes it to your desired final output. Input => Transformations (based on your instructions (i.e. software)) => Output.

Now we'll save ourselves some time and not talk about the parts of computer, bits and bytes or the hardware required and go straight to the meaty part of software.

As you have seen in our explanation, we need to tell computer how to transform information -- on its own it doesn't know what to do (obviously).

This instructing computer is called software engineering.

For the whole history of computation, from our boy Charles to practically 2010s, the way we instructed computer was by giving very explicit specific instructions step by step. First do this, then do that, then that.

But around 2010s a new paradigm was emerging, and it is useful to distinguish it. This paradigm had a new approach to instructing the computer. Instead of telling step by step how to do some actions, it was __teaching__ computer how to learn to do some task, not hand-hold it through it all.

We'll differentiate between those two ways of intructing computer as explicit coding, and implicit coding.

Explicit coding is what we've been doing for the past decades: give specific step by step instructions.

Implicit coding is the new paradigm that is arising from around 2010s: we teach computer how to do some task, but it generates the steps to solve the task, we just grade him when it does well.

--

But before I describe how this implicit coding works, let's talk about why should you care about it. Who cares how you instruct computer?

Because while in principle both types of coding solve the same set of problems: all computable functions, in practice it is different.

In practice we can't solve a bunch of problems with explicit coding. In fact, this type of problems are usually more interesting/ impactful! Think about a very important problem of identifying whether an image has a bee or not. 

In principle you can solve that with an ungodly amount of if elses loops, but in practice no human really can. And practice is all that matters, this type of implicit coding allows us in practice to solve such bee identification problems, and many more interesting things like speech recognition, robotics, self-driving and so on.

Since we have identified that in practice implicit coding has a much more interesting/ impactful set of problems it could solve, let's talk about how it works and how we could solve such problems.

🟡 => Good improvement for the future is to say that actually for most of life of "implicit coding" paradigm it just didn't work. What has changed in 2010s is that it actually started working in practice -- it actually started solving this interesting/impactful set of problems. Why this happened? I need to research that frankly, but I presume improvements in all three parts: better algorithms/ techniques, much more data, much more compute.

--

❗In describing this part (and ML in general) people start from data, but this is a poor approach. It is much better to start from a problem, and work your way from there.

To explain let's start with the problem. Say you want to identify whether image has a bee or not.

In implicit coding we'll broadly follow a three step loop to teach computer how to identify bees. First we'll show it an image and ask it to make a guess (yes/no), then we'll give it feedback (right/wrong), and then we'll ask it to update its guessing-algorithm. 

Excluding a whole world of ultra-important details this is how implicit coding works. 

--

Now let's add details to our guess => feedback => update loop.

First, making a guess.
To make a guess implicit coding comes back to its computational roots of mathematical equations.
We first have to define the mathematical equation (architecture, framework) in which our model will operate.
(To make things clear, I'll use word __algorithm__ to describe the whole process of teaching machine, and the thing we're trying to teach machine -- the steps it uses to solve some problem (like bee identification) as __model__.)

We choose mathematical equation based on the problem we're trying to solve. Choosing the right equation is a balance between universality and limitations. 

Imagine a circle that has all computable functions. You can call that cicrle the __hypothesis space__. It is the space of all possible functions we consider for solving our problem.

To solve our problem (bee identification) we need to search through that hypothesis space. But if we search the whole space it will take a lot of time and compute (search compute if you may). 

Depending on the mathematical equation we choose to base our model on we could limit that hypothesis space, which would mean we have to search through less things which means less time and compute required.

Depending on the problem and bottlenecks you have you might want to choose a very limiting equation for your hypothesis space. But the constrained hypothesis space still needs to have in it a viable solution, otherwise our search is useless. 

For example consider using linear regression as a mathematical based equation to identify whether image has a bee or not. With all our love to linear regressions it won't find viable answer! What that means? It means that the hypothesis space that linear regressions have is too limiting. 

(🔴 In fact, it is turing incomplete -- there is a whole load of computable functions it can't 🔴 => I'm confusing turing completeness and universal approximations, need to spend more time differentiating the two)

Yet, if you choose deep neural networks, then they are much more universal, their hypothesis space is much bigger, which makes them much more likely to find a viable solution to the problem, but that comes at a cost of search (i.e. time, compute). ❓ => How this relates to data? More search means more data needed? Seems like yes, but need to learn more.

But sometimes you need something as simple as guessing well the price of a house, and linear regression or polynomial regression we'll just fine of a job. You make an __assumption__ that the solution we'll be in this limited hypothesis space. That assumptions helps to find solution faster if it is well grounded in the problem/ data you're trying to solve.


# V2 after some research.

ML is implicit coding. Deep down its all the same as explicit coding -- both instruct computer, and both have the same problem set they can solve IN PRINCIPLE. 

It is all nice and well in the limit, but practice is what actually matters. And in practice implicit coding with ML type of solutions can solve a different set of problems which usually are more impactful (like bee identification), than explicit coding.

So, how do we do implicit coding? How do we __teach__ computer?

The main loop you run in teaching computer is: guess, feedback, update. But let's clarify that in several parts:

1. We define the mathematical model through which guesses will be made. Mathematical architecture defines the HYPOTHESIS SPACE. Limiting (non-turing complete) math models are things like linear or logistic regressions. What they do is heavily limit the hypothesis space, this saves a lot of search computation, and if the solution is in that limited space, all is well. But ocassionally it isn't, then you need turing complete math models, like deep neural networks. Their hypothesis space is much bigger, which means it takes much more search compute to find good solutions. => ❓Is it fair to say they have the turing complete search space? Does that make sense?
2. After we have defined the model architecture, usually computer makes a random guess. So now the goal is to fill that architecture with model weights that solve the problem. (To make the random guess we fill the model with random weights)
3. To do that after the computer has made first initial random guess, we give it feedback based on the data. Data is THE world to the model. It is the world in which model operates, from that world feedback is given. Of course we define the feedback function.
4. Once model receives the feedback, it takes the guess and the feedback, and changes its weights based on some function for updating its policy.
5. Then it makes another guess and so on. This loop is done until optimum weights are found for the given data and feedback function.

If your data is of poor quality, either poor features or not enough samples then the world in which model operates is too separated from the real life scenario you're trying to simulate. Too divergent world would mean model likely won't be useful in IRL.
Choose wrong math model, or fuck up the feedback function, or the updating function even with good data you won't find good useful weights.
In reality most of the machine learning engineer time is spend finding and cleaning the data, there is just a handful of models and feedback and updating functions that are frequently used.

Now that you understand this loop we can talk about supervised, unsupervise and reinforcement learning. These are the subtypes of ML, they all follow the algorithm we have described before, but there are some differences in what the data is, how feedback is generated and how updating is made.

Okay, tomorrow I'll continue with this document and finish putting details onto this framework. Once I'm done with that, some flashcards and back to practice learning.


# V1

Alright. 

Where do we start.

We start with coding. 

Coding is about telling computer what to do, so it then can do those tasks on its own. It is leverage for humans.

Computation is about giving some input to then be transformed via the given rules to produce the output. Instructing computer is software engineering. Just remember that whenever you give instructions they actually happen in the physical world on hardware. We do have much more complex things then bells and whistles for computers to do stuff, but fundamentals it is all bells and whistles executing your instructions.

In our instructions we have to be very explicit and specific: do that, get that.

We can call that explicit, specific instructing of computer traditional coding.

Traditional coding is amazing and allows us to solve a HUGE set of problems.

Yet there is also another big set of problems that can't be solved by giving explicit instructions. 

Think for example of a very important task of identifying if an image has a bee or not. It would be pretty hard to do with specific instructions and rules you give to computer, if there are yellow pixels then probably say bee? 

Yeah, it's hard to solve this type of problems with traditional, specific, explicit coding.

In fact, this set of problems is pretty big and probably more important and interesting than the set of traditional coding.❓

So, how should we identify bees on images?!

Here implicit type of coding comes in. We don't tell computer the specific step by step to arrive at the answer, but we give it the instructions on how to learn to do that task.

So while we didn't code explicit rules for computer to do to identify bees, we did give it the instructions for how to find and learn them on its own.

This is what machine __learning__ is about.

--

So how do we teach the computer?

There are three omni-fucking-fundamental bedrocks that all machine "teaching" instructions base on:
1. First computer makes a guess (based on (probably) random policy (the actual rules computer uses to identify if image has a bee or not))
2. Then it gets feedback on how good the guess was from environment
3. Then it updates the policy based on the feedback

We specify what is the initual policy, what is the environment, how we give to it feedback and how to update the policy. 

--

Policies can be VERY different. 
It is also called a model, because we are giving computer some framework (mathematical equation basically) which it uses to understand (model) the environment and reach some goal. => ❓ How correct is this?

Here comes an interesting balance. 

Depending on your environment and what goal you're trying to reach, some models/ policy-frameworks would be better than others. In fact sometimes you just won't be able to solve the goal with the wrong framework you give to computer.

Sometimes the mistake would be in some other place.

There is also an interesting balance between choosing a universal enough policy-framework (mathematical model) for computer to find the solution in the solution space, but also constrained enough so the computations don't take forever.
=> Or not happen at all beacuse the feedback is too sparse (far away from each other) to be useful?

Turing complete? Some mathematical models are turing complete? Like NNs?

--

So what are the different policy frameworks? => Is it just now linear regression, decision trees, neural networks, support vector machines, logistic regressions and so on??

If so then I need to describe how computer gets feedback from environment. Where environment is literally the data (data is computer's world), the worse data represents reality the less likely final model be useful!
And where we decide how to give feedback to computer, and it should be high-signal, not too noisy, sparse etc. to be useful.
And then we also need to specify how computer should update its policy based on the feedback, and you need to get that right too.

Then you could talk about how actually in practice day-to-day of an ML engineer most of the time is spend on crafting a good environment (collecting and cleaning the data) to then fit to just a handful of models to learn things with.

--
Alright I'll stop here, and start a new doc with answering questions and doing feedback.
