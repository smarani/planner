from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#from compare import setUser
from planner.models import Courses1, Major

def index(request):
    latest_course_list= Major.objects.all()
    context = {'latest_course_list': latest_course_list}
    return render(request, 'planner/index.html', context)

def detail(request, major_id):
    major = get_object_or_404(Major, pk=major_id)
    

    return render(request, 'planner/detail.html', {'major': major})
def name(request):
	try:
		username = request.POST['username']
		coursetext = request.POST['courses']
		password = request.POST['password']
		majortext = get_object_or_404(Major, pk = request.POST['major_select'])
		return HttpResponse("HI %s, you've taken %s and you are a %s major" % (username, coursetext, majortext))
	except:
		return HttpResponse("Failed")


def results(request, major_id):
    return HttpResponse("You're looking at the results of course %s." % major_id)

def vote(request, major_id):
    p = get_object_or_404(Major, pk=major_id)
    selected = ''
    j = len(p.courses1_set.all())

    for i in range(0, j): 
    	pk = ''
    	try:
    		pk = request.POST['choice'+str(i+1)]
    	except:
    		pass
    	if pk != '':
    		selected = selected + ', ' + pk
    return HttpResponse("You selected:%s" %selected)