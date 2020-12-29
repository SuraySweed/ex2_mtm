#### IMPORTS ####
import event_manager as EM

NUMBER_OF_FIELDS = 5
VALID_ID_LENGTH = 8
NOT_TO_PRINT = "-2"
MAX_AGE = 120
MIN_AGE = 16
CURRENT_YEAR = 2020
ZERO = 0
K_IS_NEGATIVE = -1
SEMESTER_IS_INVALID = -1

# id is string
def checkIdValidation(id):
	id = id.lstrip()
	id = id.rstrip()
	if(id.isdigit() == True): 
		int_id = int(id)
		str_id = str(int_id)
		if(len(str_id) == VALID_ID_LENGTH):
			return True, str_id
	return False, id

#name is string
def checkNameValidation(name):
	name = name.lstrip()
	name = name.rstrip()
	#spaces_counter = name.count(' ')

	names_list = name.split(" ")
    
	real_name_list =[]
	for str_name in names_list:
		if(str_name != ''):
			real_name_list.append(str_name)

	#words_counter = len(real_name_list)
	real_name = ' '.join(real_name_list)
    
	#if(words_counter - 1 != spaces_counter):
		#for str_name in real_name_list:
			#if(str_name.isalpha() == False):
				#return False, NOT_TO_PRINT
		
		#return False, real_name
	for str_name in real_name_list:
		if(str_name.isalpha() == False):
			return False, NOT_TO_PRINT
	
	return True, real_name

# age_str is string
def checkAgeValidation(age_str):
	age_str = age_str.lstrip()
	age_str = age_str.rstrip()
	
	if(age_str.isdigit() == False):
		return False, NOT_TO_PRINT
	
	age = int(age_str)
	if(age >= MIN_AGE and age <= MAX_AGE):
		return True, age_str
	return False, NOT_TO_PRINT
	
# age and year are strings
def checkBirthYearValidation(age, year):
	age = age.lstrip()
	age = age.rstrip()
	year = year.lstrip()
	year = year.rstrip()
	if(year.isdigit() == False or age.isdigit == False):
		return False, NOT_TO_PRINT
	year_int = int(year)
	age_int = int(age)
	if(CURRENT_YEAR - age_int == year_int):
		return True, year
	return False, NOT_TO_PRINT
	
# str_semester is string
def checkSemesterValidation(semester):
	semester = semester.lstrip()
	semester = semester.rstrip()
	if(semester.isdigit() == False):
		return False, NOT_TO_PRINT
	int_semester = int(semester)
	if(int_semester > 0):
	    return True, semester
	return False, NOT_TO_PRINT

#### PART 1 ####
# Filters a file of students' subscription to specific event:
#   orig_file_path: The path to the unfiltered subscription file
#   filtered_file_path: The path to the new filtered file
def fileCorrect(orig_file_path: str, filtered_file_path: str):
	original_file = open(orig_file_path, 'r')
	original_file_string = original_file.read()
	original_file_list = original_file_string.split('\n')

	filtered_file = open(filtered_file_path, 'w')
	members_dict = {}
	
	for line_string in original_file_list:
		line_list = line_string.split(',')
		
		if(line_list != ['']):
			is_valid_id, printed_id = checkIdValidation(line_list[0])
			is_valid_name, printed_name = checkNameValidation(line_list[1])
			is_valid_age, printed_age = checkAgeValidation(line_list[2])
			is_valid_birth_year, printed_birth_year = checkBirthYearValidation(line_list[2], line_list[3])
			is_valid_semester, printed_semester = checkSemesterValidation(line_list[4])
			
			if(is_valid_id and is_valid_name and is_valid_age and is_valid_birth_year and is_valid_semester):				
				string_value = printed_name + ", " + printed_age + ", " + printed_birth_year + ", " + printed_semester
	
				members_dict[printed_id] = string_value
	
	for key in sorted(members_dict.keys()):
		filtered_file.write(key + ", " + members_dict[key] + "\n")
							
	original_file.close()
	filtered_file.close()   
    
