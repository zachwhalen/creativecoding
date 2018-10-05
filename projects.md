---
layout: single
title: Projects
permalink: /projects/
toc: true
---

In this class you'll be completing several smaller projects throughout the semester -- about one per week -- and then you'll select and revise your best work to include in a final portfolio.

## Project: Bot
Make a bot for Twitter or Mastadon. It can be text or image-based, but it should be meaningful in some way. I suggest using Cheap Bots Done Quick, but might also want to consider [Tweepy](http://www.tweepy.org/) or a hosted bot with [Glitch.com](http://www.glitch.com), bearing in mind that Twitter's API constraints may make this route untenable.

(NB: If you want your bot to live in Mastadon, I recommend the [botsin.space](http://botsin.space) instance.)

### Criteria
* To receive credit, your bot must 
  - Be creatively compelling in some way
  - Post automatically to Twitter at least twice a day
  - Be capable of generating at least 100,000 unique permutations
* **Workshop:** Wednesday, September 5
* **Final Version Due:** Friday, September 7

### Example: Bots with CBDQ

The Twitter account, [@RRAAAAARRL](http://www.twitter.com/RRAAAAARRL), is a bot that tries to sound like [monsters from old comic books](http://comicbookplus.com/?dlid=12518). I made it in CBDQ, so you can [view the source there](https://cheapbotsdonequick.com/source/RRAAAAARRL), or if you prefer, [as a JSON file](https://github.com/zachwhalen/creativecoding/blob/master/examples/rraaaaarrl.json). There's not much to it.

[@HouseBudgets](http://www.twitter.com/housebudgets) is also a [CBDQ bot](https://cheapbotsdonequick.com/source/HouseBudgets), with some more complicated things going on [in the code](https://github.com/zachwhalen/creativecoding/blob/master/examples/housebudgets.json).


## Project: Remix
For this second project, write some code that appropriates some text, transforms it in some way, and present the resulting output as poetry. You may use command-line tools, write a Python script, or some combination thereof.

In other words, you have two things to figure out:
 * A source -- anything that is not already poetry
 * A method -- a process for transforming that into poetry.

That method involves both the concept (i.e. "Select from a list of all of the adjectives and nouns in _Frankenstein_") and some Python code to realize that concept (see below)
.
I encourage you to use books from [Project Gutenberg](http://www.gutenberg.org) as your sources, but please feel free to think more expansively than that. Just about anything can become poetry! I've already demonstrated how to work with [Python's random](https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python) functions, and we'll try some other things like [text parsing with TextBlob](https://textblob.readthedocs.io/) and other poetic algorithms.

### Criteria
* A Python program that takes non-poetry input and prints out poetry
* A blog entry that
  - includes some sample output, explaining its poetics
  - describes your process, including annotated source code
* **Workshop:** Friday, September 21
* **Final Version Due:** Monday, September 24

### Example: Frankenpoem

View, run, or modify as a [Jupyter Notebook](https://github.com/zachwhalen/creativecoding/blob/master/examples/Franken%20Poetry.ipynb) or a [Python 3 Script](https://github.com/zachwhalen/creativecoding/blob/master/examples/frankenpoetry.py).

Sample output:

<blockquote><pre>placid skiff
considerable youth

new month
prosperous society

mutable misery
good reality

only map
guilty night
</pre></blockquote>



## Project: More Poetry? Oh, Noetry!

Whereas the [Remix Project](#project-remix) welcomed a broad definition of poetry -- especially free verse and minimalist styles -- this third project challenges students to create a program that will generate poems following the constraints (meter, rhyme, structure) of a poetic form of their choice.

### Criteria
* A Python program that creates poetry in a specific form.
* A blog entry describing the program, demonstrating sample output, and linking to the annotated source code.
* **Final Version Due:** Friday, October 5

### Example: Secret Peaches

This is a series of videos, but I'm also sharing the relevant notebooks in [the examples folder](https://github.com/zachwhalen/creativecoding/tree/master/examples).

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLu8zaGaJFFipsk-bO96AjWghP0EnOCrej" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Project: Glitch 
"Glitch Art" is a general category of data manipulation that changes images into something else. The results are messy, chaotic, and unpredictably ａ ｅ ｓ ｔ ｈ ｅ ｔ ｉ ｃ. In this project, you'll experiment with different glitch methods -- some based in software, some based in code -- to convey a specific idea, narrative, or theme in 8 - 20 images. For the purposes of this project, please avoid off-the-shelf "glitch" apps as these are working against the basic themes of this project. Instead, please use at least two of the methods listed below to produce 8 - 20 glitched images.

### Glitch Methods
 * **Databending**. Use software designed for something else to mess with image files. [Audacity](https://www.audacityteam.org/download/), WordPad, and TextEdit are popular options.
 * **Pixel sorting**. Use a [Python module](http://satyarth.me/articles/pixel-sorting/) to rearrange the pixels of an image according to different criteria to produce [a surreal effect](http://www.twitter.com/crookedcosmos).
 * **Datamoshing**. Manipulating structural data in media files, especially video, to [produce interesting and often disturbing alternatives](https://twitter.com/youtubeartifact).

### Project Criteria
 * 8 - 20 glitched images using **at least two** of the methods listed above
 * A gallery of these images presented or arranged meaningfully.

## Project: NaNoGenMo


## Project: Screensaver

## Project: Clock

## Final Portfolio

