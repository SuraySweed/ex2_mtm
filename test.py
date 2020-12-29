from eventManager import *

def testPrintEventsEmptyList(file_path :str):
	events_lists = []
	em = printEventsList(events_lists,file_path)
	if(events_lists and events_lists[0]):
		for event in events_lists:
			EM.dateDestroy(event["date"])
		EM.destroyEventManager(em)

def testOnlyOneEvent(file_path :str):
	events_lists = [{"name":"New Year's Eve","id":1,"date": EM.dateCreate(30, 12, 2020)}]
	em = printEventsList(events_lists,file_path)
	if(events_lists):
		for event in events_lists:
			EM.dateDestroy(event["date"])
		EM.destroyEventManager(em)

def testPrintSameEventsDates(file_path :str):
	events_lists=[{"name":"New Year's Eve","id":1,"date": EM.dateCreate(30, 12, 2020)},\
					{"name" : "annual Rock & Metal party","id":2,"date":  EM.dateCreate(21, 4, 2021)}, \
						{"name" : "Improv","id":3,"date": EM.dateCreate(21, 4, 2021)}, \
							{"name" : "Student Festival","id":4,"date": EM.dateCreate(30, 12, 2020)},    ]
	em = printEventsList(events_lists,file_path)
	if(events_lists):
		for event in events_lists:
			EM.dateDestroy(event["date"])
		EM.destroyEventManager(em)


if __name__ == '__main__':
    fileCorrect("tests/input","tests/out1")
    num1 = correctAgeAvg("tests/input", 3)
    print(float(num1))
    printYoungestStudents("tests/input","tests/out2", 2)
    testPrintEventsEmptyList("tests/output3")
    testOnlyOneEvent("tests/output4")
    testPrintSameEventsDates("tests/output5")
    testPrintEventsList("tests/output6")