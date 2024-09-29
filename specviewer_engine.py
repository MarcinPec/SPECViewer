import psutil
import cpuinfo
import GPUtil
import wmi
from datetime import datetime


memory_types = {
    0: "Unknown",
    1: "Other",
    2: "DRAM",
    3: "Synchronous DRAM",
    4: "Cache DRAM",
    5: "EDO",
    6: "EDRAM",
    7: "VRAM",
    8: "SRAM",
    9: "RAM",
    10: "ROM",
    11: "Flash",
    12: "EEPROM",
    13: "FEPROM",
    14: "EPROM",
    15: "CDRAM",
    16: "3DRAM",
    17: "SDRAM",
    18: "SGRAM",
    19: "RDRAM",
    20: "DDR",
    21: "DDR2",
    22: "DDR2 FB-DIMM",
    24: "DDR3",
    26: "DDR4"
}

form_factors = {
    0: "Unknown",
    1: "Other",
    2: "SIP",
    3: "DIP",
    4: "ZIP",
    5: "SOJ",
    6: "Proprietary",
    7: "SIMM",
    8: "DIMM",
    9: "TSOP",
    10: "PGA",
    11: "RIMM",
    12: "SODIMM",
    13: "SRIMM",
    14: "SMD",
    15: "SSMP",
    16: "QFP",
    17: "TQFP",
    18: "SOIC",
    19: "LCC",
    20: "PLCC",
    21: "BGA",
    22: "FPBGA",
    23: "LGA"
}


class SpecView:
    def __init__(self, group):
        self.group = group

    @staticmethod
    def cpu_view():
        cpu_i = wmi.WMI()
        result = ""
        for data in cpu_i.Win32_Processor():
            result += f"{data.Name}"
        return result

    @staticmethod
    def cpu_view_det():
        cpu_i = wmi.WMI()
        result = ""
        for cpu in cpu_i.Win32_Processor():
            result += (f'Name: {cpu.Name}\n'
                       f'Base Clock Speed: {cpu.MaxClockSpeed} MHz\n'
                       f'Turbo Clock Speed: {cpu.CurrentClockSpeed} MHz\n'
                       f'L2 Cache Size: {cpu.L2CacheSize} KB\n'
                       f'L3 Cache Size: {cpu.L3CacheSize} KB')
        return result

    @staticmethod
    def ram_view():
        ram_i = psutil.virtual_memory()
        result = f"{round(ram_i.total/1024**3)} GB"
        return result

    @staticmethod
    def ram_view_det():
        c = wmi.WMI()
        ram_i_det = c.Win32_PhysicalMemory()
        result = ""

        for memory in ram_i_det:
            smbios_memory_type = memory_types.get(memory.SMBIOSMemoryType)
            form_factor = form_factors.get(memory.FormFactor)

            result += f"Slot: {memory.BankLabel}\n"
            result += f"Type: {smbios_memory_type} ({form_factor})\n"
            result += f"Size: {int(memory.Capacity) / (1024 ** 3):.2f} GB\n"
            result += f"Frequency: {memory.Speed} MHz\n\n"

        return result

    @staticmethod
    def gpu_view():
        gpu_i = GPUtil.getGPUs()
        if not gpu_i:
            return "No GPU detected."
        result = ""
        for gpu in gpu_i:
            result += f"{gpu.name}\n"
        return result

    @staticmethod
    def gpu_view_det():
        gpu_i = GPUtil.getGPUs()
        if not gpu_i:
            return "No GPU detected."
        result = ""
        for gpu in gpu_i:
            result += (f"Name: {gpu.name}\n"
                       f"ID: {gpu.id}\n"
                       f"Driver: {gpu.driver}\n"
                       f"Serial: {gpu.serial}\n"
                       f"Load: {round(gpu.load,2) * 100}%\n"
                       f"Memory used:  {gpu.memoryUsed}MB\n"
                       f"Memory total: {gpu.memoryTotal}MB\n"
                       f"Memory free: {gpu.memoryFree}MB\n"
                       f"Temperature: {gpu.temperature}°C\n")
        return result

    @staticmethod
    def mb_view():
        mobo = wmi.WMI()
        result = ""

        for board in mobo.Win32_BaseBoard():
            result += f" {board.Manufacturer}, {board.Product}"

        return result

    @staticmethod
    def mb_view_det():
        mobo = wmi.WMI()
        raw_date = ""
        result = ""
        for bios_date in mobo.Win32_BIOS():
            raw_date += f"{bios_date.ReleaseDate}"

        date_str = raw_date.split('.')[0]
        date_obj = datetime.strptime(date_str, "%Y%m%d%H%M%S")
        formatted_date = date_obj.strftime("%d-%m-%Y")

        for board in mobo.Win32_BaseBoard():
            result += (f"Mod.: {board.Product}\n"
                       f"Ver.: {board.Version}\n"
                       f"Serial: {board.SerialNumber}\n")

        for bios in mobo.Win32_BIOS():
            result += (f"BIOS Name: {bios.Manufacturer}\n"
                       f"BIOS Ver.: {bios.SMBIOSBIOSVersion}\n"
                       f"BIOS Release Date: {formatted_date}")
        return result

    @staticmethod
    def get_disk_info():
        disk_info = psutil.disk_partitions()
        disk_details = []

        for partition in disk_info:
            partition_info = {
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "fstype": partition.fstype,
                "opts": partition.opts
            }

            # Uzyskaj dane o wykorzystaniu dysku
            usage = psutil.disk_usage(partition.mountpoint)
            partition_info["total"] = usage.total
            partition_info["used"] = usage.used
            partition_info["free"] = usage.free
            partition_info["percent"] = usage.percent

            disk_details.append(partition_info)

        return disk_details

    def disc_view(self):
        disk_details = self.get_disk_info()
        result = ""
        for disk in disk_details:
            result += f" {disk['device']} - {disk['total'] / (1024 ** 3):.2f} GB\n"
        return result

    def disc_view_det(self):
        disk_details = self.get_disk_info()
        result = ""
        for disk in disk_details:
            result += (f"Device: {disk['device']}\n"
                       f"Mountpoint: {disk['mountpoint']}\n"
                       f"Filesystem type: {disk['fstype']}\n"
                       f"Options: {disk['opts']}\n"
                       f"Total size: {disk['total'] / (1024 ** 3):.2f} GB\n"
                       f"Used space: {disk['used'] / (1024 ** 3):.2f} GB\n"
                       f"Free space: {disk['free'] / (1024 ** 3):.2f} GB\n"
                       f"-------------------\n")

        return result

    def __str__(self):
        if self.group == "cpu":
            return f'{self.cpu_view()}'
        if self.group == "cpu_d":
            return f'{self.cpu_view_det()}'
        if self.group == "ram":
            return f'{self.ram_view()}'
        if self.group == "ram_d":
            return f'{self.ram_view_det()}'
        if self.group == "gpu":
            return f'{self.gpu_view()}'
        if self.group == "gpu_d":
            return f'{self.gpu_view_det()}'
        if self.group == "mb":
            return f'{self.mb_view()}'
        if self.group == "mb_d":
            return f'{self.mb_view_det()}'
        if self.group == "dsc":
            return f'{self.disc_view()}'
        if self.group == "dsc_d":
            return f'{self.disc_view_det()}'

test = SpecView('cpu_d')
print(test)
