# from django.forms import forms
from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# from polls.forms import NameForm
from django import forms
from django.views.generic import View
from .forms import NameForms
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
import logging

# logger = logging.getLogger(__name__)


class MyView(View):
    def get(self, request):
        return HttpResponse('result')

class AboutView(TemplateView):
    template_name = "about.html"

class IndexView(View):
    def get(self, request, *args, **kwargs):
        latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'polls/index.html', context)


# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

class DetailView(View):

    def get(self, request, question_id):
        # question_id = 1

        question = get_object_or_404(Question, pk=question_id)
        return render(request,'polls/detail.html', {'question': question})


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question':question})

class ResultsView(DetailView):
    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class VoteView(View):
    def post(self, request, question_id):
        # logger.debug(f"vote().question_id: {question_id}")
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def vote(request, question_id):
#     # logger.debug(f"vote().question_id: {question_id}")
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




'''
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

def name(request):
    if request.method =='POST':
        form = NameForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['your_name']
            print('new_name = ', new_name)
            return HttpResponseRedirect('/polls/form-class-ex-thanks/')
    else:
        form = NameForm()
        context={'form': form}
    return render(request, 'polls/name.html', {'form': form})

def test(request):
    print('function test in polls/views.py is run')
    return render(request, 'polls/index.html')

class MyFormView(View):
    form_class = NameForms
    initial = {'your_name': 'Sherlock'}
    template_name = 'polls/name.html'

    # GET 요청을 받았을 경우, 즉 처음 해당 URL로 접속할 때
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {'form': form}
        return render(request, self.template_name, context)

    # POST 요청을 받았을 경우, 즉 POST 데이터를 받았을 경우
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['your name']
            print('new_name = ', new_name)

            return HttpResponseRedirect('polls/form-class-ex-thanks/')
        # request.POST의 데이터가 유효하지 않으면
        return render(request, self.template_name, {'form': form})

class MyFormView2(FormView) :
    form_class = NameForms
    initial = {'your name': 'Homes'}
    template_name = 'polls/name.html'
    success_url = 'polls/form-class-ex-thanks'

    def form_valid(self, form):
        new_name = form.cleaned_data['your_name']
        print('new_name_of_MyFormView2 = ', new_name)

        return super(MyFormView2, self).form_valid(form)

# class BaseView(TemplateView):
#     template_name = 'polls/indexchild.html'
'''''''''