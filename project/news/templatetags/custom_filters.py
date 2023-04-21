import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# слова попадающие под цензуру
CURSE_WORDS = ['огромный', 'динамики', 'коаксиальные', 'начиная', 'возможно', 'времени',
               'подвижные', 'системы', 'для', 'сабвуфер', 'акустика', 'огромный', 'создаст',
               'оснащение', 'кинотеатр', 'крупный', ]


@register.filter(name='censorship')
def censor(text):
    # перебор списка слов и подставление *, при совпадении
    for el in CURSE_WORDS:
        pattern = re.compile(r'\b{}\b'.format(el), re.IGNORECASE)
        censored_word = el[0] + '*'*(len(el)-1)
        text = re.sub(pattern, censored_word, text)
    return mark_safe(text)
