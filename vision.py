import cv2                                              #Import CV2;                                            For opening, editing and displaying images and video
import numpy as np                                      #Import numpy, shortend as "np";                        For editing images/video map
from datetime import datetime                           #Import datetime function from datetime library;        For checking actual time and calculation framerate
import time                                             #Import time library;                                   For wait (time.sleep) function on connecting to the camera





#======================================= Camera startup settings ================================================#

#camera variable, standard resolution of the camera
width = 1280
height = 720

#Scaling value, scaling image down improves performance. Displayed images/video are also scaled to this value
scale = 0.5

#Window settings, create windows and default location to display on screen
cv2.namedWindow("input",cv2.cv.CV_WINDOW_AUTOSIZE)
cv2.cv.MoveWindow("input",0,00)
cv2.namedWindow("hsv",cv2.cv.CV_WINDOW_AUTOSIZE)
cv2.cv.MoveWindow("hsv",0,int(height*scale))
cv2.namedWindow("output",cv2.cv.CV_WINDOW_AUTOSIZE)
cv2.cv.MoveWindow("output",int(width*scale),int(height*scale))

#Camera settings, input from webcam
webcam = cv2.VideoCapture(0)

#Set input to fixed camera settings (width & height)
webcam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,width)
webcam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,height)


#=================================== PID parameters ============================================#

#Create trackbars
def nothing(x): # DUMMY FUNCTION
    pass

def clearSetpoint(x):
    g_iterm = 0
    
cv2.createTrackbar('P','hsv',15,255,nothing) # KP
cv2.createTrackbar('I','hsv',100,255,nothing) # KI
cv2.createTrackbar('D','hsv',0,255,nothing) # KD
cv2.createTrackbar('S','hsv',160,255,clearSetpoint) # SETPOINT

g_iterm = 0




#=================================== Washfront detection parameters ============================================#

#Minimal setpoint for detecting the washfront (1-255); Normal value = 25-50, 
WF_setpoint = 30

#Detection mode; 1 = Saturation (used for colorful products), 2 = Value (used for white products);    0 = Hue (not useful), and all other values will result in an error.
WF_detection_mode = 1

#
WF_measurements_y = 100
WF_measurements_x = 10

#
WF_min_width = 5
WF_stepsize  = 2
WF_max_width = 80


# Box positions
hand_x_pos = 230
hand_y_pos = 18
hand_width = 64
hand_height = 324

ball_x_pos = hand_x_pos + 50 + hand_width
ball_y_pos = 18
ball_width = 32
ball_height = 324




#======================================= Other Initial Values =================================================#

#Variable to keep track of the actual time of last cyclus; Used for calculating FPS
previoustime = 0

#The ball distance
g_ball_distance = 0
g_hand_distance = 0
g_running = True

#==============================================================================================================#
#========================================== Start Functions ===================================================#
#==============================================================================================================#

def getresolution(img):
    try:
        height, width, channels = img.shape     #Function to get properties of the image, value "channels" is not used
        return height, width
    except:
        print "Image not defined, could not get resolution"

#==============================================================================================================#

def getfps(previoustime):                       #Calculate FPS from time between frames
    dt = datetime.now()
    time = dt.microsecond - previoustime
    if time > 0:                                #Normal fps calculation
        fps = int(1/(float(time)/1000000))
    else:                                       #Calculation when microseconds restart (1.000.000 microseconds -> 1 sec)                     
        previoustime = previoustime - 1000000
        time = dt.microsecond - previoustime
        fps = int(1/(float(time)/1000000))
    return fps, dt.microsecond

#==============================================================================================================#       

