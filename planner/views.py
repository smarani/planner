from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from planner.models import Courses1, Major

def index(request):
    latest_course_list= Major.objects.all()
    context = {'latest_course_list': latest_course_list}
    return render(request, 'planner/index.html', context)

def user(request, course_id):
	return HttpResponse("You are user %s" % course_id)

def detail(request, course_id):
    major = get_object_or_404(Major, pk=course_id)
    return render(request, 'planner/detail.html', {'major': major})

def results(request, course_id):
    return HttpResponse("You're looking at the results of course %s." % course_id)

def vote(request, course_id):
    p = get_object_or_404(Major, pk=course_id)
    try:
        selected_choice = p.courses1_set.get(pk=request.POST['choice'])
    except (KeyError, Courses1.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'planner/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        #selected_choice.votes += 1
       # selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('planner:results', args=(p.id,)))