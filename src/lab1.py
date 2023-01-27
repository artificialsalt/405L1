import motor_driver
import encoder_reader

def main():
    # Configure motor driver for motor M1
    M1 = motor_driver.MotorDriver('A10', 'B4', 'B5', 3, 1, 2)
    # Configure encoder for motor M1
    E1 = encoder_reader.EncoderReader('C6', 'C7', 8, 1, 2)



if __name__ == "__main__":
    main()