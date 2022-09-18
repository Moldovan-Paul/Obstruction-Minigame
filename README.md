# About Obstruction

<p align="center">
<img width="400" alt="image" src="https://user-images.githubusercontent.com/98110966/190891012-0314b726-2028-498f-a1cb-663aa23b0f8e.png">
</p>

# Overview

This is a console-based application that allows the user to play a game of **Obstruction** against the computer. A **minimax algorithm** is implemented in order to give the computer a great chance at winning, thus challenging the user. It is written in **Python**. **Unit tests** are implemented for non-UI functionalities.

FOR **VIDEO DEMONSTRATION** PLEASE REFER TO THE FOLLOWING ANCHOR:

[Gameplay Demonstration](#gameplay-demonstration)

# Game Rules

Rules for the game are straight forward: 
* Players take turns in marking accessible territories on a 6x6 grid 
  - Territories available to be marked are represented by a hyphen `-`
  - A player marked territory is represented by an `X` and a computer marked territory is represented by an `O`
  - Marking a territory will also mark all neighbouring territories as inaccessible with a plus sign `+`
* The first player unable to move loses.

# How to Play

The user always has the first move. Two consecutive console messages will ask the user to input the **coordinates** of the territory they wish to mark. They will first choose a value for the row coordinate (in the range 0-5) and then a value for the column coordinate (in the 0-5 range). Subsequently, the computer will make its move. It can be observed that the territory coordinates are indexed from 0.

### Input Validation

If the territory is marked or the chosen position is not valid or the input is not a number, appropriate messages will be shown to the user.

<img width="270" alt="image" src="https://user-images.githubusercontent.com/98110966/190892636-0d73ec7c-2dea-46ec-ae6d-4fd3f6ac6111.png">
<img width="270" alt="image" src="https://user-images.githubusercontent.com/98110966/190892693-44ac0058-689e-4674-89dc-0589eeab0463.png">
<img width="270" alt="image" src="https://user-images.githubusercontent.com/98110966/190892736-88c447cd-06e4-4ac6-8852-e627d9aa1498.png">


# Gameplay Demonstration

### Computer wins

https://user-images.githubusercontent.com/98110966/190895059-55560f96-2d26-467c-9dbb-e065cb12786d.mp4

### Player wins

https://user-images.githubusercontent.com/98110966/190894659-c89ed7b4-7b41-4ad8-8a1f-aa61d7c9348b.mp4
