import serial
ser = serial.Serial('/dev/tty.usbmodemfa131', 19200)
print ser.readline() # to print the initial connection confirmation message

while True: # keeping reading data from Arduino
    line = ser.readline() # reading serial output from Arduino line by line
    data = str.strip(line) # strip newline from the end

    if data == "start": # z button pressed down for first time
        gesture = []
        print "starting to collect data now"

    elif data == "stop": # z button had been pressed down previously, now just let go of it to end collection of data
        print "vectors collected: ", gesture # list of lists of xyz coordinates

    else:
        print "collecting data..."
        vector_list = str.split((data), ",") # break apart into a 3-item [x, y, z] list

        for i in range(len(vector_list)):
            vector_list[i] = int(vector_list[i]) # convert contents of vector_list into numbers

        gesture.append(vector_list)