#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu

from collector import get_initial, get_data
from dashboardUIui import dashUIUI
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, time

class dashUI(dashUIUI):
    def __init__(self, master=None):
        super().__init__(master)

        initial_dict = get_initial()
        self.lbl_hostname.set(initial_dict.get('name'))
        self.lbl_ram_tot.set(round(int(initial_dict.get('memTotal')) / (1024**3), 3))
        self.lbl_swap_tot.set(round(int(initial_dict.get('swapTotal')) / (1024**3), 3))
        self.lbl_disk_tot.set(round(int(initial_dict.get('diskTotal')) / (1024**3), 3))

    def get_time(self):
        current_time = datetime.now()
        time_val = current_time.strftime("%H:%M:%S")
        return time_val

    def update_ui(self):
        data_dict = get_data()
        self.lbl_cpu_perc.set(float(data_dict.get('cpuUsage')))

        self.lbl_ram_avbl.set(round(int(data_dict.get('memoryAvailable')) / (1024**3), 3))
        self.lbl_ram_used.set(round((self.lbl_ram_tot.get() - self.lbl_ram_avbl.get()), 3))
        self.ram_usage_perc.set(round(self.lbl_ram_used.get() / self.lbl_ram_tot.get() * 100, 2))

        self.lbl_swap_free.set(round(int(data_dict.get('swapAvailable')) / (1024**3), 3))
        self.lbl_swap_used.set(round(self.lbl_swap_tot.get() - self.lbl_swap_free.get(), 3))
        self.lbl_swap_perc.set(round(self.lbl_swap_used.get() / self.lbl_swap_tot.get() * 100, 2))

        self.lbl_disk_free.set(round(int(data_dict.get('diskFree')) / (1024**3), 3))
        self.lbl_disk_used.set(round(self.lbl_disk_tot.get() - self.lbl_disk_free.get(), 3))
        self.lbl_disk_perc.set(round(self.lbl_disk_used.get() / self.lbl_disk_tot.get() * 100, 2))

        self.lbl_io_writes.set(int(data_dict.get('ioWriteCount')))
        self.lbl_io_reads.set(int(data_dict.get('ioReadCount')))
        self.lbl_io_wbyte.set(round(int(data_dict.get('ioWriteBytes')) / (1024**3), 3))
        self.lbl_io_rbyte.set(round(int(data_dict.get('ioReadBytes')) / (1024**3), 3))

        self.lbl_net_up.set(round(int(data_dict.get('netSentBytes')) / (1024**3), 3))
        self.lbl_net_down.set(round(int(data_dict.get('netRecvBytes')) / (1024**3), 3))
        self.lbl_net_psent.set(int(data_dict.get('netSentPackets')))
        self.lbl_net_precv.set(int(data_dict.get('netRecvPackets')))
        self.lbl_net_errin.set(int(data_dict.get('netErrin')))
        self.lbl_net_errout.set(int(data_dict.get('netErrout')))
        self.counter += 2
        self.timestamp.append(self.counter)
        self.cpuData.append(self.lbl_cpu_perc.get())
        self.ramData.append(self.ram_usage_perc.get())
        self.net_packets_up.append(self.lbl_net_psent.get())
        self.net_packets_down.append(self.lbl_net_precv.get())
        self.netUp_data.append(self.lbl_net_up.get())
        self.netDown_data.append(self.lbl_net_down.get())
        self.io_wops_data.append(self.lbl_io_writes.get())
        self.io_rops_data.append(self.lbl_io_reads.get())

        self.mainwindow.after(2000, self.update_ui)


    def create_graphs(self):
        self.fig_perc.suptitle('Metrics')
        #plt.subplots_adjust(hspace=1)

        self.axes[0,0].set_title('CPU Usage %')
        self.axes[0,1].set_title('RAM Usage %')
        self.axes[1,0].set_title('Net Packets')
        self.axes[1,1].set_title('Net Bytes')
        self.axes[1,2].set_title('IO Ops')

        # self.axes[0,0].plot(self.timestamp, self.cpuData)

        self.fig_perc.canvas.draw()



    def update_graphs(self):
        self.cpu_line.set_data( self.timestamp, self.cpuData)
        self.ram_line.set_data(self.timestamp, self.ramData)
        self.net_recv_line.set_data(self.timestamp, self.net_packets_up)
        # self.net_sent_line.set_data(self.timestamp, self.net_packets_down)
        # self.net_up_line.set_data(self.timestamp, self.netUp_data)
        # self.net_down_line.set_data(self.timestamp, self.netDown_data)
        # self.io_read_line.set_data(self.timestamp, self.io_rops_data)
        # self.io_write_line.set_data(self.timestamp, self.io_wops_data)
        #self.canvas_perc.figure.update()
        self.axes[0, 0].plot(self.timestamp, self.cpuData, '-r')
        self.axes[0, 1].plot(self.timestamp, self.ramData, '-b')
        self.axes[1,0].plot(self.timestamp, self.net_packets_up, '-r')
        self.axes[1,0].plot(self.timestamp, self.net_packets_down, '-b')
        self.axes[1,1].plot(self.timestamp, self.netUp_data, '-r')
        self.axes[1,1].plot(self.timestamp, self.netDown_data, '-b')
        self.axes[1,2].plot(self.timestamp, self.io_wops_data, '-r')
        self.axes[1,2].plot(self.timestamp, self.io_rops_data, '-b')
        self.canvas_perc.draw()



        self.mainwindow.after(2000, self.update_graphs)



if __name__ == "__main__":
    appMain = dashUI()
    appMain.update_ui()
    appMain.create_graphs()
    appMain.update_graphs()
    appMain.run()

