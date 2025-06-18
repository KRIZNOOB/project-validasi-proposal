def lang():
    transition = {
        ('q1', 'upload'): {'q2'},
        ('q2', 'complete'): {'q3'},
        ('q2', 'incomplete'): {'q1'},
        ('q3', 'next'): {'q4'},
        ('q4', 'next'): {'q5'},
        ('q5', 'next'): {'q6'},
        ('q6', 'next'): {'q7'},
        ('q7', 'next'): {'q8'}
    }
    start = {'q1'}
    final = {'q8'}
    return transition, start, final

def delta(state, input, transition):
    return transition.get((state, input), set())

def hat_delta(states, input_string, transition):
    current_states = states
    for symbol in input_string:
        next_states = set()
        for state in current_states:
            next_states.update(delta(state, symbol, transition))
        current_states = next_states
    return sorted(current_states)

def run_nfa(state, input):
    transition, start, final = lang()
    next_states = delta(state, input, transition)
    return next_states.pop() if next_states else state