from controller import Robot
## robot berjalan pada line
def go():
    rightmotor.setVelocity(5)
    leftmotor.setVelocity(5)
def left():
    rightmotor.setVelocity(4)
    leftmotor.setVelocity(-4)
def right():
    rightmotor.setVelocity(-4)
    leftmotor.setVelocity(4)
def stop():
    rightmotor.setVelocity(0)
    leftmotor.setVelocity(0)

#robot mendeteksi line     
def kondisi_1():
    if sensor < 1200:
        go()
    elif line_kiri < 450:
        stop()
        left()
    elif sensor_kanan > 1300 and sensor_kiri < 1300:
        go ()
        stop()
        left()
    elif sensor_kanan < 1300 and sensor_kiri > 1300:
        go ()
        stop ()
        right()
       
def kondisi_2():
    if sensor_kanan > 1300 and sensor_kiri < 1300:
        go()
        stop()
        left()
    elif sensor_kanan < 1300 and sensor_kiri > 1300:
        go()
        stop()
        right()
    elif line_kanan < 508:
        go()
        stop()
        right()
    elif ke_depan > 300:
        go()
    elif ke_depan < 300:
        stop ()
    else :
        go()
       
        
robot = Robot()
timestep = int(robot.getBasicTimeStep())
maxspeed = 8
leftmotor = robot.getDevice('motor_1')
rightmotor = robot.getDevice('motor_2')
leftmotor.setPosition(float('inf'))
rightmotor.setPosition(float('inf'))

irl2 = robot.getDevice('IRL2')
irl1 = robot.getDevice('IRL1')
ircl = robot.getDevice('IRCL')
ircr = robot.getDevice('IRCR')
irr1 = robot.getDevice('IRR1')
irr2 = robot.getDevice('IRR2')

irl2.enable(timestep)
irl1.enable(timestep)
ircl.enable(timestep)
ircr.enable(timestep)
irr1.enable(timestep)
irr2.enable(timestep)

kekanan = robot.getDevice('ds_right')
kekiri = robot.getDevice('ds_left')
kedepan = robot.getDevice('ds_front')
kekanan.enable(timestep)
kekiri.enable(timestep)
kedepan.enable(timestep)

while robot.step(timestep) != -1:  
    rightmotor.setVelocity(8)
    leftmotor.setVelocity(8)
    
    irl2_val = irl2.getValue()
    irl1_val = irl1.getValue()
    ircl_val = ircl.getValue()
    ircr_val = ircr.getValue()
    irr1_val = irr1.getValue()
    irr2_val = irr2.getValue()
    ke_kiri = kekiri.getValue()
    ke_kanan = kekanan.getValue()
    ke_depan = kedepan.getValue()

    line_kanan = irr1_val + irr2_val
    line_kiri = irl1_val + irl2_val
    sensor_kanan = ircr_val + irr1_val + irr2_val
    sensor_kiri = ircl_val + irl1_val + irl2_val
    sensor_tengah = ircr_val + ircl_val
    sensor = sensor_kanan + sensor_kiri    
   
    if maxspeed == 8:
       kondisi_1()
    elif (sensor > 3600 and sensor_kanan < 1000) or (sensor > 3600 and ke_kiri < 1000):
        go()
        
    if sensor < 3000 and ke_kiri < 1000:
       maxspeed = 4
    elif maxspeed == 4:
       kondisi_2()
       
    if ke_kanan < 910: 
       maxspeed = 2
    
    print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(line_kanan, line_kiri, sensor_kanan, sensor_kiri, sensor_tengah, sensor))
