# v1

# Goal
The goal is to revisit all studied ML.
I'll first try to re-explain everything I remember from scratch, then I'll go on and do flashcards to see what I missed.

## Questions
1. What is the set of problems that you can solve with traditional, explicit coding? How is it different from emerging, implicit coding? Is it true that the implict coding problem set is more important?
2. Is explicit and implicit coding the same in the limit because they're both turing complete? But just different practically?
3. How information theory is related to laws of physics, how deep is it?
4. Is it fair to say that in explicit coding the decision policy is explicitly written by us (basically the code we write?) whereas in implicit coding (ml) we give algorithm by which computer has to arrive at the decision policy. And is it then fair to say that the decision policy is basically a mathematical model which means some models are unfit to solve some problems (do certain information transformations due to being turing incomplete)
5. What is the balance between making models (decision policy frameworks) universal (turing complete?) to find the solution in the solution space and constraining them so the computation required for finding the solution doesn't take forever? How is computation is general related to solution space, search, how universal is it? 
6. How sparsity of feedback (noise to signal?) plays a role in finding solutions in solution space (i.e. creating useful models)?

# Debrief

----

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
