import os
import subprocess
import re

def general_info():
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
	top_ten = []
	for i in range(34, 44):
		line = re.split("\s+", cpu_output[i])
		top_ten.append([" ".join(line[0:len(line)-2]), line[len(line)-2]])
	return top_ten

def mem_top_ten():
	top_ten = []
	for i in range(34, 44):
		line = re.split("\s+", mem_output[i])
		number = re.split("[a-zA-Z]", line[len(line)-2])
		top_ten.append([" ".join(line[0:len(line)-2]), number[0]])
	return top_ten

def get_command_output(command):
	many_cols = os.environ.copy()
	many_cols["COLUMNS"] = "512"
	return str(subprocess.check_output(command, env = many_cols)).split("\\n")

command = ["top", "-b", "-n", "1"]
output = get_command_output(command)

cpu_dict = {"us": "User",
			"sy": "System",
			"id": "Idle",
			"ni": "Niced",
			"wa": "IO-Wait"}

def main():
	print(general_info())

if __name__ == '__main__':
	main()
