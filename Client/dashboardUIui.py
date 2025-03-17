#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "server_dashboard_uiWIP.ui"
RESOURCE_PATHS = [PROJECT_PATH]


class dashUIUI:
    def __init__(self, master=None):
        self.builder = pygubu.Builder()
        self.builder.add_resource_paths(RESOURCE_PATHS)
        self.builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow: tk.Toplevel = self.builder.get_object(
            "toplevel1", master)

        self.lbl_hostname: tk.DoubleVar = None
        self.lbl_cpu_perc: tk.DoubleVar = None
        self.ram_usage_perc: tk.DoubleVar = None
        self.lbl_ram_avbl: tk.DoubleVar = None
        self.lbl_ram_used: tk.DoubleVar = None
        self.lbl_ram_tot: tk.DoubleVar = None
        self.lbl_disk_perc: tk.DoubleVar = None
        self.lbl_disk_free: tk.DoubleVar = None
        self.lbl_disk_used: tk.DoubleVar = None
        self.lbl_disk_tot: tk.DoubleVar = None
        self.lbl_swap_perc: tk.DoubleVar = None
        self.lbl_swap_free: tk.DoubleVar = None
        self.lbl_swap_used: tk.DoubleVar = None
        self.lbl_swap_tot: tk.DoubleVar = None
        self.lbl_io_writes: tk.IntVar = None
        self.lbl_io_reads: tk.IntVar = None
        self.lbl_io_wbyte: tk.DoubleVar = None
        self.lbl_io_rbyte: tk.DoubleVar = None
        self.lbl_net_precv: tk.IntVar = None
        self.lbl_net_psent: tk.IntVar = None
        self.lbl_net_up: tk.DoubleVar = None
        self.lbl_net_down: tk.DoubleVar = None
        self.lbl_net_errin: tk.IntVar = None
        self.lbl_net_errout: tk.IntVar = None
        self.counter = 1
        self.timestamp = []
        self.cpuData, self.ramData, self.net_packets_up, self.net_packets_down = [], [], [], []
        self.netUp_data, self.netDown_data, self.io_wops_data, self.io_rops_data = [], [], [], []

        perc_cont = self.builder.get_object('cnvs_perc_readout')

        self.fig_perc, self.axes = plt.subplots(2,3,figsize=(16, 8))

        self.cpu_line, = self.axes[0,0].plot([], [])
        self.ram_line, = self.axes[0,1].plot([], [])
        self.net_recv_line, = self.axes[1,0].plot([], [], '-r', label='Recv')
        self.net_sent_line, = self.axes[1,0].plot([], [], '-b', label='Sent')
        self.axes[1,0].legend()
        self.net_up_line, = self.axes[1,1].plot([], [], '-r', label='Up')
        self.net_down_line, = self.axes[1,1].plot([], [], '-b', label='Down')
        self.axes[1,1].legend()
        self.io_read_line, = self.axes[1,2].plot([], [], '-r', label='Read')
        self.io_write_line, = self.axes[1,2].plot([], [], '-b', label='Write')
        self.axes[1,2].legend()

        # for ax in self.axes.flat:
        #     ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
        #     #ax.set_ylim(0, 100)

        self.canvas_perc = FigureCanvasTkAgg(self.fig_perc, master=perc_cont)
        self.renderer = self.canvas_perc.get_renderer()
        self.canvas_perc.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        self.builder.import_variables(self)

        self.builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()




if __name__ == "__main__":
    app = dashUIUI()
    app.run()
