# Hand Gesture Number Counter

This Python project utilizes OpenCV and Mediapipe libraries to determine hand gestures and count the number of fingers shown on the screen. The user can perform hand gestures to represent digits, and the program will repeatedly count and combine these digits to form two numbers. Finally, it calculates the sum of these two numbers.

## Installation

To run the project, you need to have Python installed on your system. Additionally, you need to install the following libraries:

- OpenCV: `pip install opencv-python`
- Mediapipe: `pip install mediapipe`

## How to Use

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the `main.py` file.

Upon running the program, you will be prompted to enter the number of digits in the first and second numbers. Follow the instructions on the screen to perform hand gestures and show the corresponding number of fingers. The program will then combine the digits to form two numbers and display their sum on the screen.

## Project Files

The project contains the following files:

### `pose.py`

This file defines the `inpt` function, which is responsible for detecting hand gestures and counting the number of fingers shown. The function takes the number of digits as input and returns the combined number formed by repeating the gesture multiple times.

### `calcul.py`

This file defines the `outpt` function, which displays the two input numbers and their sum on the screen using OpenCV. The numbers are shown in different colors for easy identification.

### `main.py`

This is the main file of the project, which imports the functions from `pose.py` and `calcul.py`. It prompts the user to enter the number of digits for the two numbers and then calculates and displays the sum of these numbers on the screen.

## Sample Output

Here is a sample output of the project:

```
Enter the number of digits in the first number: 3
Enter the number of digits in the second number: 2
[Perform hand gestures as instructed]
The first number is: 742
The second number is: 16
The sum of the two numbers is: 758
```

## Contribution

Contributions to the project are welcome. If you find any issues or want to add new features, feel free to create a pull request or open an issue on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE), allowing you to modify and distribute the code as per the license terms.
