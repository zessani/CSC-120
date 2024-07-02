"""
    File: bball.py
    Author: Zayyan Essani
    Course: CSC 120, Spring 2024
    Purpose: This program manages a database of basketball teams
            and computes from this the win ratios of the teams 
            as well as the conference(s) with the highest average
            win ratio. The program structure uses three classes
            to represent information about a team, the teams that
            belong to a conference and a collection of conferences.

"""

class Team:
    
    """
    This class represents sports teams with their names,
    conference and win ratio

       The class defines the methods for defining the Team object,
       and the methods of returning the name, conference and win ratio.
       It also has a function to return it
    """

    def __init__(self, line):
        
        """
        This function initializes a Team object by calculating
        the location of the name and team in the file and calculating
        the win ratio.
    
        Parameters: A string of a line read from the input file.
    
        Returns: None 

        """
        # extracting team name and conference from input file
        if line.find(")") != line.rfind(")"):

            end_name = line.find(")") + 1
        else:
            end_name = line.find("(")
        # conference name is between the first parenthesis from the right
        l_conf = line.rfind("(")
        # locate the end of conference name
        r_conf = line.rfind(")")
        name = line[0 : end_name]
        conf = line[l_conf + 1 : r_conf]
        # extract win and loss stats
        stats = line[r_conf + 1:].split()
        win = int(stats[0])
        loss = int(stats[1])
        ratio = win / (win + loss)

        self._name = name
        self._conf = conf
        self._ratio = ratio

    def name(self):
        return self._name

    def conf(self):
        return self._conf

    def win_ratio(self):
        return self._ratio
    def __str__(self):
        return "{} : {}".format(self._conf, self._ratio)


class Conference:
    """
    This class represents a conference with its name and associated
    teams.

       The class defines the methods for checking if the conference
       contains a certain team, returning the name of the conference,
       adding a team to the conference and calculating the average win
       ratio for the conference.
    """
    def __init__(self, conf):
        """
        This function initializes a Conference object by 
        an empty list for teams and a string for the name 
        of conference.
    
        Parameters: A string of the name of the conference
    
        Returns: None 

        """
        self._name = conf
        self._teams = []

    def __contains__(self, team):
        # check if team is in conference
        return team.conf() == self._name

    def name(self):
        return self._name

    def add(self, team):
        self._teams.append(team)

    def win_ratio_avg(self):
        """
        This function calculates the average win ratio
        for a conference
    
        Parameters: self: the object itself
    
        Returns: Average win ratio

        """
        total_wins = 0
        for team in self._teams:
            total_wins += team.win_ratio()
        return total_wins / len(self._teams)

    def __str__(self):
        return "{} : {}".format(self._name, self.win_ratio_avg())


class ConferenceSet:
    """
    This class represents a collection of conferences

       The class defines the methods for adding teams to conferences
       and creates a Conference object for it.
    """
    def __init__(self):
        """
        This function initializes a ConferenceSet object by an empty 
        dictionary
    
        Parameters: self: the object itself
    
        Returns: None 

        """
        self._conferences = {}

    def add(self, team):
        '''
        Adds a team to the Conference object

        Parameters: A Team object

        Returns: None
        '''
        conf_name = team.conf()
        if conf_name in self._conferences:
            self._conferences[conf_name].add(team)
        else:
            new_conf = Conference(conf_name)
            new_conf.add(team)
            self._conferences[conf_name] = new_conf

    def best(self):
        '''
        Returns the conference(s) with the highest average
        ratio

        Parameters: self: the object itself

        Returns: A dictionary of the conference(s) with
                the highest average ratio
        '''
        avg_dict = {}
        highest_conf = {}
        # calculate highest win ratio for each conference
        for conf_name, conf in self._conferences.items():
            avg_dict[conf_name] = conf.win_ratio_avg()
        highest_avg = max(avg_dict.values())
        for key, value in avg_dict.items():
            if value == highest_avg:
                highest_conf[key] = value
        # sort the dictionary by conference name
        highest_conf = dict(sorted(highest_conf.items()))
        return highest_conf


def main():
    filename = input()
    file = open(filename, 'r')
    conference_set = ConferenceSet()
    for line in file:
        
        if line.startswith("#"):
            continue
        team = Team(line)
        conference_set.add(team)

    file.close()

    best_conferences = conference_set.best()
    for conf_name, avg_ratio in best_conferences.items():
        print("{} : {}".format(conf_name, avg_ratio))

main()

