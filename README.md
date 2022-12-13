# LING-L645
Practical repository for LING L-645
-For Matthew

**Project description**

See ./project for project files

*An RNN-Transducer for Russian character prediction*

There are some cranky parts which have been resistant to change, but here is
the main gist of the project.

Since there aren't any libraries to efficiently implement an RNN-transducer
on arbitrary data. This is an extension of the project that I've attempted
to implement, but that sort of thing will take a little bit longer.

The project is as follows right now: slightly broken.

Currently I'm trying to concurrently set up a framework with can accept
arbitrary models for the predictor/encoder/joiner that's not just setup
for speech recognition.

The predictor can be toggled between a feedforward network (whose training
phrase gives some poor results for currently unknown reason, like 3%
accuracy) and a probabilistic model
(which gives 25% accuracy on text data). The output of these networks is a
softmax over the entire alphabet + null character.

The encoder model is set up as a Bi-LSTM, though I wonder about the efficacy
of this to just process a vector which represents individual characters. The
output is a (hopeful) encoding which helps the joiner network decide on which
character to predict.

The joiner model is a simple feedforward network which takes in the predictor
and encoder model's output and outputs another softmax over all characters in
the alphabet + null character.

The file 'orthographies.txt' contains all the separate orthographies I was able
to find/come up with on my own, and the code generates a new textfile to train
on based upon randomly selected orthographies

The results aren't in yet - this is still a work in progress as I figure out
pytorch and its various libraries and work out beam-search and work out loss
function implementation across the networks.
