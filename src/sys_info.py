import subprocess
import re

cpu_command = ["top", "-o", "cpu", "-l", "2", "-n", "10"]
mem_command = ["top", "-o", "mem", "-l", "2", "-n", "10"]

def main():
	print(cpu_top_ten())

def general_info():
	output = get_command_output(cpu_command)
	cpu = output[3] #CPU usage: 7.14% user, 25.0% sys, 67.85% idle 
	mem = output[6] #PhysMem: 2637M used (783M wired), 1457M unused.
	return [cpu, mem]

def cpu_top_ten():
	cpu_output = get_command_output(cpu_command)
	top_ten = []
	for i in range(34, 44):
		line = re.split("\s\s+", cpu_output[i])
		top_ten.append([line[1], line[2]])
	return top_ten

def mem_top_ten():
	mem_output = get_command_output(mem_command)
	top_ten = []
	for i in range(34, 44):
		line = re.split("\s\s+", mem_output[i])
		top_ten.append([line[1], line[2]])
	return top_ten

def get_command_output(command):
	return str(subprocess.check_output(command)).split("\\n")

if __name__ == '__main__':
	main()