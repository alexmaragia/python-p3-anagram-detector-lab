class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, word_list):
        matches = []
        for word in word_list:
            if self._is_anagram(word):
                matches.append(word)
        return matches

    def _is_anagram(self, other_word):
        if self.word.lower() == other_word.lower():
            return False
        return sorted(other_word.lower()) == self.sorted_word