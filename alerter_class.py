#
# Alerts script
# Carson Forter
#

import csv
import os

class Alerter:
    """
    Alerts when input falls outside 2 sd of rolling 30-day mean.

    Can be used to trigger alerts for a given day or a batch of
    days by iterating through a list.
    """

    def __init__(self):
        self.mean = 0.0
        self.sd = 0.0
        self.inputs = []
        self.alert = False
        self.alert_type = None

    def update_stats(self, day_inputs):
        """
        Updates SD and mean, then appends latest inputs to self.inputs.

        Takes one parameter representing the total inputs for a
        city for a particular day. Always call before set_alert().
        It both updates the current stats, mean and SD, to include
        everything up until the current day, and appends the current
        day's total inputs after these calculations so it's not
        self inclusive.
        """
        if len(self.inputs) > 1:
            self.mean = (sum(self.inputs)) / float(len(self.inputs)) # len returns an int
            var = 0.0
            for i in (self.inputs):
                var += ((i - self.mean) ** 2.0)
            var = var / float(len(self.inputs)) # we have the whole population
            self.sd = var ** (1/2.0)
        self.inputs.append(day_inputs) # after calcs so it's not self-inclusive
        if len(self.inputs) > 30:
            self.inputs.pop(0)

    def set_alert(self, day_inputs):
        """
        Sets alerts to T or F for a given day and if T, sets type to HI or LOW.

        Takes one parameter representing the total inputs
        for a city for a particular day. Run after running
        update_stats() using the same argument.
        """
        self.alert = False
        self.alert_type = None
        if len(self.inputs) == 30: # doesn't set alert until rolling stats include 30 days
            if day_inputs > self.mean + (self.sd * 2.0):
                self.alert = True
                self.alert_type = "HI"
            if day_inputs < self.mean - (self.sd * 2.0):
                self.alert = True
                self.alert_type = "LOW"
