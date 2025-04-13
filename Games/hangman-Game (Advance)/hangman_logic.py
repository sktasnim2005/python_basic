# hangman_logic.py

def get_hint(answer_word, guessed_letters):
    return [ch if ch in guessed_letters else "_" for ch in answer_word]

def is_word_guessed(hint):
    return "_" not in hint
