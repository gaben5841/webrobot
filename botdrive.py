from Raspi_MotorHAT import Raspi_MotorHAT
import keyboard

mh = Raspi_MotorHAT(addr=0x6f)
lmotor = mh.getMotor(1)
rmotor = mh.getMotor(2)
# lmotor.run(Raspi_MotorHAT.FORWARD)
# loopend = True

def driveBot(buttonInput):

    if buttonInput == "w":
        lmotor.run(Raspi_MotorHAT.FORWARD)
        rmotor.run(Raspi_MotorHAT.FORWARD)
        lmotor.setSpeed(100)
        rmotor.setSpeed(100)
    elif buttonInput == "s":
        lmotor.run(Raspi_MotorHAT.BACKWARD)
        rmotor.run(Raspi_MotorHAT.BACKWARD)
        lmotor.setSpeed(100)
        rmotor.setSpeed(100)
    elif buttonInput == "a":
        lmotor.run(Raspi_MotorHAT.FORWARD)
        rmotor.run(Raspi_MotorHAT.BACKWARD)
        lmotor.setSpeed(100)
        rmotor.setSpeed(100)
    elif buttonInput == "d":
        lmotor.run(Raspi_MotorHAT.BACKWARD)
        rmotor.run(Raspi_MotorHAT.FORWARD)
        lmotor.setSpeed(100)
        rmotor.setSpeed(100)
    else:
        lmotor.setSpeed(0)
        rmotor.setSpeed(0)

