#from util import flatatt
from django.utils.html import escape, conditional_escape
from django.utils.encoding import StrAndUnicode, force_unicode
from django.utils.safestring import mark_safe
from django.forms import widgets

class RightRadioInput(widgets.RadioInput):
    """
    An object used by RadioFieldRender that represents a single <input type='radio'>.
    """
    
    def __unicode__(self):
        if 'id' in self.attrs:
            label_for = ' for="%s_%s"' % (self.attrs['id'], self.index)
        else:
            label_for = ''
        choice_label = conditional_escape(force_unicode(self.choice_label))
        choice_hint = conditional_escape(force_unicode(self.choice_hint))
        return mark_safe(u'<label%s>%s </label>%s' % (label_for, choice_label, self.tag()))
    

class HintedRadioInput(widgets.RadioInput):
    """
    An object used by RadioFieldRenderer that represents a single
    <input type='radio'>.
    """

    def __init__(self, name, value, attrs, choice, index):
        self.name, self.value = name, value
        self.attrs = attrs
        self.choice_value = force_unicode(choice[0])
        self.choice_label = force_unicode(choice[1])
        try:
            self.choice_hint = force_unicode(choice[2])
        except IndexError:
            self.choice_hint = None

        self.index = index

    def __unicode__(self):
        if 'id' in self.attrs:
            label_for = ' for="%s_%s"' % (self.attrs['id'], self.index)
        else:
            label_for = ''
        choice_label = conditional_escape(force_unicode(self.choice_label))
        if self.choice_hint:
            choice_hint_tag = "<span class=\"small\">%s</span>" % conditional_escape(force_unicode(self.choice_hint))
        else:
            choice_hint_tag = ""
        return mark_safe(u'<label%s>%s %s</label>%s' % (label_for, choice_label, choice_hint_tag, self.tag()))

class HintedRadioFieldRenderer(widgets.RadioFieldRenderer):
    """
    An object used by RadioSelect to enable customization of radio widgets.
    """

    def __init__(self, name, value, attrs, choices):
        self.name, self.value, self.attrs = name, value, attrs
        self.choices = choices

    def __iter__(self):
        for i, choice in enumerate(self.choices):
            yield HintedRadioInput(self.name, self.value, self.attrs.copy(), choice, i)

    def __getitem__(self, idx):
        choice = self.choices[idx] # Let the IndexError propogate
        return HintedRadioInput(self.name, self.value, self.attrs.copy(), choice, idx)

    #def render(self):
    #    """Outputs a <ul> for this set of radio fields."""
    #    return mark_safe(u'<ul>\n%s\n</ul>' % u'\n'.join([u'<li>%s</li>'
    #            % force_unicode(w) for w in self]))
