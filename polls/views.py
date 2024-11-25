from django.shortcuts import render, get_object_or_404, redirect
from .models import Question,Choice
from .forms import ChoiceForm, QuestionForm
from django.db import transaction

# Create your views here.
def home(request):
    questions = Question.objects.all()
    context = {
        "questions":questions
    }
    return render(request, 'home.html', context)


def results(request,pk):
    question = get_object_or_404(Question, pk=pk)
    print(question)
    context = {
        "question":question
    }
    return render(request, 'results.html',context)

def vote(request,pk):
    question = get_object_or_404(Question, pk=pk)
    choices = question.choices.all()

    if request.method == 'POST':
        choice_id=request.POST.get('polls')
        choice = Choice.objects.get(id=choice_id)
        choice.votes = choice.votes + 1
        choice.save()
        return redirect('/')

    context = {
        "question":question,
        "choices":choices
    }
    return render(request, 'vote.html', context)

def create(request):    
    if request.method == 'POST':
        question = QuestionForm(request.POST)
        choice = ChoiceForm(request.POST)
        
        if question.is_valid() and choice.is_valid():
            with transaction.atomic():
                #save the question
                question = question.save()
                
                #save the choices
                choices = choice.save(commit=False)
                for choice in choices:
                    choice.question = question
                    choice.save()
            return redirect('home')
    
    question_form = QuestionForm()
    choice_form = ChoiceForm(queryset=Choice.objects.none())

    context = {
        'question_form':question_form,
        'choice_form':choice_form
    }
    return render(request, 'create.html', context)