from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
joke_true = []
def get_jokes(n, flag=False):
    '''
           Функция get_jokes возвращает случайные шутки, собранные из трех слов и трех списков (nouns, adverbs, adjectives)
           n: колличество шуток
           flag=False/True: неуникальные/уникальные по умолчанию False
           joke: строка с готовой шуткой
           joke_true: список из шуток с уникальными словами
    '''
    for _ in range(n):
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        joke = f'{noun} {adverb} {adjective}'
        print(joke)
        if flag:
            joke_true = joke.split()
            for noun in nouns:
                for fun in joke_true:
                    if noun == fun:
                        nouns.remove(noun)
            for adverb in adverbs:
                for fun in joke_true:
                    if adverb == fun:
                        adverbs.remove(adverb)
            for adjective in adjectives:
                for fun in joke_true:
                    if adjective == fun:
                        adjectives.remove(adjective)

# get_jokes(3)
get_jokes(3,True)