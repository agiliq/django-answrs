from django import forms
from models import *

class QuestionForm(forms.ModelForm):
    def __init__(self, user = None, *args, **kwargs):
        self.user = user
        super(QuestionForm, self).__init__(*args, **kwargs)
    
    def save(self):
        question = Question(user = self.user, category = self.cleaned_data['category'], title =self.cleaned_data['title'], description = self.cleaned_data['description'])
        question.save()
        return question
        
    class Meta:
        model = Question
        exclude = ('user', 'is_open')
    
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('slug')
        
class AnswerForm(forms.Form):
    def __init__(self, user = None, question = None, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.user = user
        self.question = question
        
    def save(self):
        answer = Answer(text = self.cleaned_data['answer'])
        answer.user = self.user
        answer.question = self.question
        answer.save()
        return answer
    
    answer = forms.CharField(widget = forms.Textarea)
    
class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('best_answers', 'answers', 'points', 'user')
        
