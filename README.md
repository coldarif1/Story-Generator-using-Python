# Story-Generator-using-Python
# 🚀🔍📅⏳💪😄🎉✨🌈💖🎈✨🏆
# How to build a Random Story Generator using Python?
In this section, we are going to make a very interesting beginner-level project of Python. It is a random story generator. The random story generator project aims to generate random stories every time user executes the code. A story is made up of a collection of sentences. We will choose random phrases to build sentences, and hence stories. 

Now, the pertinent question is - How we will do so? Its answer is very simple :

We will first put the elements of the story in different lists.
Then we will use the random module to select random parts of the story collected in different lists.
And then concatenate them to make a story.
We will make use of random.choice() function. Before starting, let's see an example of how random.choice() works.


import random
​
# list of books is stored in the list -'books'
books = ['Mother', 'Midnight Children', 'My experiments with truth']
​
# An item from the list 'books' is selected
# by random.choice()
print(random.choice(books))

Mother

Output
Midnight Children
As we can see, random.choice() function basically selects an item from a list of items. 

Following are the steps involved in this Random story generator project.

1. Import the random module, as it is a built-in module of python.  So, there's no need to install it manually.


# Importing random module
import random
2.  Define several lists of phrases. Here, we have defined eight lists. We can define more also, it depends totally on our choice.

Sentence_starter - This list gives an idea about the time of the event.
character - This list tells about the main character of this story.
time - This list defines the exact day on which some incident has occurred.
story_plot - This list defines the plot of the story.
place - This list defines the place at which the incident occurred.
second_character - This list defines the second character of the story.
age - This list defines the age of the second character.
work - This list tells about the work the second character was doing.
