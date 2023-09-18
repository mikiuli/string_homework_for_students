"""
Вы - начинающий журналист. Накануне вечером вы написали статью
про кошек для ветеринарного журнала,
но забыли заблокировать компьютер. На утро вы обнаружили,
что вашей собаке не понравилось, что пишете вы про кошек,
а не про собак.
Она испортила вам статью и оставила следующую записку:
1) я заменила все слова "cat" в статье на "woof-woof"
2) я развернула каждое предложение и добавила в его конец,
перед точкой, строку, состояющую из символа "!".
Длина этой строки восклицательных знаков равна длине предложения
(без учета точки).
3) я перевела все предложения в верхний регистр

Попробуй вернуть все назад, woof-woof!

Ваша задача вернуть текст в первозданный вид.
Ограничения:
1) В результате предложения разделены символом '.\n'.
2) В результате все предложения начинаются с буквы верхнего регистра.
Это единственная буква в верхнем регистре в предложении.

Исходный текст представлен в файле correct_article.txt.
Испорченный текст представлен в файле wrong_article.txt.

Реализуйте код, который восстановит статью и вернет ее
в качестве результата работы функции.

Проверка результата:
pytest ./4_safe_text/test.py
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_correct_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles',
                                    'correct_article.txt'))


def get_wrong_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles',
                                    'wrong_article.txt'))


def recover_article() -> str:
    """Recover wrong article to correct version."""
    wrong_article = get_wrong_article()
    wrong_sentences_list = wrong_article.split(SPLIT_SYMBOL)
    correct_sentences_list = [sentence[(int(len(sentence)/2))-1::-1]
                              .lower()
                              .replace('woof-woof', 'cat')
                              .capitalize()
                              for sentence in wrong_sentences_list
                              ]
    return SPLIT_SYMBOL.join(correct_sentences_list)
