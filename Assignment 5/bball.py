'''
CSC 120 (A5)
File: bball.py
Author: Aditya Gupta
Purpose: a program to read given file, compute the
        average win ratio for each conference &
        find the conferences that have the highest 
        win ratio.
'''
class Team:
    '''
    An object of the team represents information about a team: 
    namely, the team name, the conference it belongs to, and win-loss data.
    '''
    def __init__(self, line):
        '''
        line is the input, and which is how object is initialised
        other methods/alternations are performed for the below methods

        Parameters:
            self - object itself
            line - line - input given

        Returns: None
        '''
        if line.find(")") != line.rfind(")"):
            name_end = line.find(")") + 1
        else:
            name_end = line.find("(")

        left_con = line.rfind("(")
        right_con = line.rfind(")")
        name = line[0 : name_end]
        conf = line[left_con + 1 : right_con]

        stats = line[right_con + 1:].split()
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
        return  "{} : {}".format(self._name, str(self._ratio))

class Conference:
    '''
    An object of the Conference Class represents information about a 
    collection of teams, namely, the teams belonging to that conference.
    '''
    def __init__(self, conf):
        '''
        Initializes a conference object with name conf

        Parameters:
            self - object itself
            conf - string, name of conference

        Returns: None
        '''
        self._conf_list = []
        self._conf = conf

    def __contains__(self, team):
        return team in self._conf_list

    def name(self):
        return self._conf

    def add(self, team):
        self._conf_list.append(team)

    def win_ratio_avg(self):
        '''
        win_ratio_avg calculates the win_ratio

        Parameters:
            self - object itself

        Returns:
            avg - the calculated average
        '''
        sum = 0
        for team in self._conf_list:
            sum += team.win_ratio()
        self._avg = sum / len(self._conf_list)
        return self._avg

    def __str__(self):
        "{} : {}".format(self._conf, str(self._avg))

class ConferenceSet:
    '''
    An object of the ConferenceSet class represents
    a collection of conferences.
    '''
    def __init__(self):
        self._conference_set = {}

    '''
    add adds the conference to the set collecttion

    Parameters:
        self - object itself
        team - the team object

    Returns: None
    '''
    def add(self, team):
        team_conf = team.conf()
        if team_conf not in self._conference_set:
            conf_obj = Conference(team_conf)
            self._conference_set[team_conf] = conf_obj
        self._conference_set[team_conf].add(team)

    '''
    best returns highest conferences' dictionary after calculation
    and checking each conference set and their respective
    averages.

    Parameters:
        self - object itself

    Returns:
        high_ratio_conf - list of highest conf.
    '''
    def best(self):
        average_d = {}
        high_ratio_conf = {}
        for conf in self._conference_set:
            name = self._conference_set[conf].name()
            avg = self._conference_set[conf].win_ratio_avg()
            average_d[name] = avg
        highest_avg = max(average_d.values())
        for key, val in average_d.items():
            if val == highest_avg:
                high_ratio_conf[key] = val
        high_ratio_conf = dict(sorted(high_ratio_conf.items()))
        return high_ratio_conf

def main():
    file = input()
    file = open(file)
    conference_set = ConferenceSet()
    for line in file:
        if line[0] != "#":
            if line[0].isdigit():
                line = line[1:].strip()
            team = Team(line)
            conference_set.add(team)
    high_ratio_conf = conference_set.best()
    for key, val in high_ratio_conf.items():
        print("{} : {}".format(str(key), str(val)))

main()