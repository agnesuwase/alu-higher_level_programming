# Python - Almost a circle

This project builds three classes, Base, Rectangle and Square,
to review Python object-oriented programming concepts.

## Concepts
- Unit testing and how to implement it in a large project
- Serializing and deserializing a class
- Writing and reading a JSON file
- args and kwargs
- Handling named arguments in a function

## Files
- models/base.py: Base class (id management, JSON, save/load to file)
- models/rectangle.py: Rectangle class, inherits from Base
- models/square.py: Square class, inherits from Rectangle
- tests/test_models/: unit tests for all classes

## Run the tests
    python3 -m unittest discover tests

Agnes Uwase
