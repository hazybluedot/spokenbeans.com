from django import forms
from django.forms.widgets import RadioSelect, TextInput
from SnB.invoice.widgets import HintedRadioFieldRenderer
from SnB.coffee.models import Origin

class OrderForm(forms.Form):
    ROAST_CHOICES=(
        ('light','Light'),
        ('city','City'),
        ('dark','Dark'),
        )
    AMOUNT_CHOICES=(
        ('pint','Pint'),
        ('quart','Quart'),
        )
    FREQ_CHOICES=(
        (1,'Every week'),
        (2,'Every two weeks'),
        (4,'Every four weeks'),
        )

    CYCLE_CHOICES=(
	(1,'4'),
	(2,'8'),
	(3,'12'),
	(4,'16'),
	(5,u"\u221E, billed monthly")
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
    DELIVERY_CHOICES=(
        ('1','Home'),
        ('2','Office'),
        )
    origin = forms.ChoiceField(widget=RadioSelect(renderer=HintedRadioFieldRenderer), choices=ORIGIN_CHOICES)
    roast = forms.ChoiceField(widget=RadioSelect(renderer=HintedRadioFieldRenderer), choices=ROAST_CHOICES)
    frequency = forms.ChoiceField(widget=RadioSelect(renderer=HintedRadioFieldRenderer), choices=FREQ_CHOICES)
    amount = forms.ChoiceField(widget=RadioSelect(renderer=HintedRadioFieldRenderer), choices=AMOUNT_CHOICES)
    cycles = forms.ChoiceField(widget=RadioSelect(renderer=HintedRadioFieldRenderer), choices=CYCLE_CHOICES)
    #cycles = forms.CharField(widget=forms.TextInput(attrs={'class':'small'}),  help_text='x4 = total number of deliveries')
    name = forms.CharField(max_length=100)
    address = forms.CharField()
    email = forms.EmailField()
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': '3'}), help_text='any special delivery instructions? e.g. leave on the back porch', required=False)
    delivery_day = forms.ChoiceField(widget=RadioSelect(renderer=HintedRadioFieldRenderer), choices=DELIVERY_CHOICES)
