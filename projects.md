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

## Project: Glitch Gallery
"Glitch Art" is a general category of data manipulation that changes images into something else. The results are messy, chaotic, and unpredictably ａ ｅ ｓ ｔ ｈ ｅ ｔ ｉ ｃ. In this project, you'll experiment with different glitch methods -- some based in software, some based in code -- to convey a specific idea, narrative, or theme in 8 - 20 images. For the purposes of this project, please avoid off-the-shelf "glitch" apps as these are working against the basic themes of this project. Instead, please use at least two of the methods listed below to produce 8 - 20 glitched images.

### Glitch Methods
 * **Databending**. Use software designed for something else to mess with image files. [Audacity](https://www.audacityteam.org/download/), WordPad, and TextEdit are popular options.
 * **Pixel sorting**. Use a [Python module](http://satyarth.me/articles/pixel-sorting/) to rearrange the pixels of an image according to different criteria to produce [a surreal effect](http://www.twitter.com/crookedcosmos).
 * **Datamoshing**. Manipulating structural data in media files, especially video, to [produce interesting and often disturbing alternatives](https://twitter.com/youtubeartifact).

### Project Criteria
 * 8 - 20 glitched images using **at least two** of the methods listed above
 * A gallery of these images presented and arranged meaningfully.
 * A blog entry explaining your glitch methods and the intent behind your arrangement.

## Project: Screensaver
"Screensavers" are (or were) a way to save energy and avoid the ["burn-in"](https://en.wikipedia.org/wiki/Screen_burn-in) damage that can happen to CRT monitors when they display the same imagery for long periods of time. While we're more likely today to have a simple slideshow, an inspirational quote, or maybe a clock, and we've probably configured that with software built in to our operating system, it used to be the case that users would download custom software like ["After Dark"](https://en.wikipedia.org/wiki/After_Dark_(software)) specifically for this purpose.

In this project, your goal is to create an interesting, looping animation in the style of a screensaver using p5.js. You should create and share this using the online p5.js editor: [editor.p5js.org](http://editor.p5js.org), which you can sign into with your Github account.

Your screensaver can be abstract or representational. It can be fully scripted or random. It can be completel novel, or it could be a recreation of a classic screensaver. It can be completely self-contained, or it can pull in live data from an external source. 

All of these things are possible with p5.js. Whatever you choose, keep in mind the target audience of the HCC media wall, and plan it to last for at least 5 minutes.

### Project Criteria
 * A project created and shared with the p5.js web editor
 * A canvas set to 1920x1080 so that it fits the media wall
 * Something that stays interesting for at least 5 minutes
 * A blog entry describing and embedding the final project
 * A final version by **Nov 2, 2018**.


## Project: NaNoGenMo
NaNoGenMo or "**Na**tional **No**vel **Gen**eration **Mo**nth" is an annual challenge in computational creativity. It started in 2013 with [a tweet from Darius Kazemi](https://twitter.com/tinysubversions/status/396305662000775168), and it's been running [in Github](https://github.com/NaNoGenMo) every year since.

The rules are simple:
 * Write code that generates 50,000 words
 * Share your final product and your code

There's a wide range of complexity among the 399 successfully-completed novels, and we'll spend some time looking at different approaches.

For this project, you may choose any language or system that works, but I recommend Python since we've been working with it already. I encourage you to publicly in [the official NaNoGenMo Github thread](https://github.com/NaNoGenMo/2018/issues) (it's a friendly community), but this isn't mandatory.

Here's what **is** required:

### Project Criteria
 * A program that generates at least 50,000 words 
 * ... and saves that code as a TXT or PDF file
 * A blog entry describing your project
 * Your source code in Github
 * All by **November 19, 2018**.

## Project: Clock

Is time continuous or discrete? Why do we insist on dividing it into units of hours, minutes, seconds? Why are there 60 minutes in an hour, but 24 hours in a day? And why do we so often use circles to represent the passing of time? Why is the 7-segment display so ubiquitous for digital representations of time?

In this project, your goal is to use p5js to create a graphical representation of the current time with as much ingenuity, novelty and coding skill as you can muster.

By drawing on [the history of marking and representing time](http://www.cabinetmagazine.org/issues/29/foer.php) and [some contemporary artistic examples of time representation](https://github.com/golanlevin/lectures/tree/master/lecture_clock), and by building on the coding skills you've been developing all semester, make something interesting, provocative, or useful in software.

### Project Criteria
 * A p5js sketch that represents the current time.
 * A blog entry describing your work in the context of prior art and acknowledging any influences, inspiration, or tutorials you relied on.
 * Your source code shared in Github.
 * All by **December 5, 2018**.

## Final Portfolio

The final portfolio stand in place of a final examination for this class, and as such it is a significant project in its own right. It is intended as a cumulative summation of the skills you've developed this semester. More than simply a list of all of your projects, this portfolio should be a thoughtful presentation of the _best_ work you completed this semester, revised and improved since its first submission.

One of the learning outcomes for this class is that students should be able to "_Be able to speak about their creative work critically -- both process and product_," so this portfolio is your demonstration of that ability. As a general reflection, it is also a demonstration of how you can "_Reflect on the value of the creative process_."

To complete this portfolio, identify **at least four** of your projects from this semester that you'd like to improve somehow. These could be your favorite projects, the projects with the most room to grow, or the projects that were never quite completed to your satisfaction. 

Then, do whatever work you need to improve each of those projects in some way, whatever "improvement" means for you in the context of each of those project's parameters. 

Create a page or series of posts on your website, Github, or elsewhere to make those newly-revised projects visible along with any other projects you wish to feature. This could be a "portfolio" page on your website, for example.

Finally, write a blog post or Github page where you describe your four improved projects noting what changes you made and reflecting on what makes the newly improved version of each project more successful or valuable. Reflect generally on how you approached the revision process including how you selected the projects, how you chose to revise and how the new version better meets your personal goals for the project. 

You should also include any general reflections on the class and describe what you learned about creative coding and yourself as you worked on the various projects this semester. 

Submit the URL for this final blog post in Canvas by 11:00 on Friday, December 14.

### Project Criteria
 * At least four revised and improved projects.
 * A central place on the web featuring your creative coding projects.
 * A blog post reflecting on your projects and describing your revision process.
 * All submitted to Canvas no later than 11:00 on Friday, December 14.