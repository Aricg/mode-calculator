#!/usr/bin/env python
import argparse

class ModeCounter:
    def __init__(self):
        self.frequency_dictonary = {}
        self.winning_frequency = 0

    def add_number(self,number):
        if number not in self.frequency_dictonary:
            self.frequency_dictonary[number] = 1
        else:
            self.frequency_dictonary[number] += 1
        self.update(number)

    def update(self, number):
        current_freqency = self.frequency_dictonary[number]
        if current_freqency > self.winning_frequency:
            self.winning_frequency = current_freqency
            print(f"Number {number} is the newest number with the highest with frequency {self.winning_frequency}. It is the new mode.")
            self.winner = number 

    def get(self):
        return self.winner

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', metavar='NUM', type=int, nargs='+', help='numbers to process')
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