def scaleimages(scale, img1):                   
    try:
        img1 = cv2.resize(img1,None,fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
        return img1
    except:
        print "Image1 not defined, could not scale"

#==============================================================================================================#

def getvalues(img, xPos, yPos, width = 32, height = 324):
    
    line_x1 = xPos
    line_x2 = xPos + width
    
    x_step = (line_x2-line_x1)/WF_measurements_x
    
    line_y1 = yPos
    line_y2 = yPos + height

    y = line_y1
    pos_list = []
    sat_list = []
    
    while y <= line_y2:
        av_sat = 0
        
        for x in range(0, WF_measurements_x):
            hsv_val = img[ y, line_x1 + x*x_step]
            av_sat = av_sat + hsv_val[WF_detection_mode]      
            
        av_sat = av_sat / WF_measurements_x
        pos_list.append(y)                              #list of positions of the saturation values
        sat_list.append(av_sat)                         #list of saturation values
        
        y = y +(line_y2-line_y1) / WF_measurements_y    #Amount of values on y-axis

        
    cv2.rectangle(img,(line_x1,line_y1),(line_x2,line_y2),(255,255,255),3) #drawing the detection zone as a white retangle on the screen 
    return img, pos_list, sat_list

#==============================================================================================================#

def calculate_wasfront(sat_list):
    check_wasfront    = True                    #Function "calculate_wasfront" will keep checking for a wasfront while "check_wasfront" = "True". 
    wasfront_detected = False                   #
    factor            = WF_min_width            #Factor for calculation differences. Defined at "minimum width"
    list_gem          = []                      #List for avarages, once defined per function "calculate_wasfront"
    
    
    for a in range (len(sat_list)):
        if a > 1:
            try:
                list_gem.append( (sat_list[a-2]+sat_list[a-1]+sat_list[a]+sat_list[a+1]+sat_list[a+2])/5)
            except:                         #
                list_gem.append(None)       #Fault value
        else:                               #
            list_gem.append(None)           #Fault value

    while check_wasfront == True:           #Keep looking while "check_wasfront" = "True"
        list_dif = []                       #Create empty list for differences between averages, up to 30 times per function "calculate_wasfront"

        for b in range (len(list_gem)):
            if (b >= factor):
                if (list_gem[b] != None) and (list_gem[b-factor] != None):
                    list_dif.append( list_gem[b] - list_gem[b - factor])    # List of differences
                else:
                    list_dif.append(None)   #Fault value                    
            else:
                list_dif.append(None)       #Fault value

        if (max(list_dif) >= WF_setpoint):  #Wasfront detected
            check_wasfront = False          
            wasfront_detected = True        
        else:
            factor = factor + WF_stepsize   #Increasing "factor" value by "stepsize"; Also possible to double the factor for increased performance (factor = factor *2)

        if factor > WF_max_width:           #Wasfront not detected after x times increasing "factor" value (set with washfront_max_widht)
            check_wasfront = False          
            wasfront_detected = False       

    return wasfront_detected, list_dif, factor  

#==============================================================================================================#


def visualisation(img, img_can, pos_list, sat_list, xPos, yPos, width, height):
    
    line_x = xPos
    line_y1 = yPos
    line_y2 = yPos + width

    lastval = 50

    wasfront_detected, list_dif, factor = calculate_wasfront(sat_list)

    if wasfront_detected == True:
        cv2.rectangle(img,( line_x-50, pos_list[list_dif.index(max(list_dif))-factor] ),(line_x, pos_list[ list_dif.index(max(list_dif))] ),(0,255,0),3)
        cv2.rectangle(img_can,( line_x-50, pos_list[list_dif.index(max(list_dif))-factor] ),(line_x, pos_list[ list_dif.index(max(list_dif))] ),(255,255,255),3)

        position = 0.9*height - ( pos_list[list_dif.index(max(list_dif))-factor] - (0.05*height) )
        scalefactor = 285 / (0.9*height)
    
        mm_bot = 0
        mm_top = 285
        mm_washfront = int(position * scalefactor)
    
        cv2.line(img_can,(line_x-60,int(height*0.95)),(line_x-60, int(pos_list[list_dif.index(max(list_dif))-factor])),(0,255,0),1)
        cv2.putText( img_can, str(mm_washfront), (line_x-100, int(pos_list[list_dif.index(max(list_dif))-factor])), 5, 1, (255,255,255) )

    else:
        mm_washfront = 999

    mm_bot = 0
    mm_top = 285

    cv2.line(img_can,(line_x-50,int(height*0.05)),(line_x, int(height*0.05)),(160,160,160),2)
    cv2.putText( img_can, str(mm_top), (line_x-75,int(height*0.05)), 5, 0.5, (160,160,160) )

    cv2.line(img_can,(line_x-50,int(height*0.95)),(line_x, int(height*0.95)),(160,160,160),2)
    cv2.putText( img_can, str(mm_bot), (line_x-75,int(height*0.95)), 5, 0.5, (160,160,160) )

    '''
    for x in range (len(pos_list)):     
        cv2.putText( img, str(sat_list[x]), (line_x+10, pos_list[x]), 5, 0.5, (255,255,255) )
        cv2.line(img,(line_x+50,pos_list[x]),(line_x+50+sat_list[x],pos_list[x]),(0,255,0),1)
    '''
    if (mm_washfront < 0):
        mm_washfront = 0
    
    return img, img_can, mm_washfront
        







#======================================== SERIAL THINGS ======================================================#
import serial
import threading
import time
ser_com = serial.Serial('COM8')  # open serial port
print(ser_com.name)         # check which port was really used


def int_to_byte(var):
    return bytes(bytearray([var]))


def write_to_port(ser):
    global g_iterm
    old_time = time.time()
    delay = 0.1
    while g_running:
        if time.time() - old_time > delay:  # Every 10 sec
            old_time = time.time()
            ser.write(b'M')     # Set edit mode to Motor on arduino
            setpoint = cv2.getTrackbarPos('S','hsv') if cv2.getTrackbarPos('S','hsv') != 0 else g_hand_distance;
            kp = float(cv2.getTrackbarPos('P', 'hsv')) / 100;
            ki = float(cv2.getTrackbarPos('I', 'hsv')) / 100
            error = (g_ball_distance - setpoint)

            #print "Error: " + str(error)

            STABLE_AT = 168
            # DEfault value - p + i + d
            value = STABLE_AT - int(kp * error) + int(ki * g_iterm )

            if (value > 255):
                value = 255
            elif  (value < STABLE_AT - 30):
                value = STABLE_AT - 30

            
            '''
            if (g_ball_distance > setpoint):
                value = 160
            elif (g_ball_distance < setpoint):
                value = 200
            else:
                value = 255 - g_ball_distance
            '''

            # Out of screen
            '''
            if (g_ball_distance > 255):
                value = 150
            '''

            # Minimal fan speed
            '''
            if (value < 140):
                value = 140
            '''

            if (g_ball_distance == 999):
                print "DOEI BALL"
                value = STABLE_AT - 5
            else:
                g_iterm *= delay
            
            print "Ball hight: " + str(g_ball_distance)
            #print "Fan speed: " + str(value)
            ser.write(int_to_byte(value))     # Set motor speed

            ser.write(b'S')
            print "Set point: " + str(setpoint) + "/n"
            ser.write(int_to_byte(g_ball_distance if g_ball_distance < 256 else 255))


def read_from_port(ser):
    while g_running:
        print "Result: " + ser.readline()


read_thread = threading.Thread(target = read_from_port, args = (ser_com,))
write_thread = threading.Thread(target = write_to_port, args = (ser_com,))

read_thread.start()
write_thread.start()


#======================================== Main loop ======================================================#
retval = False

while(retval == False):
    print "cannot connect to webcam"
    retval,input_image = webcam.read()
    time.sleep(1)

while(True):   #Main program
    retval,input_image = webcam.read()                                      #function to read camera input, "retval" = True/False, "input_image" = recorded image

    img_canvas = scaleimages(scale, input_image)

    scaled_image = scaleimages(scale, input_image)                          #Function to scale the image
    img_hsv = cv2.cvtColor(img_canvas, cv2.COLOR_BGR2HSV)                   #Creaty copy of the image in HSV color spectrum

    height, width = getresolution(img_canvas)                               #Function to get the resolution of the image



    img_vis, hand_pos_list, hand_sat_list = getvalues(img_hsv, hand_x_pos, hand_y_pos, hand_width, hand_height)           #Function to detect and calculate values
    img_vis, ball_pos_list, ball_sat_list = getvalues(img_hsv, ball_x_pos, ball_y_pos, ball_width, ball_height)           #Function to detect and calculate values
    img_vis, img_canvas, g_hand_distance = visualisation(img_hsv, img_canvas, hand_pos_list, hand_sat_list, hand_x_pos, hand_y_pos, hand_width, hand_height)     #Function to print visualisize values on image
    img_vis, img_canvas, g_ball_distance = visualisation(img_hsv, img_canvas, ball_pos_list, ball_sat_list, ball_x_pos, ball_y_pos, ball_width, ball_height)     #Function to print visualisize values on image

    fps, currenttime = getfps(previoustime)
    previoustime = currenttime
    cv2.putText(scaled_image,"fps = "+str(fps), (10,25), 5, 1, (255,255,255))
            
    cv2.imshow("input", scaled_image)   #Display scaled input image
    cv2.imshow("hsv", img_vis)          #Display HSV image with visualizations
    cv2.imshow("output", img_canvas)    #Diplay 
    
    if(cv2.waitKey(20) == 27):          #Escape button pressed
        break                           #Quit program

    
cv2.destroyAllWindows()

g_running = False

# Closing serial breaks code d;(
# ser_com.close()
