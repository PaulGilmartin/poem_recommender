# poetry_analysis

# What is this?
A poetry recommendation service! This is a very simple tool which, given a (correctly formatted, english-language) poem, recommends to the user another poem with a similar form and structure.

# What's the motivation?
Aside from being a RAGE challenge entry, this is an extremely simplified (and very rushed) version of an idea I had for a potential hip-hop/grime recommendation service.

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
from poetry.recommend_poem import recommend_poem
recommend_poem("""After killing
a spider, how lonely I feel
in the cold of night!""")

Some info about your poem:
Rhyming Scheme:(), Syllable Scheme:(set([5]), set([6]), set([5])), Form:  HAIKU

A similar poem you might like:

From across the lake,
Past the black winter trees,
Faint sounds of a flute.



recommend_poem("""A cool wind blows in
With a blanket of silence.
Straining to listen
For those first few drops of rain,
The storm begins in earnest.""")

Some info about your poem:
Rhyming Scheme:(), Syllable Scheme:(set([5]), set([7]), set([5]), set([7]), set([7])), Form: TANKA

A similar poem you might like:

Subtle hints of spring
In the wet bark of the tree
Dew dripping from leaves
Then runs down the russet trunk
Pools round the roots and is drunk


recommend_poem(""""There was a young rustic named Mallory,
who drew but a very small salary.
When he went to the show,
his purse made him go
to a seat in the uppermost gallery.""")

Some info about your poem:
Rhyming Scheme:('A', 'A', 'B', 'B', 'A'), Syllable Scheme:(), Form: LIMERICK

A similar poem you might like:
There once was a young lady named bright
Whose speed was much faster than light
She set out one day
In a relative way
And returned on the previous night.


recommend_poem("""And then the day came,
when the risk
to remain tight
in a bud
was more painful
than the risk
it took
to blossom.
""")

No recommendation found, but here are some facts about your poem:

Rhyming Scheme:('A', 'B', 'C', 'D', 'E', 'B', 'F', 'G'), Syllable Scheme:(set([5]), set([3]), set([4]), set([3]), set([4]), set([3]), set([2]), set([3])), Form: Unclassified
```

