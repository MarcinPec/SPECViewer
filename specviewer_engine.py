import psutil
import cpuinfo
import win32api
import GPUtil


class SpecView:
    def __init__(self, group):
        self.group = group

    @staticmethod
    def os_view():
        version_info = win32api.GetVersionEx(1)
        major, minor, build, platform, text = version_info[:5]
        os_version = f"Windows {major}.{minor} (Build {build})"
        return os_version

    @staticmethod
    def cpu_view():
        cpu_i = cpuinfo.get_cpu_info()
        result = (f"{cpu_i['brand_raw']}, {round(psutil.cpu_freq().max/1000, 2)} GHz, "
                  f"{psutil.cpu_count(logical=False)} "
                  f"({psutil.cpu_count(logical=True)}) cores")
        return result

    @staticmethod
    def ram_view():
        ram_i = psutil.virtual_memory()
        result = f"{round(ram_i.total/1024**3)} GB"
        return result

    @staticmethod
    def gpu_view():
        gpu_i = GPUtil.getGPUs()
        if not gpu_i:
            return "No GPU detected."
        result = ""
        for gpu in gpu_i:
            result += f"{gpu.name}, {round(gpu.memoryTotal/1000, 0)} GB\n"
        return result

    def __str__(self):
        if self.group == "os":
            return f'{self.os_view()}'
        if self.group == "cpu":
            return f'{self.cpu_view()}'
        if self.group == "ram":
            return f'{self.ram_view()}'
        if self.group == "gpu":
            return f'{self.gpu_view()}'
