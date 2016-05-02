import subprocess

cpu_command = ["top", "-o", "cpu", "-l", "2", "-n", "10"]
mem_command = ["top", "-o", "mem", "-l", "2", "-n", "10"]

def main():
	cpu_output = get_command_output(cpu_command)
	for line in cpu_output:
		print(line)
	#print(cpu_output)

def cpu_graph():
	cpu_output = get_command_output(cpu_command)

def mem_graph():
	mem_output = get_command_output(mem_command)

def get_command_output(command):
	return str(subprocess.check_output(command)).split("\\n")

if __name__ == '__main__':
	main()