# Writes the names of the K youngest students which subscribed 
# to the event correctly.
#   in_file_path: The path to the unfiltered subscription file
#   out_file_path: file path of the output file
def printYoungestStudents(in_file_path: str, out_file_path: str, k: int) -> int:
    if(k <= ZERO):
	    return K_IS_NEGATIVE

    original_file = open(in_file_path, 'r')
    corrected_file = open(out_file_path, 'w+')
    fileCorrect(in_file_path, out_file_path)

    corrected_file_string = corrected_file.read()
    corrected_file_list = corrected_file_string.split('\n')
    
    list_of_lists = []
    #list that contain the name and the age and the id
    for member in corrected_file_list:  
	    member_list = member.split(', ')
	    if(member_list != ['']):
		    list_of_lists.append([member_list[1], int(member_list[2]), int(member_list[0])])  #append internal list
	
    list_of_lists = sorted(list_of_lists, key = lambda x: (x[1], x[2]))

    corrected_file.close()	
    
    num_of_members = len(list_of_lists)
    youngest_students_file = open(out_file_path, 'w')
    if(num_of_members <= k):
        for member in list_of_lists:
            youngest_students_file.write(str(member[0]) + "\n")
    else:
        for member in list_of_lists[0:k]:
            youngest_students_file.write(str(member[0]) + "\n")

    original_file.close()
    youngest_students_file.close()	
    
    if(num_of_members < k): 
        return num_of_members
    else:
        return k

# Calculates the avg age for a given semester
#   in_file_path: The path to the unfiltered subscription file
#   retuns the avg, else error codes defined.
def correctAgeAvg(in_file_path: str, semester: int) -> float:
    if(semester <= ZERO):
        return SEMESTER_IS_INVALID

    original_file = open(in_file_path, 'r')
    original_file_string = original_file.read()
    original_file_list = original_file_string.split('\n')
    
    members_dict = {}
    for line_string in original_file_list:
        line_list = line_string.split(',')
		
        if(line_list != ['']):
            is_valid_id, printed_id = checkIdValidation(line_list[0])
            is_valid_name, printed_name = checkNameValidation(line_list[1])
            is_valid_age, printed_age = checkAgeValidation(line_list[2])
            is_valid_birth_year, printed_birth_year = checkBirthYearValidation(line_list[2], line_list[3])
            is_valid_semester, printed_semester = checkSemesterValidation(line_list[4])

            if(is_valid_id and is_valid_name and is_valid_age and is_valid_birth_year and is_valid_semester):
                int_age_value = int(printed_age)
                int_semester_value = int(printed_semester)
                members_dict[printed_id] = [int_age_value, int_semester_value]
    if(printed_name and printed_birth_year):pass #remove unused variables
    original_file.close()
    counter = 0
    if(members_dict == {}):
        return ZERO
    else:
        age_sum = 0
        for value in members_dict.values():
            if(value[1] == semester):
                age_sum += value[0]
                counter += 1
        if(counter != 0):
            return age_sum / counter
        else: return ZERO

#### PART 2 ####
# Use SWIG :)
# print the events in the list "events" using the functions from hw1
#   events: list of dictionaries
#   file_path: file path of the output file
def printEventsList(events :list,file_path :str): #em, event_names: list, event_id_list: list, day: int, month: int, year: int):
	
	if(events and events[0]):
		current_date = events[0]["date"]
		for dict in events:
			if(EM.dateCompare(dict["date"], current_date) < ZERO):
				current_date = dict["date"]

		em = EM.createEventManager(current_date)
		for dict in events:
			EM.emAddEventByDate(em, dict["name"], dict["date"], dict["id"])
		EM.emPrintAllEvents(em, file_path)
		return em
	else: return None

def testPrintEventsList(file_path :str):
	events_lists=[{"name":"New Year's Eve","id":1,"date": EM.dateCreate(30, 12, 2020)},\
					{"name" : "annual Rock & Metal party","id":2,"date":  EM.dateCreate(21, 4, 2021)}, \
						{"name" : "Improv","id":3,"date": EM.dateCreate(13, 3, 2021)}, \
							{"name" : "Student Festival","id":4,"date": EM.dateCreate(13, 5, 2021)},    ]
	
	em = printEventsList(events_lists,file_path)
	for event in events_lists:
		EM.dateDestroy(event["date"])
	EM.destroyEventManager(em)

		
#### Main #### 
# feel free to add more tests and change that section. 
# sys.argv - list of the arguments passed to the python script
if __name__ == "__main__":
	import sys
	if len(sys.argv)>1:
		testPrintEventsList(sys.argv[1])




