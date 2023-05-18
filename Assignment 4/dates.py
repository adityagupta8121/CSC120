'''
CSC 120 (A4)
File: dates.py
Author: Aditya Gupta
Purpose: a program to read given file, which
        contains dates and events related,
        and returns the dates and events
        listed in canonical format.
'''
class Date:
    def __init__(self, date, event):
        self._date = date
        self._event = [event]

    def get_date(self):
        return self._date

    def get_event(self):
        return self._event

    def add_event(self, event):
        self._event.append(str(event))

    def __str__(self):
        i = 1
        events = ""
        for event in self._event:
            if i == len(self._event):
                events += event
            else:
                events += event + ", "
                i += 1
        return str(self._date) + ": " + events

class DateSet:
    def __init__(self):
        self._dates = {}

    def add_date(self, date, event):
        self._dates[date._date] = date

    def get_dict(self):
        return self._dates

    def get_date(self, date):
        return self._dates[date]

    def __str__(self):
        dict_str = "{"
        i = 1
        for key in self._dates:
            if i != len(self._dates):
                dict_str += "'" + key + "': '" + str(self._dates[key]) + "',"
                i += 1
            else:
                dict_str += "'" + key + "': '" + str(self._dates[key]) + "'}"
        return dict_str

def correct_date_format(date):
    '''
    correct_date_format is a helper function for the more important,
    file_to_date function, as it is essential for converting the read date
    into the given YYYY-MM-DD format, by using some if-else statements
    and slicing the input, which is taken as a parameter - date.

    Parameters:
        date - String, it is a string, in which date is passed in the function
            when implemented in the file_to_read function.

    Returns:
        String, which contains the date in required YYYY-MM-DD format
    '''
    date_list = date.replace("-", " ").replace("/", " ").split(" ")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    length_datelist = len(date_list[0])

    if length_datelist == 4:
        year = date_list[0]
        month = date_list[1]
        day = date_list[2]
    elif length_datelist == 3:
        index = 1
        for month in months:
            if date_list[0] == month or index == " ":
                month = index
                day = date_list[1]
                year = date_list[2]
                break
            else:
                index += 1
    else:
        month = date_list[0]
        day = date_list[1]
        year = date_list[2]
    
    return "{:d}-{:d}-{:d}".format(int(year), int(month), int(day))

def file_to_date(file):
    '''
    file_to_date calls in the file name as a parameter, reads it,
    stores it and creates a set/object of DateSet class, and the Date
    class, to format the dates in canonical form. The function also
    uses a helper function named correct_date_format, which is essential
    to put the date in required format. The func. also makes sure the 
    user input is read as required, and provides output as 
    mentioned in the spec-sheet.

    Parameters:
        file - String, which is the name of the file to be read.

    Returns: None
    '''
    lines = file.read().split("\n")
    dates = DateSet()

    for line in lines:
        if line != "":
            line = " ".join(line.split())
            operator = line[0][0]

            if operator == "I":
                line = line.split(":", 1)
                date_info = line[0].strip("I ").strip("R ")
                date_info = correct_date_format(date_info)
                event_info = line[1].strip(" ")
                if date_info not in dates.get_dict():
                    curr_date = Date(date_info, event_info)
                    dates.add_date(curr_date, event_info)
                else:
                    curr_date = dates.get_dict()[date_info]
                    curr_date.add_event(event_info)
                    dates.add_date(curr_date, event_info)
                    
            elif operator == "R":
                line = line.split(":", 1)
                date_info = line[0].strip("I ").strip("R ")
                date_info = correct_date_format(date_info)

                if date_info in dates.get_dict():
                    date_object = dates.get_date(date_info)
                    events = date_object.get_event()
                    events.sort()
                    for event in events:
                        print ("{}: {}".format(date_info, event))

            else:
                print("Error - Illegal operation.")

def main():
    file = open(input())
    file_to_date(file)
    file.close()

main()