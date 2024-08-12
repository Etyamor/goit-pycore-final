from prompt_toolkit.completion import WordCompleter
from typing import List

class AutoCompleter:
    def __init__(self, words: List[str]):
        self.completer = WordCompleter(words)

    def get_completer(self) -> WordCompleter:
        return self.completer