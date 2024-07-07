"""
Map noises (like pop) to actions so they can have contextually differing behavior
"""

from talon import Module, actions, cron, noise
import time
mod = Module()

global last_cluck_time
last_cluck_time = 0
def excedeu_tempo(max_diff:int = 1):
    '''
    Essa funcao valida se o intervalo de tempo entre uma acao e outra eh curto o suficiente pra ser considerado valido.
    Retorna True se tiver excedido o tempo
    '''
    global last_cluck_time
    current_time = time.time()
    last_cluck_time, diff = current_time, current_time - last_cluck_time

    return diff > max_diff

def mic_valido():
    '''
    Essa funcao valida se o microfone sendo usado eh um mic bom o suficiente para usar o parrot (aka, nao o vanilla).
    Retorna False se for um mic ruim
    '''
    return actions.sound.active_microphone() == 'HyperX QuadCast S Analog Stereo'


@mod.action_class
class Actions:
    def noise_trigger_cluck_duplo():
        """
        Estalar a lingua (cluck): dar toggle no wake/sleep do Talon
        """
        if not mic_valido() or excedeu_tempo():
            return

        actions.speech.toggle()

    def noise_trigger_assobio():
        """
        assobiar: repetir o último comando executado
        """
        actions.core.repeat_command()

