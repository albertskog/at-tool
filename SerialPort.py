import serial
import serial.tools.list_ports

class SerialPort():

    port = serial.Serial(timeout=1)

    def __init__(self, parent):
        self.master = parent

    def get_ports(self):      
        port_list = []
        for port in serial.tools.list_ports.comports():
            port_list.append(port.device)
        return port_list

    def connect_port(self, port_name, baudrate):
        if self.port.is_open:
            self.port.close()

        self.port.port = port_name
        self.port.baudrate = baudrate
        try:
            self.port.open()
            self.master.after(100, self.get_data)
            self.master.serial_terminal.add_line("Port connected", "info")
        except serial.SerialException:
            self.master.serial_terminal.add_line("Port disconnected", "error")
    
    def disconnect_port(self):
        if self.port.is_open:
            self.port.close()
            self.master.serial_terminal.add_line("Port disconnected", "info")

    def get_data(self):
        try:
            if self.port.is_open:
                if self.port.in_waiting > 0:
                    try:
                        data = self.port.readline().decode().strip()
                        if data != "":
                            self.master.serial_terminal.add_line(data, "response")
                    except UnicodeDecodeError:
                        pass
                self.master.serial_terminal.after(10, self.get_data)
            else:
                self.master.serial_terminal.add_line("Port is disconnected", "error")

        except OSError:
            self.master.serial_terminal.add_line("Port disconnected", "error")
            return

    def send_data(self, data):
        try:
            port_is_open = self.port.is_open
        except OSError:
            self.master.serial_terminal.add_line("Port disconnected", "error")
            return
        if port_is_open:
            newline = "\r\n"
            try:
                self.port.write((data+newline).encode())
                self.master.serial_terminal.add_line(data, "command")
            except serial.SerialException as error:
                print(error)
                self.master.serial_terminal.add_line("Port disconnected", "error")
        else:
            self.master.serial_terminal.add_line("Port is not connected", "error")
