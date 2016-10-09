import serial

#Connection list
cl =[]

# Argument parser
def parsearg(ui):
    args=ui.replace('(',' ').replace(')',' ').replace(',',' ').strip().split()
    return args

# configure the serial connections (the parameters differs on the device you are connecting to)
class as_ser:
    def __init__(self,com,br):
        self.ser = serial.Serial(
            port=com,
            baudrate=br,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS
        )
        
    def status(self):
        return self.ser.isOpen()

    def close(self):
        self.ser.close()
    
class functions:
    global cl
    def __init__(self):
        pass
    
    def connect(self,args):
        if args=='serial':
            com = input('What is the com port? ')
            br= input('What is the baud rate? ')
            try:
                cl.append(as_ser(com,br))
                print("|> Connected to ", com, " at baudrate ",br, "!")
            except:
                print("Something wrong with Serial connection")
        elif args=='tcp':
            pass
        
    def log(self):
        pass
                  
                  
    def macro(self):
        print("Run Macro")
    
    def exit(self):
        pass
    
    def helps(self):
        print(dir(self))
        #print(self.__name__)
