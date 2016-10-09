import time
import serial

com ='/dev/ttyACM1'
br = 9600

ser = serial.Serial(
    port=com,
    baudrate=br,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
print("|>Connected to ", com, " at baudrate ",br, "!")
def main():
    ui=''
    while ui != 'exit':
        ui = input("|>")
        if ui == 'exit':
            ser.close()
            exit()
        else:
            ser.write(bytearray(ui + '\r\n','ascii'))
            out = bytearray('','ascii')
            time.sleep(0.1)
            while ser.inWaiting() > 0:
                out += ser.read(1)

            if out != bytearray('','ascii'):
                print("|>" + out.decode('ascii'))
        
if __name__=='__main__':
    main()
