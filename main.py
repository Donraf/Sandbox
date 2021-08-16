import random


def mix_words(text):
    list_words = text.split()
    for id_, word in enumerate(list_words):
        list_words[id_] = list(word)
        queue = []
        queue.append(list_words[id_].pop(0))
        len_word = len(list_words[id_])
        while len_word > 1:
            rand_int = random.randint(0, len_word - 2)
            queue.append(list_words[id_].pop(rand_int))
            len_word = len(list_words[id_])
        if len_word > 0:
            queue.append(list_words[id_].pop(0))
        list_words[id_] = ''.join(queue)
    list_words = ' '.join(list_words)
    print(list_words + '\n')


text_1 = "Я сегодня был в Москве"
text_2 = "Возьмите свои вещи из открывшейся ячейки"
text_3 = "За столом сидят несколько человек"
text_4 = "Убедительная просьба надеть свои маски в общественном месте"
text_5 = "Я был разочарован когда услышал его мнение на этот счет"
text_6 = "Прогноз погоды на сегодня предвещает прекрасный день"
text_7 = "Я одолжил у него книгу на выходные"
text_8 = "Будучи хорошо воспитанным человеком он предпочитает не\
 участвовать в подобных мероприятиях"
text_arr = (text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8)
for text_sample in text_arr:
    mix_words(text_sample)
