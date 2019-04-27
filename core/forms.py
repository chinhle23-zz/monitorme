from django import forms
from core.models import User, TrackerGroup, Answer, Question, Response
from registration.forms import RegistrationForm
from django.contrib.auth import get_user_model, authenticate, password_validation
from django.contrib.auth.models import Group
    # https://docs.djangoproject.com/en/2.2/topics/auth/default/#groups
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()

class CustomRegistrationForm(RegistrationForm):
    # https://github.com/macropin/django-registration/blob/master/registration/forms.py
    # https://github.com/django/django/blob/master/django/contrib/auth/forms.py

    email = forms.EmailField(
        label='E-mail', 
        widget=forms.TextInput(attrs={'class': ''}),
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': ''}),
        # help_text=password_validation.password_validators_help_text_html(),
        help_text=None,
    )

    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': ''}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

        
    name = forms.CharField(
        label= 'Name',
        max_length=100,
        widget=forms.TextInput(attrs={'required': True})
    )

    disclosure_accepted = forms.BooleanField(required=True, label="By registering for and using the Monitor-Me website and/or mobile application, you are deemed to have read and agreed to the following terms and conditions: ")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = None

    class Meta(RegistrationForm.Meta): # Meta is a class defined in a class
        
        widgets = {
            'username': forms.TextInput(attrs={'class': ''}),
        }

        fields = ['username', 'name', 'email', 'password1', 'password2']      

class NewGroupForm(forms.Form):

    name = forms.CharField(label='Name',
        max_length=512,
        widget=forms.TextInput(attrs={'placeholder': 'enter a group name'})
    )
    def save(self, **kwargs):
        if self.is_valid():
            group_properties = {'name': self.cleaned_data['name']}
            group_properties.update(kwargs)
            return Group.objects.create(**group_properties)
        return None


class NewTrackerInstanceForm(forms.Form):
    pass
    # https://docs.djangoproject.com/en/2.2/topics/forms/#building-a-form-in-django
    # tracker = forms.ModelChoiceField(required=True, queryset=TrackerGroup.objects.all())
        # https://docs.djangoproject.com/en/2.2/ref/forms/fields/#modelchoicefield
        # https://docs.djangoproject.com/en/2.2/topics/db/queries/
        # this is no longer needed as the tracker pk can be passed as a variable in the URL
    

class NewResponseForm(forms.Form):
    # credit: https://stackoverflow.com/questions/291945/how-do-i-filter-foreignkey-choices-in-a-django-modelform
    def __init__(self, question, *args, **kwargs):
        super(NewResponseForm, self).__init__(*args, **kwargs)
        self.fields['answer'] = forms.ModelMultipleChoiceField(Answer.objects.filter(question_id=question))
            # https://docs.djangoproject.com/en/2.2/ref/forms/fields/#modelmultiplechoicefield  

class CreateResponseForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(CreateResponseForm, self).__init__(*args, **kwargs)
        self.fields['answer'] = forms.ModelMultipleChoiceField(
            queryset=Answer.objects.filter(question_id=question.id),
            label=f'{question.tracker_question}'
        )
            # https://docs.djangoproject.com/en/2.2/ref/forms/fields/#modelmultiplechoicefield 
            
class ResponseForm(forms.ModelForm):
    # https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/
    # def __init__(self, *args, **kwargs):
    #     super(ResponseForm, self).__init__(*args, **kwargs)
    #     self.fields['answers'].empty_label = None
    answers = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset = Answer.objects.filter(question_id=12),
        label = f'{Answer.objects.filter(question_id=12)[0].question.tracker_question}'
    )
    
    class Meta:
        model = Response
        fields = ['answers',]

class CreateTrackerQuestionAnswerForm(forms.Form):
    tracker_name = forms.CharField(
        label='Enter a name for your tracker',
        max_length=512,
        widget=forms.TextInput(attrs={'placeholder': 'Type tracker name here'}),
    )
    question_description = forms.CharField(
        label='Enter a question',
        max_length=512,
        widget=forms.TextInput(attrs={'placeholder': 'Type question here'}),
    )
    answer_name1 = forms.CharField(
        label='Enter answer',
        max_length=512,
        widget=forms.TextInput(attrs={'placeholder': 'Type answer here'}),
    )
    answer_name2 = forms.CharField(
        label='Enter answer',
        max_length=512,
        widget=forms.TextInput(attrs={'placeholder': 'Type answer here'}),
    )
    answer_name3 = forms.CharField(
        label='Enter answer',
        max_length=512,
        widget=forms.TextInput(attrs={'placeholder': 'Type answer here'}),
        required=False,
    )

class CreateQuestionAnswerForm(forms.Form):
    question_description = forms.CharField(
        label='Enter a question',
        max_length=512,
        widget=forms.TextInput(attrs={'placeholder': 'Type question here'}),
    )
    answer_name1 = forms.CharField(
        label='Enter answer',
        max_length=512,
        widget=forms.TextInput(attrs={'placeholder': 'Type answer here'}),
    )
    answer_name2 = forms.CharField(
        label='Enter answer',
        max_length=512,
        widget=forms.TextInput(attrs={'placeholder': 'Type answer here'}),
    )
    answer_name3 = forms.CharField(
        label='Enter answer',
        max_length=512,
        widget=forms.TextInput(attrs={'placeholder': 'Type answer here'}),
        required=False,
    )

class CreateAnswerForm(forms.Form):
    answer_name = forms.CharField(
        label='',
        max_length=512,
        widget=forms.TextInput(attrs={'placeholder': '+ another answer'}),
    )
    def save(self, **kwargs):
        if self.is_valid():
            answer_properties = {
                "name": self.cleaned_data['answer_name'],
            }
            answer_properties.update(kwargs)
            return Answer.objects.create(**answer_properties)
        return None
