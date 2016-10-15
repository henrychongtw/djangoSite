from django.conf.urls import url
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Choice, Question
from . import views

app_name ='polls'

urlpatterns = [
	#ex: /polls/
	url(r'^$', views.index, name='index'),
	#/polls/5/
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	#/polls/5/results/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	#/polls/5/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
] 

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['chioce'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html',{
				'question': question,
				'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing with POST data
		# This prevents data from being posted twice if a user hits the back button
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))