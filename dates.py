
"""
    File: dates.py
    Author: Zayyan Essani
    Course: CSC 120, Spring 2024
    Purpose: This program manages a database of dates and events to
            look up dates in the past. It prompts the user for a date
            and returns all the events that occured on that date.
"""

class Date:
    """
    This class represents dates in a list with their corresponding events

       The class defines the methods for returning the date and event
       while also adding an event to the list of events and a function
       to returning it.
    """
    def __init__(self, date, event):

        """
        This function initializes a date object
    
        Parameters: A string of the date and string of the events.
    
        Returns: None 

        """
        self._date = date   
        self._events = [event]

    def get_date(self):
        return self._date
    
    def get_events(self):
        return self._events
    
    def add_event(self, event):
        '''
        Adds an event to the date object

        Parameters: A string of events

        Returns: None
        '''
        self._events.append(event)
        self._events.sort()

    def __str__(self):
        events_str = ", ".join(self._events)
        return "{}: {}".format(self._date, events_str)
    
class DateSet:
    """
    This class represents a set of data objects.

       The class defines the methods for adding dates to the object and
       printing them in a new line
    """
    def __init__(self):
        """
        This function initializes a DateSet object by an empty
        dictionary
    
        Parameters: None
    
        Returns: None 

        """
        self._dates = {}

    def add_date(self, date, event):
        '''
        Adds a date to the DateSet object

        Parameters: A string of events and a string of dates

        Returns: None
        '''
        if date in self._dates:
            self._dates[date].add_event(event)
        else:
            self._dates[date] = Date(date, event)

    def print_date(self, date):
        '''
        This function prints the events associated with a given date

        Parameters: A string of date

        Returns: None (prints the date and event(s) in the
                correct format)
        '''
        if date in self._dates:
            date_obj = self._dates[date]
            events = date_obj.get_events()
            # print each event in a new line
            for event in events:
                print("{}: {}".format(date_obj.get_date(), event))


    
    def __str__(self):
        date_strings = []
        for date_obj in self._dates.values():
            date_strings.append(str(date_obj))
        return '\n'.join(date_strings)
    





def canonicalize_date(date_str):

    """
    Takes a list of date strings as input which can be in
    three different forms and canonicalizes into a single form
  
    Parameters: A list of dates in string form
    Returns: Returns the date in canonicalized form

    """

    # check to see the format of the inputted date
    if "-" in date_str:
        date = date_str.split("-")
        year, month, day = date
        if month[0] == "0":
            month = month.lstrip("0")
        if day[0] == "0":
            day = day.lstrip("0")
    elif "/" in date_str:
        date = date_str.split("/")
        month, day, year = date
        if month[0] == "0":
            month = month.lstrip("0")
        if day[0] == "0":
            day = day.lstrip("0")
    elif " " in date_str:
        parts = date_str.split()
        months = {
            "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
            "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
            "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
        }
        # extract month, day and year
        # convert month name to numeric value
        month = months[parts[0]]
        day = int(parts[1])
        year = int(parts[2])
        if parts[1][0] == "0":
            day = int(parts[1].lstrip("0"))
    return "{:d}-{:d}-{:d}".format(int(year), int(month), int(day))


def main():
    input_file = input()
    # create object
    dataset = DateSet()
    file = open(input_file, 'r')
    for line in file:
        line = line.strip()
        if line[0] == "I":
            # find the first colon in he line to seperate
            # the date and event
            switch = line.find(":")
            # extract date and event
            date = line[1:switch]
            event = line[switch+1 :]
            date = canonicalize_date(date)
            # add date and event to the object
            dataset.add_date(canonicalize_date(date.strip()), event.strip())

        elif line[0] == "R":
            # extract date from each line
            date = line[1:]
            date = canonicalize_date(date)
            dataset.print_date(date)

        else:
            print("Error - Illegal operation.")

        
    file.close()


main()