import pyb 

class EncoderReader:

    def __init__(self, pin1:str, pin2:str, timer:int, ch1:int, ch2:int):
        # Pin, timer, and channel configuration
        self.pin1 = pyb.Pin(pin1, pyb.Pin.OUT_PP)
        self.pin2 = pyb.Pin(pin2, pyb.Pin.OUT_PP)
        self.timer = pyb.Timer(timer, prescaler=0, period=0xFFFF)
        self.ch1 = self.timer.channel(ch1, pyb.Timer.ENC_AB, pin=pin1)
        self.ch2 = self.timer.channel(ch2, pyb.Timer.ENC_AB, pin=pin2)

        # Initialize encoder position to zero
        self.position = 0
        # Variable for previous count value
        self.prev_cnt = 0

    def zero(self):
        self.position = 0
    
    def read(self):
        # Calculate difference in position
        current_cnt = self.timer.counter()
        diff = current_cnt - self.prev_cnt 

        # Handle overflow and underflow 
        if diff < -(65536/2):       # Overflow adjustment
            diff += 65536
        elif diff > (65536/2):      # Underflow adjustment
            diff -= 65536

        # Set previous count value to current count value
        self.prev_cnt = current_cnt

        # Add distance to position measurement
        self.position += diff

        return self.position
