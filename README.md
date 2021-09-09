# NOUGHTS & CROSSES

![game logo](https://user-images.githubusercontent.com/82375381/132107968-b2bdb4ba-6f0c-4a7e-8e8b-5e0e3db7e062.jpeg)

## Author
Gabriel Alves

## Project Overview

![game-overview](https://user-images.githubusercontent.com/82375381/132195776-c33506c5-96db-418f-a962-0934ba8f5bbe.gif)

- This application was developed as part of my third Portfolio project with Code Institute. It is a Noughts & Crosses (or Tic Tac Toe) game developed with Python as it's only language and is a Player vs Computer style game. It contains two levels of difficulty, which are chosen by the user. The user can then either play against a computer which chooses its moves randomly, or a computer that maximizes its gains whilst minimizing its losses, making it unbeatable.

- You can view my deployed app [here](https://noughts-n-crosses.herokuapp.com/).

## Table of Contents

- [How To Play](#how-to-play)
- [Technologies](#technologies)
- [Features](#features)
  * [Implemented Features](#implemented-features)
  * [Future Features](#future-features)
- [Design Documents](#design-documents)
- [Data Model](#data-model)
- [Python Libraries](#python-libraries)
- [Testing](#testing)
  * [Validation Testing](#validation-testing)
  * [Manual Testing](#manual-testing)
  * [Defect Tracking](#defect-tracking)
- [Deployment](#deployment)
  * [Heroku](#heroku)
- [Credits](#credits)
  * [Code Institute](#code-institute)
  * [GitHub](#github)
  * [Stackoverflow](#stackoverflow)
  * [Tutorials](#tutorials)
  * [Acknowledgments](#acknowledgments)

## How To Play

- Go to the [deployed website](https://noughts-n-crosses.herokuapp.com/).
- Click on "Run Program".
- Input your username.
- Select difficulty (either "easy" or "hard").
- You will be playing against a computer.
- Select your first move based on a numbered list of empty spots ranging from 0 to 8.
- Await the computer's move and repeat the previous step until there are no empty spots left (a tie), or until either you or the computer score a straight line (vertically, horizontally or diagonally) to win.

## Technologies

- Python3
- JavaScript
- HTML
- Markdown
- GitHub
- GitPod
- PyCharm
- Heroku

## Features

### Implemented Features

- Game logo. Colored with Colorama library for aesthetic reasons.

<img width="433" alt="game-logo" src="https://user-images.githubusercontent.com/82375381/132222001-18398f09-2434-478f-b995-e40b8569da94.png">

<br>

- Game intro. It was designed to introduce the player to the game. I used Python's time library to slow the messages down to allow the user time to read the messages as they appear. Here I also collect the user's username and then print a hello message to them, to make the game seem friendly.

<img width="324" alt="game-intro" src="https://user-images.githubusercontent.com/82375381/132222617-e6d448b7-8be0-4abc-ac9e-52c8a55054ed.png">

<br>

- Difficulty choice. Here I give the user three options to proceed with the game. The choices are "easy", "hard" or "quit". With the "easy" choice, the user will be playing against a computer that randomly selects its moves, thus making it easily beaten. With the "hard" choice, the user will be playing against a genius computer which uses an algorithm to maximize its score whilst minimizing its losses, making it seemingly unbeatable. And ,finally,
the "quit" options offers the user a way to exit the game. Each option prints its own personalized message to the user.

<img width="883" alt="easy-difficulty" src="https://user-images.githubusercontent.com/82375381/132223330-0db190d4-5a53-486c-9673-c8104b961a91.png">
<img width="890" alt="hard-difficulty" src="https://user-images.githubusercontent.com/82375381/132223342-f1027e8a-1883-4275-9061-44b795427a42.png">
<img width="381" alt="quit-option" src="https://user-images.githubusercontent.com/82375381/132223348-6656f64f-823f-4486-8506-c287b49378f4.png">

<br>

- Making the first move. Once a difficulty has been chosen, the game then displays a game board to the user, it has numbers corresponding to each of the empty spaces where the user's tag (X or O) will go on. The user will then input a number (must be an available move ranging from 0 to 8 or the game will raise a ValueError and ask the user to re-input a valid number) and their tag will be added to the corresponding empty space. The game prints out updated versions of the available moves and game boards in between rounds and provides message feedback to the user, so the user knows what is happening in the game at all times.

<img width="138" alt="availability-game-board" src="https://user-images.githubusercontent.com/82375381/132225450-4cae58d1-9129-4dcb-95e4-11ab50f7ac41.png">
<img width="169" alt="available-moves" src="https://user-images.githubusercontent.com/82375381/132225554-2fc88833-6018-48f1-ae64-3da63123edca.png">
<img width="183" alt="game-board" src="https://user-images.githubusercontent.com/82375381/132225585-5bb72a1b-54b7-4178-a417-0e98d8b49517.png">
<img width="292" alt="make-move" src="https://user-images.githubusercontent.com/82375381/132225727-2d24c3cd-7c18-4a04-b3eb-60820b07baba.png">
<img width="285" alt="validation" src="https://user-images.githubusercontent.com/82375381/132225964-d0714040-a7f9-43f8-8f88-c7a168c1f3a0.png">
<img width="393" alt="game-play" src="https://user-images.githubusercontent.com/82375381/132225496-6fb95a6e-6e48-43f6-b853-4e058f10d721.png">

<br>

- Finding the winner. After each move, the game checks whether the previous move was a winning move (a straight line vertically, horizontally or diagonally) and if it does find a winning move, it awards it to the tag which the straight line was scored with. If there are no move available moves on the board and no one has won, the game sends a "tie" message.

<img width="85" alt="x-win" src="https://user-images.githubusercontent.com/82375381/132228808-834ade44-3bd2-49bc-9342-e16bc2838622.png">
<img width="81" alt="o-win" src="https://user-images.githubusercontent.com/82375381/132228813-0f88d34c-cdb8-4bc5-ac7b-58d33fe3e114.png">
<img width="122" alt="tie" src="https://user-images.githubusercontent.com/82375381/132228817-eceb083a-9ce9-4c6c-be8d-27a003f03e6d.png">

<br>

### Future Features

- To store the user's score and present it to them once they decide to quit the game.
- To give the user the option to choose which tag to start with.
- To collect the user's favorite color and color their tag with it.
- To further color the game throughout with Colorama.


## Design Documents

- Code flow chart.
<img width="986" alt="code-flow-chart" src="https://user-images.githubusercontent.com/82375381/132256579-d5fd8d2c-aeb1-42cb-b9c1-738cc1a2a8bb.png">

<br>

- Game flow chart.

<img width="879" alt="game-flow-chart" src="https://user-images.githubusercontent.com/82375381/132256596-bbe57916-b829-401a-b629-7a70a7e5c86d.png">
<br>

## Data Model

In this section write our your data model(s).

You might want to include subsections that include how the data in the model is . initialized and then the methods that you created to update it through the program.

![image](https://user-images.githubusercontent.com/23039742/130148204-b56406bf-0fff-48f3-9dee-2f3cdbe67cc5.png)


## Python Libraries

- Time: used the sleep() function in between messages to the user to allow time for reading.
- Math: used to code the minimax algorithm to make the genius computer player.
- Random: used to randomize the computer's moves in the "easy" mode and the first move the genius computer makes.
- Colorama: used to color the game throughout.

## Testing

### Validation Testing

- Testing was done with [PEP8 Validator](http://pep8online.com/).
<img width="625" alt="pep8-testing1" src="https://user-images.githubusercontent.com/82375381/132258505-46d1d087-6ecd-4419-90ce-1aef32264ee1.png">
<img width="379" alt="pep8-testing2" src="https://user-images.githubusercontent.com/82375381/132258509-a8c8538c-d818-4fc0-b2de-fe0689a00a0e.png">

### Manual Testing

- You will find my manual testing sheet [here](https://docs.google.com/spreadsheets/d/13o0Dz90fs4jI3M9rIsmxmlVFqfCWSbQBoOWfJUvsbwc/edit?usp=sharing).

### Defect Tracking

- You will find my defect tracking sheet [here](https://docs.google.com/spreadsheets/d/1xYKKoZuA54QKtIxZ2fA6-BUdHOFavs1R6JX9CK3YZQM/edit?usp=sharing).

## Deployment

### Heroku

- 1) Head to [Heroku](https://heroku.com) and create an account.
- 2) Click on "Create New App".
- 3) Name your app, select your region and click on "Create app".

<img width="628" alt="deployment1" src="https://user-images.githubusercontent.com/82375381/132574725-c6cbeb6e-be0c-41ad-9c46-bb13929ddd16.png">

- 4) On your app's dashboard bar, click on "Settings" and then click on "Reveal Config Vars".

<img width="641" alt="deployment2" src="https://user-images.githubusercontent.com/82375381/132574859-ec79920c-2f78-4e90-91e2-c107c5555d18.png">

- 5) Enter a key with the value of "PORT" and a value with the value of "8000", then click on "Add".

<img width="840" alt="deployment3" src="https://user-images.githubusercontent.com/82375381/132575015-01a907c0-4535-4f44-a825-930ca7e3e90e.png">

- 6) Scroll down and click on "Add buildpack", select "python" and "Save changes".
- 7) Repeat step 6 and select "nodejs" instead of "python" (they should be added in that order, python first and nodejs after).

<img width="830" alt="deployment4" src="https://user-images.githubusercontent.com/82375381/132575097-06258f70-6951-44da-9573-3c9523c839c6.png">

- 8) On your app's dashboard bar, click on "Deploy" and on the "Deployment method" section, select "GitHub".

<img width="612" alt="deployment5" src="https://user-images.githubusercontent.com/82375381/132575159-ecea4127-2f51-4cf4-9a01-67847342e9d0.png">
<img width="984" alt="deployment6" src="https://user-images.githubusercontent.com/82375381/132575228-308886b3-996d-4375-93b1-201bfc030dac.png">

- 9) Search for your GitHub repository and click "Connect".

<img width="1240" alt="deployment7" src="https://user-images.githubusercontent.com/82375381/132575314-f2669f55-3e25-4760-a64a-a3a82a9235cd.png">

- 10) Scroll down and click on "Enable Automatic Deploys".

<img width="1223" alt="deployment8" src="https://user-images.githubusercontent.com/82375381/132575399-29ded428-305b-4ef8-a7b1-4bd09ebdd1fc.png">

- 11) Wait until all files have been installed and it should give you a "Your app was successfully deployed." message.

<img width="835" alt="deployment9" src="https://user-images.githubusercontent.com/82375381/132575430-ceb70299-cb54-4f99-8a6c-301149a1332c.png">

## Credits

### Code Institute

- [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

### GitHub

- https://github.com/roomacarthur/escape-the-cave
    - Help with printing out the logo board to the terminal.

### Stackoverflow

- https://stackoverflow.com/questions/39922967/python-determine-tic-tac-toe-winner
    - Help finding the winner in the game.
- https://stackoverflow.com/questions/42091015/check-if-python-input-contains-a-specific-word/42091192
    - Help the game's intro loop that makes the user select one of three options.
- https://stackoverflow.com/questions/44269612/python-drawing-a-tic-tac-toe-board and https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874
    - Help with printing out the board to the terminal.

### Tutorials

- https://www.youtube.com/watch?v=BHh654_7Cmw
- https://www.youtube.com/watch?v=5s_lGC2sxwQ and https://www.youtube.com/watch?v=jAaJZLqryTI
- https://www.youtube.com/watch?v=n2o8ckO-lfk&t=954s
- https://www.youtube.com/watch?v=8ext9G7xspg&t=4342s

### Acknowledgments

This project could only come to exist because of the help and support from:

- My Code Institute mentor Malia Havlicek for being incredibly helpful and accessible.
- The community on Slack (fellow students and mentors).
- Code Institute for providing the accessible content from which I learned these new skills from.
