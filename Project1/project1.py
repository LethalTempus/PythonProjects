from pathlib import Path

class Device:
    """A class that stores specific device's attributes."""
    time_count = 0
    write_list = []
    packet_list_1 = []
    def __init__(self, name):
        self.device_name = name
        self.propagation_info_list = []
        self.alert_cancel_info_list = []
        self.packet_list = []
        self.packet_out = []
        self.communication_list = []

    def store_propagation_info(self, list_of_tuple):
        """store the propagation info for each device"""
        for item in list_of_tuple:
            if item[0] == self.device_name:
                self.propagation_info_list.append(item)


    def store_alert_cancel_info(self, list_of_list):
        """store the alert and cancel info within each device"""
        for item in list_of_list:
            if item[1] == self.device_name:
                self.alert_cancel_info_list.append(item)


    def check_for_event(self):
        """if the time matches the current time, an event is running"""
        if len(self.alert_cancel_info_list) == 0:
            return []
        else:
            """when the device time has not come, it will not go into this that's why we can't test everything"""
            for event in self.alert_cancel_info_list:
                if int(event[-1]) == Device.time_count:
                    if event[0] == "ALERT" or event[0] == "CANCEL":
                        self.packet_list = []
                        self.packet_list.append(Device.time_count)
                        self.packet_list.append(event[0])
                        self.packet_list.append(event[2])
                        self.packet_list.append(self.propagation_info_list[0][0])
                        self.packet_list.append('')
                        self.packet_list.append(0)
                        return self.packet_list


    def check_if_send(self, packet_list):
        """recursive call to calculate all information for one event if no other packer interrupt"""
        try:
            if (packet_list[3] == self.device_name) and (packet_list[0] == Device.time_count):
                if packet_list[1] == "ALERT":
                    text = f"@{packet_list[0]} #{packet_list[3]}: SENT {packet_list[1]} TO #{self.propagation_info_list[0][1]}: {packet_list[2]}"
                elif packet_list[1] == "CANCEL":
                    text = f"@{packet_list[0]} #{packet_list[3]}: SENT {packet_list[1]}LATION TO #{self.propagation_info_list[0][1]}: {packet_list[2]}"
                Device.write_list.append(text)
                connections = self.propagation_info_list[0][1]
                packet_list[0] = Device.time_count + int(self.propagation_info_list[0][2])
                if packet_list[1] == "ALERT":
                    text = f"@{packet_list[0]} #{connections}: RECEIVED {packet_list[1]} FROM #{packet_list[3]}: {packet_list[2]}"
                elif packet_list[1] == "CANCEL":
                    text = f"@{packet_list[0]} #{connections}: RECEIVED {packet_list[1]}LATION FROM #{packet_list[3]}: {packet_list[2]}"
                Device.write_list.append(text)
                packet_list = packet_list
                packet_list[3] = self.propagation_info_list[0][1]
                packet_list[4] = ""
                Device.packet_list_1 = packet_list
        except:
            """when the pass in packet_list is empty"""
            pass


