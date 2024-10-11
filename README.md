# Turtle Race Game

This project simulates a fun turtle race using Python's `turtle` module. Players can choose the number of turtles (between 2 and 10) that will race on the screen, and the game will randomly determine a winner. Each turtle moves a random distance in each step, making every race unpredictable!

## Features

- Choose the number of turtles (2 to 10) to participate in the race.
- Each turtle is assigned a unique color from a predefined list.
- Turtles race vertically from the bottom of the screen to the top.
- The race outcome is randomized, ensuring a different winner each time.
- The game window automatically closes after the race ends.

## How It Works

1. When the program starts, you will be asked to choose the number of turtles to race.
2. The turtles are randomly assigned positions at the bottom of the screen and are colored from a list of colors.
3. The race starts automatically, with each turtle moving a random distance per step.
4. The first turtle to reach the top of the screen is declared the winner.
5. The game ends when you click on the screen.

## Example

```
How Many Turtles do you want to race (2-10)? 5
The Winner is green Turtle!
```

## How to Run

1. Ensure you have Python installed on your machine.
2. Install the `turtle` module if it's not pre-installed:

    ```
    pip install PythonTurtle
    ```

3. Copy the turtle race code from this repository.
4. Save it as `turtle_race.py`.
5. Run the Python script using:

    ```
    python turtle_race.py
    ```

6. Enjoy the race!

## Customization

- You can change the colors of the turtles by editing the `color_list` in the code.
- Adjust the race area by modifying the `WIDTH` and `HEIGHT` values.
- Add more randomness to the turtle movements by tweaking the range in the `random.randrange()` function.

## Dependencies

- This project uses Python's built-in `turtle` module and the `random` module, so no external dependencies are required.

