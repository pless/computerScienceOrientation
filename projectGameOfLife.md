Exercise 3: Emergent Behaviors.

There are a small number of famous computational games that have fascinated amateurs and researchers alike for the last 50 years.  Today we are going to consider a few of these that have, so called, “Emergent” behaviors.  This is the case where a game is defined with a seemingly simple set of rules, but the behaviors that are observed are surprisingly complex, interesting, and often hard to predict.  Two of the most famous of these are:

Conway’s Game of Life, and
Craig Reynolds “Boids”

Both of these are interesting, because they are relatively easy to program!  In this lab you'll explore a little of each of these, and then write a blog post exploring one of them in more detail.  Let’s stary by talking about each of these for a minute.  

Exploration 1 (you must do this!)

The game of life is a “discrete” game, where the world consists of a grid.  Each grid cells is “on” or “off”.  Time run in steps, and at each step, each cell can change, with the following rules:

If a cell is "on":
It stays "on" if it has 2 or 3 neighbors that are also "on."
It turns "off" if it has fewer than 2 neighbors (underpopulation) or more than 3 neighbors (overcrowding).
If a cell is "off":
It turns "on" if it has exactly 3 neighbors that are "on" (reproduction).

The game plays out in steps, with each step applying these rules to all cells simultaneously, creating patterns that move, grow, or disappear based on these simple conditions.  This is it!

Some quick examples:

Suppose you have a board that has all cells off.  What will happen in the next round?  They will all stay off because Rule 2 is never triggered.
Suppose you have a board that has all cells on.  What will happen in the next round?  All cells will turn off because all have more than 2 or 3 neighbors.
Suppose you have a single cell that is on?
Suppose you have three cells in a row that are on?  What will happen to each of those cell and what will happen to their neighbors?

You can now play with this here:   https://kylepaulsen.com/stuff/game_of_life.html

The “randomize board” button below the big rectangle, and the “start simulation” are very useful.  Spend 5 minutes and see what patterns you find.  What patterns are stable?  What patterns are dynamically stable?

Exploration 2 (you must do this!)

The gave of Boids is a continuous game.  Objects move smoothly through time, and don’t live on a grid, but have real-valued coordinates.  Boids, (bird-oid objects) obeys three simple rules as they fly around:

1. Coherence: Each boid flies towards the the other boids.  How quickly they steer towards each other is defined as “coherence”.

2. Separation: Each boid also tries to avoid running exactly the other boids.  “Separation” is a measure of how close it gets to another boid before it try’s to steer away.

3. Alignment: Finally, each boid tries to match the vector (speed and direction) of the other boids around it. “Alignment” is a meaure of how exactly it tries to match the neighbors.

Use one of these two sites and explore what behaviors you see as you change the sliders:

https://eater.net/boids
https://boids.cubedhuang.com/

What happens with extreme values of the sliders?




Blog Post: You must do one of the below:

Blog Post option 1:

Consider the game of life and use the following simulator:

https://kylepaulsen.com/stuff/game_of_life.html

Write a blog that explore what happens as you change the rules (the number of neighbors it takes to be alive or dead).

What rule sets are boring and why?
What rule sets also give interesting behaviors?  Are there different types of “interesting”?
Why is the default rule set the one that is most interesting?
What are some different kinds of rules that you could possible add to this game to change things?  

Include screen shots to support your conclusions!


Blog post Option 2:

Consider the boids domain

https://eater.net/boids
https://boids.cubedhuang.com/


Write a blog that explore what happens as you change the sliders.

What slider settings give very boring behaviors?
What rule sets also give interesting behaviors?  Are there different types of “interesting”?
Can you make slider settings that give multiple flocks at the same time?
What other rules could you add to this simulation that might be interesting!

Include screen shots to support your conclusions!

Submission Link: https://docs.google.com/forms/d/e/1FAIpQLSd8q5D9Uea8qpjWMAoZGq5x8MTMN0b6H9oJ4ctEfEJNZQ4Pdw/viewform

