import serial
import fnmatch
from Tkinter import *


def auto_detect_serial_unix(preferred_list=['*']):
    '''try to auto-detect serial ports on linux'''
    import glob
    glist = glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*')
    ret = []

    # try preferred ones first
    for d in glist:
        for preferred in preferred_list:
            if fnmatch.fnmatch(d, preferred):
                # ret.append(SerialPort(d))
                ret.append(d)
    if len(ret) > 0:
        return ret
    # now the rest
    for d in glist:
        # ret.append(SerialPort(d))
        ret.append(d)
    if len(ret) == 0:
        ret.append("")
    return ret


class SerialPortSelect(LabelFrame):
    def __init__(self, parent=None, **kw):
        LabelFrame.__init__(self, parent, text="Serial Port", padx=5, pady=5)
        self.config(width=300)

        self.serialPort = StringVar(self)
        self.serialBaud = StringVar(self)
        self.serialPortList = auto_detect_serial_unix()
        self.serialBaudList = ["2400", "4800", "9600", "19200", "38400", "57600", "115200"]
        self.state = "disconnected"

        # if self.serialPortList == []:
        #	self.serialPortList = [""]

        # self.frmSerial = LabelFrame(self,text="Serial Port",padx=5,pady=5)
        # self.frmSerial.config(width=300)
        self.omPorts = OptionMenu(self, self.serialPort, *self.serialPortList)
        self.omPorts.config(width=15)
        self.omBaud = OptionMenu(self, self.serialBaud, *self.serialBaudList)
        self.omBaud.config(width=5)
        self.btnConnect = Button(self, text="Connect", command=self.connectSerial)
        self.omPorts.grid(column=0, row=0)
        self.omBaud.grid(column=1, row=0)
        self.btnConnect.grid(column=2, row=0)

    # self.frmSerial.grid()

    def connectSerial(self):
        if self.state == "disconnected":
            print
            "Connecting Serial Port " + self.serialPort.get()
            self.port = serial.Serial(self.serialPort.get(), int(self.serialBaud.get()), timeout=1.0)
            self.omPorts.configure(state="disabled")
            self.omBaud.configure(state="disabled")
            self.btnConnect.config(text="Disconnect")
            self.state = "connected"
            self.port.write("Hello")
        else:
            print
            "Disconnecting Serial Port " + self.serialPort.get()
            self.state = "disconnected"
            self.port.close()
            self.omPorts.configure(state="normal")
            self.omBaud.configure(state="normal")
            self.btnConnect.config(text="Connect")


def main():
    # root = Tk()
    # root.title("Serial Port Picker")

    app = SerialPortSelect()
    app.grid()
    app.mainloop()
    return 0


if __name__ == '__main__':
    main()
