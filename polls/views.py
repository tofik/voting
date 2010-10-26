from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from polls.models import Poll
from django.template import loader, Context, RequestContext
from django.core.urlresolvers import reverse

# def index(request):
#     latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#     # t = loader.get_template('polls/index.html')
#     # c = Context({
#     #         'latest_poll_list': latest_poll_list,
#     #         })
#     # return HttpResponse(t.render(c))
#     return render_to_response('polls/poll_list.html', {'latest_poll_list': latest_poll_list})


# def details(request, poll_id):
# #     try:
# #         p = Poll.objects.get(pk = poll_id)
# #     except Poll.DoesNotExist:
# #         raise Http404
#     p = get_object_or_404(Poll, pk = poll_id)
#     return render_to_response('polls/details.html', {'poll': p},
#                               context_instance = RequestContext(request))

# def results(request, poll_id):
#     p = get_object_or_404(Poll, pk = poll_id)
#     return render_to_response('polls/results.html', {'poll': p})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk = poll_id)
    try:
        selected_choice = p.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response('polls/object_detail.html', {
                'poll': p,
                'error_message': "You didn't select a choice",
                }, context_instance = RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls_results', args=(p.id,)))
