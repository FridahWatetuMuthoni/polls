from .models import Choice, Question
from django.forms import ModelForm,modelformset_factory


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

ChoiceForm = modelformset_factory(
    Choice,
    fields=('choice_text',),  # Only the fields you want to display
    extra=3,  # Number of extra choice forms
    can_delete=False  # Disable deleting in this case
)

