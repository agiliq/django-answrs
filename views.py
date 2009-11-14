from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

import random

from answrs.models import *
from answrs import aforms

def index(request):
    payload = {}
    return render(request, 'answrs/index.html', payload)

@login_required
def ask(request):
    """Ask a question"""
    if request.method == 'POST':
        form = aforms.QuestionForm(request.user, request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_absolute_url())
    elif request.method == 'GET':
        form = aforms.QuestionForm()
    payload = {'form':form}
    return render(request, 'answrs/ask.html', payload)

@login_required
def add_cat(request):
    """Add a category"""
    if request.method == 'POST':
        form = aforms.CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save()
            return HttpResponseRedirect(cat.get_absolute_url())
    elif request.method == 'GET':
        form = aforms.CategoryForm()
        payload = {'form':form}
        return render(request, 'answrs/add_cat.html', payload)
    
@login_required
def answer(request, id):
    """Answer the question with the given id"""
    question = Question.objects.get(id = id)
    answers = question.answer_set.all()
    if request.method == 'POST':
        form = aforms.AnswerForm(user = request.user, question = question, data = request.POST)
        print 'asdf'
        if form.is_valid():
            answer = form.save()
            return HttpResponseRedirect('.')   
    elif request.method == 'GET':
        form = aforms.AnswerForm()
    payload = {'question':question, 'answers':answers, 'form':form, }
    return render(request, 'answrs/answers.html', payload)
    
def view_cat(request, slug):
    """Shows a actegory page"""
    cat = Category.objects.get(slug = slug)
    return HttpResponse(cat.name)

def profile(request, username = None):
    """Shows a profile page"""
    if username == None:
        user = request.user
    else:
        user = User.objects.get(username = username)
    profile = user.get_profile()
    if request.method == 'POST':
        form = aforms.ProfileImageForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('.')
    elif request.method == 'GET':
        form = aforms.ProfileImageForm(instance = profile)
    payload = {'form':form, 'profile':profile, 'user':user }
    return render(request, 'answrs/profile.html', payload)
    

def randompage(request):
    for i in xrange(5):
        count = Question.objects.all().count()
        randcount = random.randint(1, count)
        question = Question.objects.get(id = randcount)
        if question.is_open:
            return HttpResponseRedirect(question.get_absolute_url())
    return HttpResponseRedirect(question.get_absolute_url())
    
def render(request, template, payload):
    all_cat = Category.objects.all()
    open_questions = Question.objects.filter(is_open = True)[:10]
    recently_answered = Question.objects.all().order_by('-created_on')[:10]
    payload.update({'all_cat':all_cat, 'open_questions':open_questions, 'recently_answered':recently_answered})
    return render_to_response(template, payload, RequestContext(request))


    
    
