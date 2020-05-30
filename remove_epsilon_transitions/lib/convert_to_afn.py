from lib.automato import *


def remove_epsilon_transition(automato):
    afn = Automato()
    fecho_q = close(automato)
    new_f = create_f_aux(fecho_q, automato)
    new_tr_table = create_extend_transition(automato,fecho_q)
    create_afn(new_tr_table,afn,new_f)
    return afn

def create_afn(n_transition,afn,new_f):
    is_final = False
    for transition in n_transition:
        if(transition.get_origin() in new_f):
            is_final = True
        if(not afn.get_state_by_name(transition.get_origin().get_name())):
            temp_state = afn.create_state(name=transition.get_origin().get_name(),is_final=is_final)
        temp_state.set_transition(destiny=transition.get_destiny(),symbol=transition.get_symbol())

def close(automato):
    close_q = {}
    for state in automato.get_states_list():
        close_q[state] = [state]
        t_epsilon = state.get_transitions_list_by_symbol('{}')
        for transition in t_epsilon:
            while (transition):
                close_q[state].append(transition.get_destiny())
                transition = transition.get_destiny().get_transition('{}')
    return close_q

def create_f_aux(close_q, automato):
    f_aux = []
    for key in close_q.keys():
        if (set(close_q[key]).intersection(set(automato.get_final_state()))):
            f_aux = set(f_aux).union(set(close_q[key]))
    return f_aux

def create_extend_transition(automato,close_q):
    n_transitions = []
    for state in automato.get_states_list():
        for symbol in automato.get_input_symbols():
            if symbol!='{}':
                aux = []
                for close_state in close_q[state]:
                    if(close_state.get_transition(symbol=symbol)):
                        aux = set(aux).union(close_q[close_state.get_transition(symbol=symbol).get_destiny()])
                for x in list(aux):
                    tr = Transition(origin=state, destiny=x, symbol=symbol)
                    n_transitions.append(tr)
    return n_transitions