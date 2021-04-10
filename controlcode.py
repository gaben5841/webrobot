from Raspi_MotorHAT import Raspi_MotorHAT
import keyboard
mh = Raspi_MotorHAT(addr=0x6f)
motor = mh.getMotor(1)
motor.run(Raspi_MotorHAT.FORWARD)
#loopend = True

while True:
    
    if keyboard.is_pressed('w'):
        motor.setSpeed(100)    
    else:
        motor.setSpeed(0)
    
    if keyboard.is_pressed('q'):
        break
    
