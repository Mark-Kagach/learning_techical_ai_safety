# Flashcards

Different models have different approach to making predicitons. There are two types: instance based where training samples are learned by heart and compared to new instances; and model based, where training examples are made to create a generalizable model that is used to make predictions on new examples.

-- 

ml systems can be categorized based on three dimensions:
1. supervision during training -- are there labels in the training data? (or how much labels there are, as it is more of a scale, than binary)
2. approach to making predictions -- instance vs model
3. increment vs batch learning -- can model incrementally take new information and learn, or it has to be retrained from scratch everytime one adds training data?

-- 

There are several types of training supervision:
1. supervised -- data has desired labels
2. unsupervised -- data has no labels
3. semi-supervised -- part of data has labels
4. self-supervised -- we create labels from an unlabeled dataset, for example by doing masking on images (this is done usually to then do transfer learning)
5. reinforcement learning -- agent perceiving environment and performing actions to gain rewards.

--

ML projects are about capturing some instance of nature, and then using a model to find some useful trend/ pattern.

Thus a few things can go wrong:
1. while you captured nature without mistakes, the instance that you have captured is nonsense: think white noise, or number of hairs on a fly.
2. your capturing was poor: too much noise, not enough examples, poor features etc.
3. the model you've chose is either to simple or too complex to capture the trend at the right level of complexity to be useful 

-- 

testing and validation are important parts of ML. They try to check how well your model will do in the real world, we do that by checking it on a new unseen data (that is hopefully representative of real life cases). Validation is used because if we try to choose the best model based on the test set scores, we'll overfit exactly that test-set, which means poor generalization to real life. So we choose best model based on validation set, which can also be overfit, so we use cross validation of taking different parts as validation sets, training models several times and taking the average score as decisive metric.