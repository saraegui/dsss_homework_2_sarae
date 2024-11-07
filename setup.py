

from setuptools import setup, find_packages

setup(
    name="math_quiz_game",  # Name of your project
    version="0.1",
    packages=find_packages(),  # Automatically find packages
    install_requires=[],  # Any external dependencies
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz',  # Map the CLI command to the function
        ],
    },
)
