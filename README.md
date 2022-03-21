# BeeSpoiler

This is my first "home grown" project.
I started learning Python and Github a few weeks ago. To practice, I decided to create a script that finds words for the "Spelling Bee" game of the New York Times 
(https://www.nytimes.com/puzzles/spelling-bee)

The current version of the script correctly finds words that match the game rules (check link above) using a set of English words from the English Words module (https://pypi.org/project/english-words/).

However, since the word source doesn't include inflections (plurals, conjugated verbs, adverbs) it will not provide a full list of possible words.
For the purpose of this practice I'll consider it complete.

My first attempt at solving this involved creating a REGEX, but it soon proved too complicated for my current knowledge.

So instead I went for a strategy involving sets, which makes it easy to compare whether the unique letters of a word are a subset of the letters provided in the game.

Have a better (faster and/or more elegant approach)? 
