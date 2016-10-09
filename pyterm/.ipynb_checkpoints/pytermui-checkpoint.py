import time

from kfunctions import functions as f
        
def main():
    ui=''
    kf = f()
    while ui != 'exit':
        ui = input("|>")
        kf.callFunction(ui)
        """
        if input1 == 'exit':
            ser.close()
            exit()
        else:
            ser.write(bytearray(input1 + '\r\n','ascii'))
            out = bytearray('','ascii')
            #time.sleep(1)
            while ser.inWaiting() > 0:
                out += ser.read(1)

            if out != bytearray('','ascii'):
                print(">>" + out.decode('ascii'))
        """
if __name__=='__main__':
    main()
