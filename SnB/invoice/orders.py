from django import forms
from django.forms.widgets import RadioSelect, TextInput
from SnB.invoice.widgets import HintedRadioFieldRenderer
from SnB.coffee.models import Origin

class OrderForm(forms.Form):
    ROAST_CHOICES=(
        ('light','light'),
        ('city','city'),
        ('dark','dark'),
        )
    AMOUNT_CHOICES=(
        ('pint','pint'),
        ('quart','quart'),
        )
    FREQ_CHOICES=(
        (1,'Every Week'),
        (2,'Every two weeks'),
        (4,'Every four weeks'),
        )
    ORIGIN_CHOICES=Origin.get_choices()
        #(
        #('selva','Selva Negra Estate', 'Nicaragua'),
        #('bob', 'bob-o-link', 'Brazil'),
        #('don', 'Don Rigo Estate', 'Columbia'),
        #('lightening', 'Black Lightening', 'Darkest of the dark'),
        #('pub', 'Pub Blend', 'like you\'re at the Underground'),
        #('cyc', 'Cyclist\'s Pick', 'We pick, you enjoy'),
        #)
    origin = forms.ChoiceField(widget=RadioSelect(renderer=HintedRadioFieldRenderer), choices=ORIGIN_CHOICES)
    roast = forms.ChoiceField(widget=RadioSelect(renderer=HintedRadioFieldRenderer), choices=ROAST_CHOICES)
    frequency = forms.ChoiceField(widget=RadioSelect(renderer=HintedRadioFieldRenderer), choices=FREQ_CHOICES)
    amount = forms.ChoiceField(widget=RadioSelect(renderer=HintedRadioFieldRenderer), choices=AMOUNT_CHOICES)
    cycles = forms.IntegerField(widget=TextInput,  help_text='x4 = total number of deliveries')
    name = forms.CharField(max_length=100)
    address = forms.CharField()
    email = forms.EmailField()
    notes = forms.Textarea(help_text='any special delivery instructions? e.g. leave on the back porch', blank=True)
    #cc_myself = forms.BooleanField(required=False)
