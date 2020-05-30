####Classe Responsável por modelar um estado com base no seu nome e id#####
class State:
    def __init__(self, name,is_final):
        self.__name = name
        self.__transitions = []
        self.is_final = is_final

    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.__id = id

    def set_transition(self, symbol, destiny):
        self.transition = Transition(origin=self)
        self.transition.set_destiny(destiny)
        self.transition.set_symbol(symbol)
        self.__transitions.append(self.transition)

    def get_transitions(self):
        return self.__transitions

    def get_transition(self,symbol):
        for transition in self.__transitions:
            if(transition.get_symbol()==symbol):
                return transition
        return False
    def get_transitions_list_by_symbol(self,symbol):
        tr = []
        for transition in self.__transitions:
            if(transition.get_symbol()==symbol):
                tr.append(transition)
        return tr
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


#### Classe responsável por modelar as transições de estados no automato #####
class Transition:
    def __init__(self, origin,destiny=None,symbol=None):
        self.__destiny = destiny
        self.__symbol = symbol
        self.__origin = origin

    def get_origin(self):
        return self.__origin

    def get_destiny(self):
        return self.__destiny

    def get_symbol(self):
        return self.__symbol

    def set_origin(self, origin):
        self.__origin = origin

    def set_destiny(self, destiny):
        self.__destiny = destiny

    def set_symbol(self, symbol):
        self.__symbol = symbol


####Classe Responsável por modelar um automato com base em sua descrição formal#####
class Automato:
    def __init__(self):
        self.__count_states = 0
        self.__states_list = []
        self.__transitions_table = []
        self.__input_symbols = []
        self.__final_states = []

    def create_state(self, name, is_final):
        self.state = State(name,is_final=is_final)
        self.state.set_id(self.__count_states)
        if (is_final):
            self.__final_states.append(self.state)
        self.__states_list.append(self.state)
        self.__count_states += 1
        return self.state

    ########### Getters ##########
    def get_state_by_id(self, id):
        return self.__states_list[id]

    def get_state_by_name(self, name):
        for state in self.__states_list:
            if (state.get_name() == name):
                return state
        return None

    def get_transitions_table(self):
        self.transitions_table = []
        for state in self.__states_list:
            state_transtitions = state.get_transitions()
            for transition in state_transtitions:
                self.transitions_table.append(transition)
        return self.transitions_table

    def get_states_list(self):
        return self.__states_list

    def get_initial_state(self):
        return self.__initial_state

    def get_final_state(self):
        return self.__final_states

    def get_input_symbols(self):
        for state in self.__states_list:
            for transition in state.get_transitions():
                if (transition.get_symbol() not in self.__input_symbols):
                    self.__input_symbols.append(transition.get_symbol())
        return self.__input_symbols

    ############# Setters #############
    def set_initial_state(self, state):
        if (type(state) == State):
            self.__initial_state = state

    def set_final_state(self, state):
        if (type(state) == State):
            self.__final_state = state

    def set_state(self, state):
        if (type(state) == State):
            self.__states_list.append(state)




