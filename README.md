
# What is this?
A poetry recommendation service! This is a very simple tool which, given a (correctly formatted, english-language) poem, recommends to the user another poem with a similar form and structure.

# What's the motivation?
This is an extremely simplified (and very rushed) version of an idea I had for a potential hip-hop/grime recommendation service.

# How does it work?
Given an input poem, the tool computes its stanza, rhyming and syllable schemes (i.e. the number of syllables in each line) (this is acheived using the pronouncing module (https://pronouncing.readthedocs.io/en/latest/), a nice API to the more general nltk python module). It then attempts to classify that poem (based on these schemes) as a well-known form. Currently, the tool is able to recognize Haikus, Tankas and Limericks. If the form of the poem is recognized, we choose a random poem of that type (out of the list of saved poems of that type in the corresponding csv file) and recommend it to the user. If the form is of the poem is not recongized, we attempt to find a poem with a similar rhyming and syllable scheme in the 'unclassified form' csv file and recommend that to the user (this bit is very much work in progress).

Each time a new poem is entered into the tool, it is saved in the corresponding cvs file to be potentially read for later use. This means, theoretically at least, that recommendations should become better and more varied the more often the tool is used.

# How do I use this tool?
Navigate to recommend_poem.py and enter your desired poem into the recommend_poem. You may need to install the pronouncing module

# Caveats
This is very much incomplete and has been done with very little time to spare. It isn't very useful at all just now, but I think it could be built into something a bit more fun.
Note that the poem will need to contain all english language words (no slang) in order for this to work correctly. 

# Example output
```
from recommender import recommend_poem_to_user
haiku = """An old silent pond...
A frog jumps into the pond,
splash! Silence again.
"""
recommend_poem_to_user(haiku)
Here are some facts about the structure of your original poem:
Rhyming Scheme: (('A', 'A', 'B'),)
Syllable Scheme: (({5}, {7}, {5}),)
Poem Type: HAIKU
Based on this cirteria, we think you may enjoy the following similarly structured poem:
Don't weep, insects -
Lovers, stars themselves,
Must part.

```

