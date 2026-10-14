import sys

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

### YOUR CODE HERE ###

COVID_data = parse_nyt_data('../../data/covid/us-counties.csv') #Using the premade function to turn the data to a tuple

#print(COVID_data[0][0]) # Testing the data in the tuple


"""
Creating target criteria for finding the data
"""

Rockingham_county = 'Rockingham'   # Created target county

Harrisonburg_county = 'Harrisonburg city' # Created target county for Harrisonburg

state = 'Virginia'     # Created target state


"""
Placing the data into smaller more managable lists by scanning the parsed data for the target criteria
"""

Rockingham_cases = []   # Creating a smaller and easier to manage list for only data containing Rockingham County

Harrisonburg_cases = [] # Creating a smaller and easier to manage list for only data containing Harrisonburg

for i in COVID_data:

    if i[1] == Rockingham_county and i[2] == state: # Compares the county name in the csv file to the target county
        
       # print(i[0] , 'Rockingham Cases = ' , i[4]) # Uncomment to test if all the data to find desired values

        Rockingham_cases.append(i)  # Stores data on a county with this name to its respective smaller list
        

    if i[1] == Harrisonburg_county and i[2] == state:   # Repeats what the above loop does, but for Harrisonburg
       
       # print(i[0] , 'Harrisonburg Cases = ' , i[4]) # Uncoment to test if all the data to find desired values

        Harrisonburg_cases.append(i)    



"""
Question 1: When was the first positive COVID case in Harrisonburg? When was the first positive case in Rockingham County?
"""

print('The date of the first recorded case in Harrisonburg is: ', Harrisonburg_cases[0][0]) # Returns the date of the first recorded case on the Harrisonburg list

print('The data of the first recorded case in Rockingham County is: ', Rockingham_cases[0][0])  # Returns the date of the first recorded case on the Rockingham list

print() # creates a space to make the terminal easier to read

"""
Question 2: On what date was the greatest number of new cases reported in Harrisonburg? What date in Rockingham County?
"""


def greatest_increase(town_list, location_name):
    """
    Finding 7 consecutive days with the most new cases in one town's rows.
    Returns (start_date, end_date, new_cases_in_window).
    """
    best_total = -1      # highest 7-day total seen so far
    best_start = None    # first date of the best window
    best_end = None      # last date of the best window


    for i in range(1, len(town_list)):
        
        total = town_list[i][4] - town_list[i - 1][4]   # Cases gained accross two days

        
        if total > best_total:  # keep if it beats the best so far
            best_total = total  # total number of new cases
            best_start = town_list[i - 1][0]   # date of the first day
            best_end = town_list[i][0]         # date of the last day

            
    # Making the information from this function visible
    print("The highest increase in cases for", location_name, "is", best_total) # Making the information from this function visible
    print("The highest increase for", location_name, "occured on", best_end)

    print() # Creates a space in ther terminal to make it easier to read

    return best_start, best_end, best_total

greatest_increase(Harrisonburg_cases, 'Harrisonburg')
greatest_increase(Rockingham_cases, 'Rockingham County')

"""
Question 3: What was the worst seven-day period in Harrisonburg city for new COVID cases? 
What period in Rockingham County? These are the seven-day periods when the number of new cases was maximal.
"""

def worst_seven_days(town_list, location_name):
    """
    Finding 7 consecutive days with the most new cases in one town's rows.
    Returns (start_date, end_date, new_cases_in_window).
    """
    sevenbest_total = -1      # highest 7-day total seen so far
    sevenbest_start = None    # first date of the best window
    sevenbest_end = None      # last date of the best window

    # start at 7 so that i - 7 always exists
    for i in range(7, len(town_list)):
        
        seventotal = town_list[i][4] - town_list[i - 7][4]   # new cases over seven days

        
        if seventotal > sevenbest_total:  # keep if it beats the best so far
            sevenbest_total = seventotal  # total number of new cases
            sevenbest_start = town_list[i - 6][0]   # date of the first day
            sevenbest_end = town_list[i][0]         # date of the last day
            
    # Making the information from this function visible
    print("The new cases over seven days for", location_name, "is", sevenbest_total) # Making the information from this function visible
    print("The worst seven days for", location_name, "occured between", sevenbest_start, "and", sevenbest_end)

    print() # Creates a space in ther terminal to make it easier to read

    return sevenbest_start, sevenbest_end, sevenbest_total


worst_seven_days(Harrisonburg_cases, 'Harrisonburg')    # Running the fucntion for each county
worst_seven_days(Rockingham_cases, 'Rockingham_County')

    
    
"""Below this text is old code that is functional but commented out in case I need inspiration for other parts of the project"""

# def max_cases(town_list):
#     """
#     Creating a function to be used on both location lists that
#     compares the current row cases to the current highest number
#     """
    
#     highest = town_list[0]  # Varriable that stores the date that has the highest number of cases

#     for p in range(1, len(town_list)):  # Combs through the data range

#         if town_list[p][4] > highest[4]:    # Comparing the current cases to the highest cases
            
#             highest = town_list[p]  # Replacing the lower case count with the new highest value
    

#     return highest

# hbcase = max_cases(Harrisonburg_cases)  # Tunring the returned varriables into a list where indexes can be printed
# rhcase = max_cases(Rockingham_cases)

# print("Harrisonburg's max cases was", hbcase[4],"and occured on", hbcase[0])

# print("Rockingham's max cases was", rhcase[4],"and occured on", rhcase[0])
