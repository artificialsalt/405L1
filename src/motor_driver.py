import pyb

class MotorDriver:

    def __init__(self, en_pin:str, in1pin:str, in2pin:str, timer:int, ch1:int, ch2:int):
        # Pin and timer configurations
        self.en_pin = pyb.Pin(en_pin, pyb.Pin.OUT_PP) 
        self.in1pin = pyb.Pin(in1pin, pyb.Pin.OUT_PP) 
        self.in2pin = pyb.Pin(in2pin, pyb.sPin.OUT_PP)
        self.timer = pyb.Timer(timer, freq=20000)

        # Disables motor pin for safety
        self.en_pin.low()

        # Configures pins and their appropriate timer channels to PWM mode
        self.pwm1 = self.timer.channel(ch1, pyb.Timer.PWM, pin=self.in1pin)
        self.pwm2 = self.timer.channel(ch2, pyb.Timer.PWM, pin=self.in2pin)

    def enable_motor(self):
        self.en_pin.high()

    def disable_motor(self):
        self.en_pin.low()

    def set_duty_cycle (self, level:int):
        if level >= 0:
            if level > 100:
                level = 100
            self.pwm1.pulse_width_percent(level)
            self.pwm2.pulse_width_percent(0)
        else:
            if level < -100:
                level = -100
            self.pwm1.pulse_width_percent(0)
            self.pwm2.pulse_width_percent(-(level))
