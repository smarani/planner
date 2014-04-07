from planner.models import Courses1, Major, Requirements, Users, UserClasses, FallCourse

def setUser(username1, password1, classes1):
	p = Users(username= username1, password= password1)
	p.save()
	cla = classes1.split(, )
	for thing in cla:
		p.userclasses_set.create(course=thing)
	p.save()
