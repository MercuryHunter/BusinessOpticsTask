from flask import Flask, render_template
import sys_info_ubuntu

app = Flask(__name__)

@app.route("/")
def main():
	main_info = sys_info_ubuntu.general_info()
	main_cpu_info = main_info[0]
	main_mem_info = main_info[1]

	cpu_ten = [] #sys_info_ubuntu.cpu_top_ten()
	mem_ten = [] #sys_info_ubuntu.mem_top_ten()

	return render_template("index.html", CPU = main_cpu_info, MEM = main_mem_info, CPU_TEN=cpu_ten, MEM_TEN=mem_ten)

if __name__ == "__main__":
    app.run()
