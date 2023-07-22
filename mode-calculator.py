#!/usr/bin/env python
import argparse


class ModeCounter:

    """
    Class to keep track of the mode in a list of numbers.

    Attributes:
    frequency_dictionary: A dictionary where keys are numbers and values are their frequency
    winning_frequency: The highest frequency among all numbers.
    winner: The number with the highest frequency.
    """
    def __init__(self):
        """Initializes frequency dictionary and sets winning_frequency to 0"""
        self.frequency_dictonary = {}
        self.winning_frequency = 0

    def add_number(self, number):
        """
        Adds a number to the frequecny dictionary and update the mode.

        Args:
        number: The number to be added.
        """
        if number not in self.frequency_dictonary:
            self.frequency_dictonary[number] = 1
        else:
            self.frequency_dictonary[number] += 1
        self.update(number)

    def update(self, number):
        """
        Updates the current mode if the frequency of the number is higher than the current modes frequency.

        args:
        number: The number to be checked against the current mode.
        """
        current_freqency = self.frequency_dictonary[number]
        if current_freqency > self.winning_frequency:
            self.winning_frequency = current_freqency
            print(f"Number {number} is the newest number with the highest with frequency {self.winning_frequency}. It is the new mode.")
            self.winner = number

    def get(self):
        """
        Returns the winner

        Returns:
        The number with the highest frequency.
        """
        return self.winner


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', metavar='NUM', type=int, nargs='+', help='list of numbers to process')
    return parser.parse_args()


def mode():
    args = parse_args()
    numbers = args.numbers
    counter = ModeCounter()
    # determine the winner
    for number in numbers:
        counter.add_number(number)
    final_winner = counter.get()
    print(f"The mode is {final_winner}")


if __name__ == "__main__":
    mode()

