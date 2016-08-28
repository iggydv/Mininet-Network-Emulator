from tkinter import *
from tkinter import ttk
import configparser, os
import ctypes
import fileinput


class MininetNetworkEmulator(Frame):
    p=5
    


    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.Host_file = open('hosts2.txt','w')
        self.Switch_file = open('switches2.txt','w+')
        self.sCount = 0
        self.links = ''
        self.links2 = []
        self.sName = []
        self.hName = []
        self.host_list = ''
        self.hCount = 0
        self.button_pressed = 0
        self.wSwitches = LabelFrame(self, text="Switches", padx=self.p, pady=self.p)
        self.wSwitches.grid(row=0, column=1, rowspan=2, sticky=W+E+N+S, padx=self.p, pady=self.p)

        self.wHosts = LabelFrame(self, text="Hosts", padx=self.p, pady=self.p)
        self.wHosts.grid(row=0, column=0, sticky=W+E+N+S, padx=self.p, pady=self.p)

        self.wLinks = LabelFrame(self, text="Links", padx=self.p, pady=self.p)
        self.wLinks.grid(row=0, column=2, sticky=W+E+N+S, padx=self.p, pady=self.p)

        self.initGUI()
        self.CreateSwitchWidget(self.wSwitches)
        self.CreateHostWidget(self.wHosts)
        self.CreateLinkWidget(self.wLinks)
        
        bQuit = Button(self, text="Quit",command= lambda: Quit(self), padx=self.p, pady=self.p)
        bQuit.grid(row=2, column=2, sticky=E+S, padx=self.p, pady=self.p)

        def Quit(self):
            self.parent.destroy()
            self.Switch_file.close()
            self.Host_file.close()

    def CreateSwitchWidget(self, widget):

        lbl1 = Label(self.wSwitches,text = "DEFAULT LINK PARAMETERS\n------------------\nBandwidth (MBit)")
        lbl1.pack(fill =X,padx=3,pady=3)
        global g_bw
        g_bw = IntVar()
        e1 = Entry(self.wSwitches, textvariable=g_bw)
        e1.pack(padx=3,pady=3)

        global g_Loss
        lbl2 = Label(self.wSwitches,text = "Loss (%)")
        lbl2.pack(fill =X,padx=3,pady=3)
        g_Loss = IntVar()
        e2 = Entry(self.wSwitches, textvariable=g_Loss)
        e2.pack(padx=3,pady=3)

        global g_delay
        lbl3 = Label(self.wSwitches,text = "Delay (ms)")
        lbl3.pack(fill =X,padx=3,pady=3)
        g_delay = IntVar()
        e3 = Entry(self.wSwitches, textvariable=g_delay)
        e3.pack(padx=3,pady=3)

        global g_jitter
        lbl4 = Label(self.wSwitches,text = "Jitter")
        lbl4.pack(fill =X,padx=3,pady=3)
        g_jitter = IntVar()
        e4 = Entry(self.wSwitches, textvariable=g_jitter)
        e4.pack(padx=3,pady=3)

        Empty = Label(self.wSwitches,text = "------------------") #just for spacing
        Empty.pack(fill =X,padx=3,pady=3)
        
        AddSwitch = Button(self.wSwitches, text = "Add Switch",command = lambda: add_switch())
        AddSwitch.pack(fill =X,padx=3,pady=3)
        global Lb2
        Lb2 = Listbox(self.wLinks, exportselection =0)
        Lb2.grid(row=1, column=1, sticky=W+E+N+S, padx=5, pady=5)
        
        def add_switch():
            self.sCount +=1
            s = "S"+str(self.sCount)
            Lb2.insert(END, s)
            self.sName.append(s)
            self.Switch_file.write("[%s]\nhosts=%s\nbw =%d\nloss =%d\ndelay =%d\njitter =%d\n\n"%(s,None,g_bw.get(),g_Loss.get(),g_delay.get(),g_jitter.get()))
            print("Switch %s created"%s)
            return

    def CreateHostWidget(self, widget):
        
        lbl1 = Label(self.wHosts,text = "LINK PARAMETERS\n------------------\nBandwidth (MBit)")
        lbl1.pack(fill =X,padx=3,pady=3)
        bw = IntVar()
        e1 = Entry(self.wHosts, textvariable=bw)
        e1.pack(padx=3,pady=3)
        
        lbl2 = Label(self.wHosts,text = "Loss (%)")
        lbl2.pack(fill =X,padx=3,pady=3)
        Loss = IntVar()
        e2 = Entry(self.wHosts, textvariable=Loss)
        e2.pack(padx=3,pady=3)
        
        lbl3 = Label(self.wHosts,text = "Delay (ms)")
        lbl3.pack(fill =X,padx=3,pady=3)
        delay = IntVar()
        e3 = Entry(self.wHosts, textvariable=delay)
        e3.pack(padx=3,pady=3)
        
        lbl4 = Label(self.wHosts,text = "Jitter")
        lbl4.pack(fill =X,padx=3,pady=3)
        jitter = IntVar()
        e4 = Entry(self.wHosts, textvariable=jitter)
        e4.pack(padx=3,pady=3)
        
        check = IntVar()
        c = Checkbutton(self.wHosts, text="Inherit Switch Parameters", variable = check, command = lambda: if_checked())
        c.pack(padx=3,pady=3)

        AddHost = Button(self.wHosts,text = "Add Host", command = lambda: add_Host())
        AddHost.pack(fill =X,padx=3,pady=3)
        global Lb1
        Lb1 = Listbox(self.wLinks,selectmode=MULTIPLE, exportselection =0)
        Lb1.grid(row=1, column=0, sticky=W+E+N+S, padx=5, pady=5)
        
        def add_Host():
            self.hCount += 1
            h = "h"+str(self.hCount)
            Lb1.insert(END, h)
            self.hName.append(h)
            self.Host_file.write("[%s]\nbw =%d\nloss =%d\ndelay =%d\njitter =%d\n\n"%(h,bw.get(),Loss.get(),delay.get(),jitter.get()))
            print("Host %s created"%h)
            return
        
        def if_checked():
            if check.get() == 1:
                bw.set(g_bw.get())
                Loss.set(g_Loss.get())
                delay.set(g_delay.get())
                jitter.set(g_jitter.get())
            else:
                bw.set(0) 
                Loss.set(0)
                delay.set(0)
                jitter.set(0)
            return
        
    def CreateLinkWidget(self, widget):
        lbl1 = Label(self.wLinks,text = "Switch")
        lbl1.grid(row=0, column=0, sticky=W+E+N+S, padx=5, pady=5)
        
        lbl2 = Label(self.wLinks,text = "Host")
        lbl2.grid(row=0, column=1, sticky=W+E+N+S, padx=5, pady=5)

        Comp = Button(self.wLinks,text = "Complete",command = lambda: done(), bg = 'green')
        Comp.grid(row=3, column=0, sticky=W+E+N+S, padx=5, pady=5)

        AddLink = Button(self.wLinks,text = "Add Link",command = lambda: add_Link())
        AddLink.grid(row=2, column=0, sticky=W+E+N+S, padx=5, pady=5)
        
        def add_Link():
            self.button_pressed += 1
            self.host_list =''
            del self.links2[:]
            self.Switch_file.close()
            selected_hosts = Lb1.curselection()
            selected_switch = Lb2.get(ACTIVE)
            for i in selected_hosts:
                hosts = Lb1.get(i)
                self.links2.append(hosts)
                print('Link between %s and %s created'%(hosts, selected_switch))
            self.host_list = ','.join(self.links2)
            
            config = configparser.ConfigParser()
            config.read('switches2.txt')
            
            config.set(selected_switch, 'hosts', self.host_list)
            f = config.get(selected_switch, 'hosts')
            print(f)
            with open('switches2.txt','w') as configfile:
                config.write(configfile)
            return
            

        def done():
            #if self.links == '':
                #raise IndexError('No Links Created!')
            #f = open("switches2.txt",'r')
            #filedata = f.read()
            #f.close
            #newdata = filedata.replace("None",self.host_list)
            #f = open("switches2.txt",'w')
            #f.write(newdata)
            #f.close()
            self.Host_file.close()
            self.parent.destroy()
            return
        
        
    def initGUI(self):
        self.parent.title('Mininet Network Emulator')
        self.pack(fill = BOTH, expand=1)
        


root = Tk()
root.geometry("700x400+300+300")
app = MininetNetworkEmulator(root)
root.mainloop()


        
