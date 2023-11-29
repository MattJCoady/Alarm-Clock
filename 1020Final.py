from engi1020.arduino.api import *
from datetime import *
from time import sleep, perf_counter

#Create function to let user select alarm time
def selectedTime():
   
    selected_time = datetime.now()
    curr_time = datetime.now()
    
    oled_clear()
    oled_print('The current time is:')
    oled_print(curr_time)
    sleep(3)
    oled_clear()
    oled_print('Please select a time:')
    
    while True:
        
        inp = analog_read(0)
        
        if digital_read(6) == True:
            
            if selected_time > curr_time:
                oled_clear()
                oled_print('Alarm will go off at:')
                oled_print(selected_time)
                global alarmTime
                alarmTime = selected_time
                sleep(3)
                return 'Done'
                
            else:
                print('Please select a valid time')
                continue
        
        if inp >= 512:
            selected_time = selected_time + timedelta(minutes = 15)
            sleep(1)
            
        if inp < 512:
            selected_time = selected_time - timedelta(minutes = 15)
            sleep(1)
        
        oled_clear()
        oled_print(selected_time)

#Create menu to let user change aspects of the alarm
def alarmSettings():
    
    while True:
        menuY = analog_read(0)
        menuClose = analog_read(6)
        oled_clear()
        oled_print('Change Alarm Time')
        oled_print('Turn off alarm')
        
        if menuClose <= 50:
            break
        
        if menuY >= 700:
            oled_clear()
            oled_print('->Change Alarm Time')
            oled_print('Turn off alarm')
            
        if menuY >= 700 and digital_read(6) == True:     
            while True:
                selectedTime()
                
                if selectedTime() == 'Done':
                    sleep(3)
                    break
                    
        if menuY <= 300:            
            oled_clear()
            oled_print('Change Alarm Time')
            oled_print('->Turn off Alarm')
            
        if menuY <= 300 and digital_read(6) == True:    
            
            while True:
                oled_clear()
                oled_print('Hold button to')
                oled_print('turn off alarm')
                sleep(3)
                
                if digital_read(6) == True:
                    global alarmTime
                    alarmTime = None
                    oled_clear()
                    oled_print('Your alarm has')
                    oled_print('been shut off')
                    sleep(3)
                    break
                
                else:
                    oled_clear()
                    oled_print('Your alarm has not')
                    oled_print('been shut off')
                    sleep(3)
                    break
    
    return 'Done'


def triggerAlarm():
    
    oled_clear()
    oled_print('Time to Wake Up')
    oled_print('Hold Button to')
    oled_print('Turn Off')
    original_time = int(perf_counter())
    print(original_time)
    
    while True:
        
        off_switch = digital_read(6)
        current_time = datetime.now()
        
        if off_switch == True:
            
            digital_write(4,False)
            buzzer_stop(5)
            wake_time = int(perf_counter())
            break
        
        if off_switch == False:
            
            digital_write(4, True)
            buzzer_frequency(5, 250)
            sleep(1)
            buzzer_stop(5)
            sleep(1)
            
            
            
    sleep_time = (wake_time-original_time)
    
    if sleep_time <= 60:
        
        oled_clear()
        oled_print('You slept in for')
        oled_print(int(sleep_time))
        oled_print('seconds')
    
    elif 60 < sleep_time <= 3600:
        
        ()
        oled_print('You slept in for')
        oled_print((sleep_time)/60)
        oled_print('minutes')
    
    elif 3600 < sleep_time:
        
        oled_clear()
        oled_print('You slept in for')
        oled_print((sleep_time)/3600)
        oled_print('hours')
    
    sleep(4)
    oled_clear()
    oled_print('Current Time')
    oled_print(current_time())
############################################################################################################################################    



#Create main menu

    
alarmTime = None
    
while True:
    
    menuInpY = analog_read(0)
    currentTime = datetime.now() 
    
    if alarmTime is not None and currentTime >= alarmTime:
        triggerAlarm()
        alarmTime = None
    
    if menuInpY >= 700:
        oled_clear()
        oled_print('->Alarm Time')
        oled_print('Alarm Settings')
        
    if menuInpY >= 700 and digital_read(6) == True:
        oled_clear()
            
        if alarmTime == None:
            oled_clear()
            oled_print('No alarm set')
            oled_print('Press button to')
            oled_print('return to menu')
            
            while True:
                
                if digital_read(6) == True:
                    break
                
            continue
        
        else:
            oled_clear()
            oled_print(alarmTime)
            oled_print('Press button to')
            oled_print('return to menu')
            
            while True:
                
                if digital_read(6) == True:
                    break
            
            continue
    
    if menuInpY < 300:
        oled_clear()
        oled_print('Alarm Time')
        oled_print('->Alarm Settings')
                
    if menuInpY <= 300 and digital_read(6) == True:
        
        while True:
            alarmSettings()
            
            if alarmSettings() == 'Done':
                break
    
        continue