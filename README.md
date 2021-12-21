# Well-formed Limericks and Haikus with GPT2
## 📜 GPT-2 Rhyming Limerick and Haiku models using data augmentation
### In collaboration with Matthew Korahais & Daniel Korsunsky
### Abstract 
We explore the capabilities and limits of GPT-2 in the case of well-formed poems, specifically limericks and haikus. We hypothesized that GPT-2 trained without phonetic annotations would be unable to systematically learn and generate syllabic patterns and rhyme scheme, since these features are grounded in real world acoustic representations. Our model trained with list-of-rhymes annotations outperformed baselines, generating perfect-scoring limericks 33\% of the time. Our best haiku model generated valid haikus in 29\% of cases, with an average syllable error rate of $<$0.4. Our work invites further research into methods of combining text and phonetic data for more convincing text generation.

Limericks Colab here -> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Rr4F4XSNZhC1jOVnUWHa0a3e9cQhEVvx?usp=sharing)

Haiku Colab Here -> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1dY9eVMSHkeReJaDfl3YoQJG66DZxybcG#scrollTo=aeXshJM-Cuaf)

Evaluation Data Here: https://docs.google.com/spreadsheets/d/1rd1qCbCcTX1zHa0Dvh1q8OJ2iidxxrifTJlYWg3MMes

### Examples (Find more in the repo):
#### Limericks
``` (generated with first line as prompt)
To the one grading our research, I'd say,
that a lot of work's been done today.
our paper's been checked,
And our work is all correct.
We're not mired in conjecture today.
```
```
The Indians' chief deity, they say,
Was a god of the earth all day.
But the gods he made
Were the ones who would fade
As they were replaced by a new way.
```
```
A large, thick, thick, and thickly cut tree
(A weeping cedar) will please me.
It's a tree that's known
As a cedar it's own,
And it's named for a bird that I see.
```


#### Haiku
```
The only thing that
gets me going is you So
let's keep this going
```
```
Saw a duck come in
from the woods and now i know
what a duck is lol
```
```
the only thing I
wanna say to you is good
bye don't disappoint
```
