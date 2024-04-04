import subprocess
import time

def set_pwm_duty_cycle(duty_cycle):
    """
    Set the PWM duty cycle by writing to the /sys/class/pwm path.

    Parameters:
    - duty_cycle: The duty cycle to set, in nanoseconds.
    """
    try:
        with open("/sys/class/pwm/pwmchip0/pwm0/duty_cycle", "w") as pwm_file:
            pwm_file.write(str(duty_cycle))
    except IOError as e:
        print(f"Error writing to PWM duty cycle: {e}")

def main():
    for i in range(10):
        print(f"Iteration {i+1}: Setting duty cycle to 1600000ns for 30s")
        set_pwm_duty_cycle(1600000)
        time.sleep(30)  # Wait for 30 seconds

        print(f"Iteration {i+1}: Setting duty cycle to 1500000ns")
        set_pwm_duty_cycle(1500000)
        time.sleep(30)  # Short delay before next iteration, adjust as needed

if __name__ == "__main__":
    main()

