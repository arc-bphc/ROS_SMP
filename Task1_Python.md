# Task 1: Tic Tac Toe

Make a game of tic tac toe. Ezpz. 

## Instructions

1. Use Classes and Objects as you think necessary
2. Do not copy code from a fucking website that does the entire game for you. If I just needed a fucking tic tac toe game, I can look it up online.
3. That being said, feel free to look up stuff online about how to do something very specific, or if youa re getting an error. 
   1. Python documentation and stackoverflow will be your best friends
4. The exercise will not be graded. We can review your submissions and code if you wish
5. Comment your code. Explain logic, and not that the next line is a for loop. I can read that myself. 
7. Follow pep8 guidelines. I will not read any unformatted code.
   1. How? Install autopep8 or something. [Detailed Instructions for VS Code](#detailed-instructions-for-vs-code)
8. Use multiple files, to keep your project clean and maintainable
9. Have a main.py file, running which starts the game. For example
    ```sh
        python main.py # This exact command will be used to evaluate your submissions
    ```
## Project Structure
```sh
tictactoe
    └── main.py
    └── [module1].py
    .
    .
    └── [modulen].py # Replace [modulei].py with whatever you name your files
```

## Sprites

Every new game state should output the board in the following format:

### X:


```
xx      xx
  xx  xx
    xx
  xx  xx
xx      xx   
```


### O:

```
   oooo 
 oo    oo
oo      oo
 oo    oo
   oooo 
```

### Sample Board

```
 xx      xx |            |            | 
   xx  xx   |            |            |
     xx     |            |            |
   xx  xx   |            |            |
 xx      xx |            |            |
------------|------------|--------------
|           |    oooo    |            |
|           |  oo    oo  |            |
|           | oo      oo |            |
|           |  oo    oo  |            |
|           |    oooo    |            |
------------|------------|--------------
|           | xx      xx |            |
|           |   xx  xx   |            |
|           |     xx     |            |
|           |   xx  xx   |            |
|           | xx      xx |            |
```

## Detailed Instructions for VS Code
1. Press `ctrl+shift+P`
2. Search for Format Document. You should get a popup which says, something along the lines of 
   > autopep8 not installed. Install now? 
3. Click on install. 
4. After it is done installing, you can use `Ctrl+Shift+P > Format Document` to format your documents. 
