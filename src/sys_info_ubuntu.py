import os
import subprocess
import re

cpu_command = ["top", "-o", "%CPU", "-b", "-n", "1"]
mem_command = ["top", "-o", "%MEM", "-b", "-n", "1"]

def general_info():
    output = get_command_output(cpu_command)
    cpu = output[2].split() #%Cpu(s):  0.6 us,  0.2 sy,  0.1 ni, 98.6 id,  0.5 wa,  0.0 hi,  0.0 si,  0.0 st
    cpu_string = "CPU Usage: "
    for i in range(1,10,2):
        key = cpu[i+1]
        key = key[0:len(key)-1]
        cpu_string = cpu_string + cpu[i] + "% " + cpu_dict[key]
        if i < 9:
            cpu_string = cpu_string + ", "

    mem = output[3].split() #KiB Mem:   3690444 total,  3017848 used,   672596 free,   597656 buffers
    mem_string = "Memory Usage: "
    for i in range(2,9,2):
        mem_string = mem_string + str(int(mem[i])/1000) + " MiB " + mem[i+1]
        if i < 8:
            mem_string = mem_string + " "

    return [cpu_string, mem_string]

def cpu_top_ten():
    output = get_command_output(cpu_command)
    top_ten = []
    for i in range(8, 18):
        #line = re.split("\s+", output[i])
        line = output[i].split()
        top_ten.append([line[11].replace(',','.'), line[8].replace(',','.')])
    return top_ten

def mem_top_ten():
    output = get_command_output(mem_command)
    top_ten = []
    for i in range(34, 44):
        #line = re.split("\s+", output[i])
        line = output[i].split()
        number = re.split("[a-zA-Z]", line[9].replace(',','.'))
        top_ten.append([line[11], number])
    return top_ten

def get_command_output(command):
    many_cols = os.environ.copy()
    many_cols["COLUMNS"] = "512"
    return str(subprocess.check_output(command, env = many_cols)).split("\\n")

cpu_dict = {"us": "User",
            "sy": "System",
            "id": "Idle",
            "ni": "Niced",
            "wa": "IO-Wait"}

def main():
    print(cpu_top_ten())
    print(mem_top_ten())

if __name__ == '__main__':
    main()
