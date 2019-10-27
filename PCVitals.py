import psutil

class PCVitals:
	def sensors(self):
		a=psutil.sensors_temperatures()
		b=psutil.sensors_fans()
		c=psutil.sensors_battery()
		return a

	def process(self):
		psutil.Process(129)
# p.name()
# p.exe()
# p.cwd()
# p.pid
# p.children(recursive=True)
# p.parent()
# p.parents()
# p.status()
# p.username()
# p.create_time()
# p.terminal()
# p.uids()
# p.gids()
# p.cpu_times()
# p.suspend()
# p.resume()
# p.terminate()

	def network(self):
		a=psutil.net_io_counters(pernic=True)
		b=psutil.net_connections()
		c=psutil.net_if_addrs()
		d=psutil.net_if_stats()
		return a

	def cpu(self):
		psutil.cpu_percent()
		psutil.virtual_memory()
		psutil.cpu_stats()
		psutil.disk_usage("/dev")
		psutil.swap_memory()


	def usage(self):
		psutil.disk_partitions()
		psutil.users()
		psutil.boot_time()
		psutil.pids()
		psutil.test()



