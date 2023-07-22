#!/usr/bin/env python
# Part 1

def mode():
    counter = ModeCounter()
    # determine the winner
    for number in numbers:
        counter.add_number(number)


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

 #def get(self):

