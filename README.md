# About Obstruction

<p align="center">
<img width="400" alt="image" src="https://user-images.githubusercontent.com/98110966/190895748-a14a8b02-0c9c-42e0-b121-fb9d9158c6a2.png">
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

<p align="center">
<img width="270" alt="image" src="https://user-images.githubusercontent.com/98110966/190895811-46015bec-12e0-495d-9c83-6facdfc886bb.png">
</p>

<p align="center">
<img width="270" alt="image" src="https://user-images.githubusercontent.com/98110966/190895786-7101e73a-c484-4f62-a905-fe73b5046440.png">
</p>

<p align="center">
<img width="270" alt="image" src="https://user-images.githubusercontent.com/98110966/190895858-c7817495-7a6b-4e0a-9bb4-08478627ee52.png">
</p>

# Gameplay Demonstration

### Computer wins

https://user-images.githubusercontent.com/98110966/190895059-55560f96-2d26-467c-9dbb-e065cb12786d.mp4

### Player wins

https://user-images.githubusercontent.com/98110966/190894659-c89ed7b4-7b41-4ad8-8a1f-aa61d7c9348b.mp4

