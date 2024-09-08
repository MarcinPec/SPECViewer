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
        os_version = f"Windows {major}"
        return os_version

    @staticmethod
    def os_view_det():
        version_info1 = win32api.GetVersionEx(1)
        major, minor, build, platform, text = version_info1[:5]
        version_info2a = win32api.GetSystemMetrics(0)
        version_info2b =  win32api.GetSystemMetrics(1)
        version_info3 = win32api.GetUserName()
        version_info4 = win32api.GetComputerName()
        os_version1 = (f"Windows {major}.{minor}\n"
                      f"Build ver.: {build}")
        os_version2 = f"Screen res.: {version_info2a}x{version_info2b}"
        os_version3 = (f"User name: {version_info3}\n"
                       f"PC name: {version_info4}")

        return (f'{os_version1}\n'
                f'{os_version2}\n'
                f'{os_version3}')

    @staticmethod
    def cpu_view():
        cpu_i = cpuinfo.get_cpu_info()
        result = f"{cpu_i['brand_raw']} @ {round(psutil.cpu_freq().max/1000, 2)} GHz"

        return result

    @staticmethod
    def cpu_view_det():
        cpu_i = cpuinfo.get_cpu_info()
        cpu_l2 = cpu_i.get('l2_cache_size', 'N/A')
        cpu_l3 = cpu_i.get('l3_cache_size', 'N/A')
        cpu_turbo = psutil.cpu_freq().max
        result = (f"Cores: {psutil.cpu_count(logical=False)}\n"
                  f"Logical cores: {psutil.cpu_count(logical=True)}\n"
                  f"Turbo: {cpu_turbo/1000:.2f} GHz\n"
                  f"L2 Cache: {round(cpu_l2/1000000)} MB\n"
                  f"L3 Cache: {round(cpu_l3/1000000)} MB")
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
        if self.group == "os_d":
            return f'{self.os_view_det()}'
        if self.group == "cpu":
            return f'{self.cpu_view()}'
        if self.group == "cpu_d":
            return f'{self.cpu_view_det()}'
        if self.group == "ram":
            return f'{self.ram_view()}'
        if self.group == "gpu":
            return f'{self.gpu_view()}'

test = SpecView("cpu_d")
print(test)