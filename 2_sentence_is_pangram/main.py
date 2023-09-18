"""
Панграмма - предложение, которое использует каждую букву алфавита
(в нашем случае - английского алфавита).
Необходимо реализовать код, который скажет, является предложение
панграммой или нет.
Буквы в верхнем и нижнем регистрах считаются эквивалентными.
Предложения содержат только буквы английского алфавита, без пробелов и т.п.
Проверка:
pytest ./2_sentence_is_pangram/test.py
"""


def is_sentence_is_pangram(sentence: str) -> bool:
    """Check for pangram."""
    alphabet_letters_set = set('abcdefghijklmnopqrstuvwxyz')
    sentence_letters_set = set(sentence.lower())
    return alphabet_letters_set == sentence_letters_set
