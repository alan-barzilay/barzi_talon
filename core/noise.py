"""
Map noises (like pop) to actions so they can have contextually differing behavior
"""

from talon import Module, actions, cron, noise
import time
mod = Module()

global last_cluck_time
last_cluck_time = 0
@mod.action_class
class Actions:
    def noise_trigger_cluck():
        """
        Estalar a lingua (cluck): dar toggle no wake/sleep do Talon
        """
        actions.speech.toggle()

    def noise_trigger_cluck_duplo():
        """
        Estalar a lingua (cluck): dar toggle no wake/sleep do Talon
        """
        global last_cluck_time
        current_time = time.time()
        last_cluck_time, diff = current_time, current_time - last_cluck_time

        if diff > 1:
            return

        actions.speech.toggle()

    def noise_trigger_assobio():
        """
        assobiar: repetir o último comando executado
        """
        actions.core.repeat_command()

    # def noise_trigger_beijo():
    #     """
    #     beijo: undo
    #     """