def main() -> None:
    """Runs the simulation program in its entirety."""
    """all relates to the path. I tried to separate it into different functions but there are just too many object"""
    """I've write everything prior testing anything."""
    """I will be writing smaller chunks and organize it along the way"""
     #stores every device object and its info.
    device_storer = []
    input_file_path = _read_input_file_path()
    event_buffer = []
    A_list, B_list, C_list = readfile(input_file_path)
    A_list.sort()#["1","2","3","4"...]
    B_list.sort()#[("1","2","700"),("2","3","500")...]
    C_list.sort()#[["ALERT","1","Trouble","0"]["CANCEL","1","Trouble","2200"]...]
    for item in range(len(A_list)):
        device_storer.append(str(item))
        device_storer[item] = Device(A_list[item])
        device_storer[item].store_propagation_info(B_list)
        device_storer[item].store_alert_cancel_info(C_list)
    while Device.time_count <= 999999:
        for index in range(len(device_storer)):
            P_list = device_storer[index].check_for_event()
            if P_list:
                event_buffer.append(P_list)
                device_storer[index].check_if_send(event_buffer[0])
            device_storer[index].check_if_send(Device.packet_list_1)
        Device.time_count += 1
    Device.time_count = 0

    while len(event_buffer) != 0:
        """handles when there are multiple events happening"""
        event_buffer.remove(event_buffer[0])
        while Device.time_count <= 999999:
            for index in range(len(device_storer)):
                if len(event_buffer) == 0:
                    pass
                else:
                    device_storer[index].check_if_send(event_buffer[0])
                    device_storer[index].check_if_send(Device.packet_list_1)
            Device.time_count += 1
        Device.time_count = 0
    Device.write_list.sort()
    sorting_list = []
    for lines in Device.write_list:
        tuple_1 = [int(lines.split("#")[0].split("@")[1]), lines]
        sorting_list.append(tuple_1)
    sorting_list.sort()
    A_list = []
    for data in sorting_list:
        A_list.append(data[1].split())
    concerned_device = []
    for index in range(len(A_list)):
        if A_list[index][2] == 'RECEIVED' and A_list[index][3] == 'CANCELLATION':
            if concerned_device.count(A_list[index][1]) == 0:
                concerned_device.append(A_list[index][1])
            else:
                A_list[index].append("del")
    A_list.append(["0","0","0","0","0","0","0","del"])
    deleter = 0
    remembered_device_info = []
    deleter_1 = 0
    compare_list = []
    B_list = []
    for item in A_list:
        B_list.append([item[1],item[2],item[3],item[4],item[5],item[6]])
    for index in range(len(A_list)):
        if compare_list.count(B_list[index]) == 0:
            compare_list.append(B_list[index])
        elif compare_list.count(B_list[index]) != 0:
            A_list[index].append("del")
        if A_list[index][3] == "ALERT" and A_list[index+1][3] == "CANCELLATION":
            if A_list[index][0] == A_list[index+1][0] and A_list[index][1] == A_list[index+1][1] and A_list[index][2] == A_list[index+1][2] == "RECEIVED" and A_list[index][-1] == A_list[index][-1]:
                A_list[index].append("del")
                remembered_device_info.append([A_list[index][1],A_list[index][-1]])
                deleter += 1
        if deleter >= 1 and A_list[index][3] == "ALERT" and A_list[index][2] == "SENT":
            for item in remembered_device_info:
                if item[0] == A_list[index][1] and item[1] == A_list[index][-1]:
                    A_list[index].append("del")
                    deleter_1 += 1
                    deleter -= 1
        if deleter_1 >= 1:
            if A_list[index][3] == "ALERT" and A_list[index][2] == "RECEIVED":
                for item in remembered_device_info:
                    if item[0] == A_list[index][-2] and item[1] == A_list[index][-1]:
                        A_list[index].append("del")
                        deleter_1 -= 1
    for Y in reversed(range(len(A_list))):
        if A_list[Y][-1] == "del":
            del A_list[Y]
    for Y in A_list:
        print(" ".join(Y))




def _read_input_file_path() -> Path:
    """Reads the input file path from the standard input."""
    """can't reach full coverage because path is not always the same"""
    return Path(input())

def readfile(path):
    """Read the input file and output the corresponding info."""
    """can't reach full coverage because the file is not always the same"""
    device_name_list = [] #["1","2","3","4"...]
    propagation_delay_list = [] #[("1","2","700"),("2","3","500")...]
    alert_cancellation_list = [] #[["ALERT","1","Trouble","0"]["CANCEL","1","Trouble","2200"]...]
    try:
        a = open(path, "r")
        a.close()
    except FileNotFoundError:
        print("FILE NOT FOUND")
        exit()
    with open(path, "r") as file:
        for lines in file.readlines():
            line = lines.strip("\n")
            if line.startswith("DEVICE"):
                device_name_list.append(line.split()[1])
            elif line.startswith("PROPAGATE"):
                x = line.split()
                y = x[1],x[2],x[3]
                propagation_delay_list.append(y)
            elif line.startswith("ALERT") or line.startswith("CANCEL"):
                alert_cancellation_list.append(line.split())
            else:
                continue
    return device_name_list, propagation_delay_list, alert_cancellation_list


if __name__ == '__main__':
    main()
