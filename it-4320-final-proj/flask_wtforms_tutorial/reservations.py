




# Imports



#Functions


'''
Function to generate cost matrix for flights
Input: none
Output: Returns a 12 x 4 matrix of prices
'''
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

# function to generate an empty seating chart
def get_empty_seating_chart():
    chart = [['O', 'O', 'O', 'O'] for row in range(12)]
    return chart

# creates the e-ticket number based on the first name of the user
def make_eticket(name):
    course = "INFOTC4320"
    name_character_list = split_name(name)
    course_character_list = split_name(course)

    ticket = ""

    if len(name_character_list) < len(course_character_list):
        for i in range(len(name_character_list)):
            ticket += name_character_list[i] + course_character_list[i]
        else: 
            for j in range(len(course_character_list) - i - 1):
                ticket += course_character_list[j + i + 1]


    elif len(name_character_list) > len(course_character_list):
        for i in range(len(course_character_list)):
            ticket += name_character_list[i] + course_character_list[i]
        else: 
            for j in range(len(name_character_list) - i - 1):
                ticket += name_character_list[j + i + 1]

                
    elif len(name_character_list) == len(course_character_list):
        for i in range(len(name_character_list)):
            ticket += name_character_list[i] + course_character_list[i]

    print(ticket)
    return ticket
        

# returns a list of characters in a name
def split_name(name):
    return [char for char in name]

# returns a dictionary containing admin usernames (key) and passwords (value) from the passcodes.txt document
def get_login_dict():
    f = open("passcodes.txt", "r")
    f_contents_list = f.readlines()
    f.close()

    logins = dict()

    for t in f_contents_list:
        split_t  = t.split(', ')
        logins[split_t[0]] = split_t[1].replace("\n", "")

    return logins

# returns a nested list containing reservation data. Each element in the list is a list containing the reservation's name, row, seat, and e-ticket number
def get_reservations_list():
    f = open("reservations.txt", "r")
    f_contents_list = f.readlines()
    f.close()

    reservations = list()

    for r in f_contents_list:
        single_reservation_data = []

        split_t  = r.split(', ')

        single_reservation_data.append(split_t[0])
        single_reservation_data.append(split_t[1])
        single_reservation_data.append(split_t[2])
        single_reservation_data.append(split_t[3].replace('\n', ''))

        reservations.append(single_reservation_data)

    return reservations


# returns a seating chart displaying open and reserved seats
def generate_seating_chart():
    chart = get_empty_seating_chart()

    reservations = get_reservations_list()

    for r in reservations:
        chart[int(r[1])][int(r[2])] = 'X'

    return chart


# returns the amount of dollars made from seat reservations
def get_sales():
    sales = 0

    cost_matrix = get_cost_matrix()
    chart = generate_seating_chart()

    for i in range(len(chart)):
        for j in range(len(chart[i])):
            if chart[i][j] == 'X':
                sales += cost_matrix[i][j]

    return sales


# takes first_name, row, and seat and makes a reservation
def make_reservation(first_name, row, seat, e_ticket):
    reservation_string = first_name + ', ' + row + ', ' + seat + ', ' + e_ticket + "\n"

    append_to_reservations_document(reservation_string)

# appends a reservation to the end of the reservation document
def append_to_reservations_document(string):
    f = open('reservations.txt', 'a')
    f.write(string)
    f.close()




