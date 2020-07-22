import wmi 

def systeminfo():
    w = wmi.WMI()
    cpu_list = w.Win32_Processor()
    gpu_list = w.Win32_DisplayConfiguration()
    for item in cpu_list:
        cpu_name = item.name
    for item in gpu_list:
        gpu_name = item.SettingID
    return cpu_name,gpu_name

print(systeminfo())
