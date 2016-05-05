import os
import subprocess
import re

cpu_command = ["top", "-o", "cpu", "-l", "2", "-stats", "command,cpu", "-n", "10"]
mem_command = ["top", "-o", "mem", "-l", "2", "-stats", "command,mem", "-n", "10"]

def main():
	print(mem_top_ten())

def general_info():
	output = get_command_output(cpu_command)
	cpu = output[3] #CPU usage: 7.14% user, 25.0% sys, 67.85% idle 
	mem = output[6] #PhysMem: 2637M used (783M wired), 1457M unused.
	return [cpu, mem]

# Slightly broken but found out it wouldn't work on ubuntu anyways...
def cpu_top_ten():
	output = get_command_output(cpu_command)
	top_ten = []
	for i in range(34, 44):
		line = re.split("\s+", cpu_output[i])
		top_ten.append([" ".join(line[0:len(line)-2]), line[len(line)-2]])
	return top_ten

def mem_top_ten():
	output = get_command_output(mem_command)
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

if __name__ == '__main__':
	main()
