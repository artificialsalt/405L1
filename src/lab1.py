'''!
@file lab1.py
This file contains code to run a motor using PWM and measure its motion using an encoder.

@author Chayton Ritter, Richard Kwan, Jackie Chen
@date 24-Jan-2023
'''

# Import modules
import motor_driver
import encoder_reader
import time

def main():
    '''!
    Example test code that runs a motor back and forth between two positions
    '''
    # Configure motor driver for motor M1
    M1 = motor_driver.MotorDriver('A10', 'B4', 'B5', 3, 1, 2)
    # Configure encoder for motor M1
    E1 = encoder_reader.EncoderReader('C6', 'C7', 8, 1, 2)
    M1_position = 0

    # Enable the motor
    M1.enable_motor()

    # Drive the motor forward at 100% 
    M1.set_duty_cycle(100)
    while True:
        M1_position = E1.read()
        if M1_position > 100000:
            break
        time.sleep(0.05)             # Sleep 50ms before reading again
    
    # Drive the motor backward at 100%
    M1.set_duty_cycle(-100)
    while True:
        M1_position = E1.read()
        if M1_position < -100000:
            break
        time.sleep(0.05)             # Sleep 50ms before reading again
    
    # Drive the motor back to center at 50% speed
    M1.set_duty_cycle(50)
    while True:
        M1_position = E1.read()
        if M1_position > -2000 and M1_position < 2000:
            break
        time.sleep(0.05)
    
    # Stop and disable motor
    M1.set_duty_cycle(0)
    M1.disable_motor()

if __name__ == "__main__":
    main()