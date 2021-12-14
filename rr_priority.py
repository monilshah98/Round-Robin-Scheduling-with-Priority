'''
Script: 		Round-Robin with priority
Author:  		Monil Shah
Date: 			12/08/2021
'''


# Class based implementation of round-robin algorithm with priority
class RoundRobin:


	# intialize the constructor
	def __init__(self):
		self.initial_programs = [1, 2, 3]
		self.burst_time = [10, 7]
		self.priority = [2, 3]
		self.process_no = [1, 2]
		self.program_name = [1, 2]
		self.initial_priority = [2, 3, 1]
		self.ready_queue = [1, 2]
		self.parent_processes = [1, 2]
		self.child_processes = [2, 3]
		self.initial_burst_time = [10, 7, 5]
		self.gantt_chart = list()
		self.timer = 0;
		self.maincount = 0;
		self.gc_look = "0  ";
		self.whichproc = 0;


	# main function to implement round-robin with priority
	def Scheduling(self, time_quantum, time_slice):

		while(len(self.ready_queue)!=0):

			min_proc_ind = self.priority.index(min(self.priority))

			proc_num = self.ready_queue[min_proc_ind]

			prog_num = self.program_name[proc_num-1]    

			exe_time = 0

			if(self.burst_time[proc_num-1]>=4):
				exe_time = 4
			else:
				exe_time = self.burst_time[proc_num-1]

			burstTime = self.burst_time[proc_num-1]

			self.ReduceBT(proc_num)

			parentFlag = False

			if prog_num in self.parent_processes and burstTime/time_slice > 0:
				parentFlag = True

			if (parentFlag):
				self.AddToProcess(prog_num)

			if (self.burst_time[proc_num - 1] > 0):
				self.ready_queue.append(proc_num)
				self.priority.append(self.initial_priority[prog_num - 1])

			self.ready_queue.pop(min_proc_ind)
			self.priority.pop(min_proc_ind)

			for i in range(exe_time):
				self.gantt_chart.append(proc_num);

		# create gantt chart
		self.show_gc();


	# function to create gantt chart
	def show_gc(self):

		for i in range(len(self.gantt_chart) - 1):
			if i < len(self.gantt_chart) - 1 and self.gantt_chart[i] == self.gantt_chart[i + 1]:
				self.timer+=1
			else:
				self.maincount += self.timer + 1
				self.gc_look += "P" + str(self.gantt_chart[i]) + "  " + str(self.maincount) + "  "
				self.timer = 0
			self.whichproc = self.gantt_chart[i]

		self.maincount += self.timer + 1;
		self.gc_look += "P" + str(self.whichproc) + "  " + str(self.maincount)
		print(self.gc_look)


	# helper function
	def AddToProcess(self, progname):
		next_process_num = len(self.process_no) + 1
		self.process_no.append(next_process_num)
		child_program_num = self.child_processes[self.parent_processes.index(progname)]

		self.program_name.append(child_program_num)
		self.ready_queue.append(next_process_num)

		self.priority.append(self.initial_priority[child_program_num - 1])
		self.burst_time.append(self.initial_burst_time[child_program_num - 1])


	def ReduceBT(self, processNumber):
		val = self.burst_time[processNumber - 1]
		if val > time_quantum:
			self.burst_time[processNumber - 1] = val - time_quantum
		else:
			self.burst_time[processNumber - 1] = 0


# main driver code
if __name__=="__main__":

	time_quantum = 4
	time_slice = 3

	rr = RoundRobin()

	rr.Scheduling(time_quantum, time_slice)
