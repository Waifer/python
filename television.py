class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False  
        self.__muted = False  
        self.__volume = self.MIN_VOLUME  
        self.__channel = self.MIN_CHANNEL  

    def power(self):
        """Turn the TV on or off."""
        self.__status = not self.__status

    def mute(self):
        """Mute or unmute the TV."""
        if self.__status: 
            self.__muted = not self.__muted

    def channel_up(self):
        """Increase the channel. Wrap around to MIN_CHANNEL if at MAX_CHANNEL."""
        if self.__status:  
            self.__channel = self.MIN_CHANNEL if self.__channel == self.MAX_CHANNEL else self.__channel + 1

    def channel_down(self):
        """Decrease the channel. Wrap around to MAX_CHANNEL if at MIN_CHANNEL."""
        if self.__status:  
            self.__channel = self.MAX_CHANNEL if self.__channel == self.MIN_CHANNEL else self.__channel - 1

    def volume_up(self):
        """Increase the volume. Unmute if muted. Do nothing if at MAX_VOLUME."""
        if self.__status:  
            if self.__muted:
                self.__muted = False  
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """Decrease the volume. Unmute if muted. Do nothing if at MIN_VOLUME."""
        if self.__status:  
            if self.__muted:
                self.__muted = False  
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """Return the TV's status as a string."""
        power_status = self.__status  
        volume = "Muted" if self.__muted else self.__volume
        return f"Power = {power_status}, Channel = {self.__channel}, Volume = {volume}"

