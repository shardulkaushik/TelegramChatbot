from fuzzywuzzy import fuzz
class State:

    def __init__(self, state_id, state_type,  description, options, previous_state, next_state, identifier):
        self.state_id = state_id
        self.state_type = state_type
        self.description = description
        self.options = options
        self.previous_state = previous_state
        self.next_state = next_state
        self.identifier = identifier

    def __dict__(self):
        return {'description': self.description, 'options': self.options}

    def switch_to_next_state(self, message):

