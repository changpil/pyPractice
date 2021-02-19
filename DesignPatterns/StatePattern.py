# Allowing an object to alter behavior
# when its internal state changes so that it appears to change its class

class Phone:
    def __init__(self):
        self.ring_state = SoundState()

    def volumeUp(self):
        self.ring_state = self.ring_state.nextVolumeUp()

    def volumeDown(self):
        self.ring_state = self.ring_state.nextVolumeDown()
    def ring(self):
        self.ring_state.ring()

import abc

class RingState(abc.ABC):
    @abc.abstractmethod
    def ring(self):
        pass
    @abc.abstractmethod
    def nextVolumeUp(self):
        pass
    @abc.abstractmethod
    def nextVolumeDown(self):
        pass

class SoundState(RingState):
    def ring(self):
        print("Phone is ringing")
    def nextVolumeUp(self):
        return self
    def nextVolumeDown(self):
        return VibrateState()

class VibrateState(RingState):
    def ring(self):
        print("Phone is vibrating")
    def nextVolumeUp(self):
        return  SoundState()
    def nextVolumeDown(self):
        return SilentState()

class SilentState(RingState):
    def ring(self):
        print("Phone is silent")
    def nextVolumeUp(self):
        return  VibrateState()
    def nextVolumeDown(self):
        return self

phone = Phone()
phone.ring()
phone.volumeDown()
phone.ring()
phone.volumeDown()
phone.ring()
phone.volumeDown()
phone.ring()
phone.volumeUp()
phone.ring()
phone.volumeUp()
phone.ring()