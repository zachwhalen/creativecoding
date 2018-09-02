---
layout: single
title: Getting Your Bot Ready for the Workshop
---

On Friday, you created a [Twitter account](http://www.twitter.com/) for your bot, and you got started programming your bot in Tracery with _[Cheap Bots Done Quick](http://www.cheapbotsdonequick.com)_. There's not school on Labor day, so we'll next see each other on Wednesday, September 5. Since your complete bots are due on Friday, September 7th, class on Wednesday is dedicated to a peer review workshop of your bots.

As this is a _review_ workshop, your bot should be complete. You should be beyond the point of troubleshooting your bot and moving into revising, expanding, and improving your bot. If you still need help getting your bot set up, get that sorted out before Wednesday.

If you haven't already, you should [review the criteria your bot should meet](https://zachwhalen.github.io/creativecoding/projects/#project-bot) before it's considered complete.  If you're bot isn't doing those things, then figure out what you need to do to make it complete before class on Wednesday.

### Here's how the workshop will go:

 - Organize into groups of three
 - Spend a full 10 minutes focusing on each participant's bot
 - For each 10-minute round, the three of you will play different roles
 	- the **bot creator** should read the bot's bio and a few sample tweets -- and nothing else. DO NOT give a long introduction to your idea, just start reading
 	- the **critic** will look for problems and suggest points of improvement
 	- the **advocate** will argue on behalf of the bot, explaining its strengths and aesthetics to the critic
 - If time is left after the critic and advocate have had their turn, the creator may respond to and debrief their suggestions

On Friday, you'll each give a brief performance of your bot to the class, and we'll discuss how they all turned out.

As you complete your bot, I want to draw your attention to the "at least 100,000 variations" requirement. That may seem like a lot, but it's pretty easy to figure out. Consider some Tracery code like this:

```json
{
	"origin":["Roses are #color1#, violets are #color2#.","Sugar is #flavors# and so are #objects#"],
	"color1":["blue","red","green","yellow"],
	"color2": ["pink","white","black","turquoise","magenta","orange"],
	"objects": ["papers","toys","walls","discs","ice creams","carpets","aluminum foil"],
	"flavors":["sweet","smokey","chicken-like","sour","cold","fishy"]
}
```

The `origin` statement contains two options. For option one, `Roses...`, there are two variables, `color1` and `color2`. There are four options for `color1` and six options for `color2`. 

`6 * 4` is 24, so that's 24 possible combinations of `color1`s with `color2`s in `origins` first option.

In the second option, six `flavors` times seven `objects` equals 42 variations. 

24 from the first `origin` option plus 42 from the second `origin` option means that this little Tracery grammar with five variables can create **66 variations**. That's pretty good! And it expands geometrically if you add to any one of those lists.

> (6 * 4) + (6 * 7) = 66
> (6 * 100) + (6 * 7) = 642

It goes even faster if you add more options at the `origin` level, or if you make each of the substitutions include substitutions of their own:

```json
{
	"origin":["Roses are #color1#, violets are #color2#.","Sugar is #flavors# and so are #objects#"],
	"color1":["blue","red","green","yellow"],
	"color2": ["pink","white","black","turquoise","magenta","orange"],
	"flavors":["sweeter than #candy#","smokey","tasting like #animals#","sour","cold","fishy"],
	"objects": ["papers","toys","walls","discs","ice creams","carpets","aluminum foil"],
	"animals":["cow","pig","trout","spider"],
	"candy":["honey","Snickers","Butterfingers"]
}
```

That would be calcuated like

> (6 * 4) + ((3 * 1 * 4 * 1 * 1 * 1) * 7) = 108

Now, if you're wondering how you can get lists of 100 or more color names, the answer is the [Corpora repository](http://github.com/dariusk/corpora), which includes dozens of lists, some of which are very, very long. Many of these are already JSON-formatted in a way that you can just copy and paste into your CBDQ editor to add to your bot!

Basically, 100K variations is a lot easier to get to than you think, and if you need help or advice, please ask in Slack!


