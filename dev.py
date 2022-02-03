from english_words import english_words_set
import random
import string

WORD_LENGTH = 5
N_WORDS = 3
ENGLISH_WORDS_LIST = [*english_words_set]


answers = AnswerGenerator()



class GridGenerator:
    def __init__(self, word_length = WORD_LENGTH, n_words = N_WORDS) -> None:
        self._word_length = word_length
        self._n_words =n_words 
        self.empty_grid = self._generate_empty_grid()

    def _generate_empty_grid(self) -> list:
        row = []
        grid = []
        for _ in range(self._word_length):
            
            row.append('?')
        for _ in range(self._n_words):
            grid.append(row)
        return grid 

class AnswerGenerator:
    def __init__(self) -> None:
        self.eligible_words = [w.lower() for w in ENGLISH_WORDS_LIST if len(w) == WORD_LENGTH]
        self.words = self._select_words()

    def _select_words(self) -> list:
        return random.sample(self.eligible_words, N_WORDS)

class WordGuesser:
    def __init__(self) -> None:
        self.eligible_words = [w.lower() for w in ENGLISH_WORDS_LIST if len(w) == WORD_LENGTH]
        self.remaining_words = self.eligible_words
        self.current_grid = GridGenerator().empty_grid
        self.alphabet = list(string.ascii_lowercase)
        self.temp_alphabet = self.alphabet
        self.complete_words = [False] * N_WORDS
        self.current_word = 0

    def get_remaining_indices(self):
        return [i for i in range(len(self.current_grid[self.current_word])) if self.current_grid[self.current_word][i] == '?']

    def update_word_of_interest(self):
        for i, b in enumerate(self.complete_words):
            if b == False:
                self.current_word = i 
                break       

    def reset_temp_alphabet(self):
        self.temp_alphabet = self.alphabet
    
    def drop_letter_from_temp_alphabet(self, guess):
        self.temp_alphabet.remove(guess)

    def guess_letter(self):
        return random.sample(self.temp_alphabet)

    def evaluate_letter(self):
        guess = self.guess_letter()
        locs = self.get_remaining_indices()
        loc = random.sample(locs, 1)

        if answers[self.current_word][loc] == guess:
            self.current_grid[self.current_word] = guess
        elif guess in answers[current_word]:
            locs.remove(loc)
            while not locs:
                loc = random.sample(locs, 1)
                if answers[self.current_word][loc] == guess:
                    self.current_grid[self.current_word] = guess
                else: 
                    locs.remove(loc)
        elif guess not in answers[current_word]:
           self.drop_letter_from_temp_alphabet()

    
    def guess_row(self):
        while ''.join(self.current_grid[self.current_word]) != answers[current_word]:
            self.evaluate_letter()
            
        if ''.join(self.current_grid[self.current_word]) == answers[current_word]:


