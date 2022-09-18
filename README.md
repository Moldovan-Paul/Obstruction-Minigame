# About Obstruction

<img width="400" alt="image" src="https://user-images.githubusercontent.com/98110966/190891012-0314b726-2028-498f-a1cb-663aa23b0f8e.png">

# Overview

This is a console-based application that allows the user to play a game of **Obstruction** against the computer. A **minimax algorithm** is implemented in order to give the computer a great chance at winning, thus challenging the user. It is written in **Python**. **Unit tests** are implemented for non-UI functionalities.

FOR **VIDEO DEMONSTRATION** PLEASE REFER TO THE FOLLOWING ANCHOR:

[Gameplay Demonstration](#gameplay-demonstration)

# Game Rules

Rules for the game are straight forward: 
* Players take turns in marking accessible territories on a grid 
  - Territories available to be marked are represented by a hyphen `-`
  - A player marked territory is represented by an `X` and a computer marked territory is represented by an `O`
  - Marking a territory will also mark all neighbouring territories as inaccessible with a plus sign `+`
* The first player unable to move loses.

# How to Play

The user always has the first move. Two consecutive console messages will ask the user to input the **coordinates** of the territory they wish to mark. They will first choose a value for the x axis coordinate (in the range 0-5) and then a value for the y axis coordinate (in the 0-5 range). Subsequently, the computer will make its move. It can be observed that the territory coordinates are indexed from 0.

# Gameplay Demonstration

### Player wins

### Computer wins
