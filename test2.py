from prompt_toolkit import prompt
from AutoCompleter import AutoCompleter

words = ['command1', 'command2', 'command3']
ac = AutoCompleter(words)
text = prompt('Write your command: ', completer=ac.get_completer())