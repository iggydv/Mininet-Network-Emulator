from tkinter import *
from Parser import *
from tkinter import ttk
import math
import configparser, os
from tkinter import messagebox
import fileinput
from tkinter.messagebox import *

class MininetNetworkEmulator(Frame):
    p=5
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.dir = ''
        self.parent = parent
        self.Host_file = ''
        self.Switch_file = ''
        self.working_directory()
        self.sCount = 0
        self.links = ''
        self.links2 = []
        self.sName = []
        self.hName = []
        self.host_list = ''
        self.hCount = 0
        self.button_pressed = 0
        self.found = 0
        self.x0 = -50
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        
        
        
        self.wSwitches = LabelFrame(self, text="Switches", padx=self.p, pady=self.p, font=("Times New Roman", 10, 'bold'))
        self.wSwitches.grid(row=0, column=1, rowspan=2, sticky=W+E+N+S, padx=self.p, pady=self.p)

        self.wHosts = LabelFrame(self, text="Hosts", padx=self.p, pady=self.p, font=("Times New Roman", 10,  'bold'))
        self.wHosts.grid(row=0, column=0, sticky=W+E+N+S, padx=self.p, pady=self.p)

        self.wLinks = LabelFrame(self, text="Links", padx=self.p, pady=self.p, font=("Times New Roman", 10, 'bold'))
        self.wLinks.grid(row=0, column=2, sticky=W+E+N+S, padx=self.p, pady=self.p)
        
        self.initGUI()
        self.CreateSwitchWidget(self.wSwitches)
        self.CreateHostWidget(self.wHosts)
        self.CreateLinkWidget(self.wLinks)
        
        
        bQuit = Button(self, text="Quit",command= lambda: Quit(self), padx=self.p, pady=self.p, font=("Times New Roman", 9), bg = 'red')
        bQuit.grid(row=2, column=2, sticky=E+S, padx=self.p, pady=self.p)

        def Quit(self):
            self.parent.destroy()
            self.Switch_file.close()
            self.Host_file.close()
            
    def working_directory(self):
        
        self.parent.withdraw()
        OK = 0
        Folder = ''
        top = Toplevel()
        top.geometry("300x200")
        top.title("Save Folder")
        
        lblDir = Label(top,text = "Enter Directory", font=("Times New Roman", 9))
        lblDir.pack(fill =X,padx=3,pady=3)
        
        Path_Entered = StringVar()
        Entry_Dir = Entry(top, textvariable= Path_Entered)
        Entry_Dir.pack()
        
        AddHost = Button(top,text = "Create Folder", command = lambda : create_path(), font=("Times New Roman", 9))
        AddHost.pack(padx=3,pady=3)
        
        bQuit = Button(top, text="Quit",command= lambda: exit(0) , padx=self.p, pady=self.p, font=("Times New Roman", 9), bg = 'red')
        bQuit.pack(padx=3,pady=3)
        
        def create_path(event=None):
            Folder = str(Path_Entered.get())
            self.dir = 'D:/WinPython-64bit-3.4.3.7/MyWork/Skripsie/'+Folder
            if not os.path.exists(self.dir):
                os.makedirs(self.dir)
            os.chdir(self.dir)
            top.withdraw()
            top.destroy()
            self.parent.update()
            self.parent.deiconify()
            self.Host_file = open('hosts2.txt','w')
            self.Switch_file = open('switches2.txt','w+')
            return
        return
    
    def initGUI(self):
        
        self.parent.title('Mininet Network Emulator')
        self.pack(fill = BOTH, expand=1)
        
        return
    
    def CreateSwitchWidget(self, widget):
        Empty0 = Label(self.wSwitches,text = "") #just for spacing
        Empty0.pack(fill =X,padx=3,pady=3)
        Empty1 = Label(self.wSwitches,text = "") #just for spacing
        Empty1.pack(fill =X,padx=3,pady=3)
        lbl1 = Label(self.wSwitches,text = "DEFAULT CONNECTION PARAMETERS\n------------------\nBandwidth (MBit)", font=("Times New Roman",9))
        lbl1.pack(fill =X,padx=3,pady=3)
        global g_bw
        g_bw = DoubleVar()
        e1 = Entry(self.wSwitches, textvariable=g_bw)
        e1.pack(padx=3,pady=3)

        global g_Loss
        lbl2 = Label(self.wSwitches,text = "Loss (%)", font=("Times New Roman", 9))
        lbl2.pack(fill =X,padx=3,pady=3)
        g_Loss = IntVar()
        e2 = Entry(self.wSwitches, textvariable=g_Loss)
        e2.pack(padx=3,pady=3)

        global g_delay
        lbl3 = Label(self.wSwitches,text = "Delay (ms)", font=("Times New Roman", 9))
        lbl3.pack(fill =X,padx=3,pady=3)
        g_delay = IntVar()
        e3 = Entry(self.wSwitches, textvariable=g_delay)
        e3.pack(padx=3,pady=3)

        global g_jitter
        lbl4 = Label(self.wSwitches,text = "Jitter", font=("Times New Roman", 9))
        lbl4.pack(fill =X,padx=3,pady=3)
        g_jitter = IntVar()
        e4 = Entry(self.wSwitches, textvariable=g_jitter)
        e4.pack(padx=3,pady=3)

        Empty = Label(self.wSwitches,text = "------------------", font=("Times New Roman", 9)) #just for spacing
        Empty.pack(fill =X,padx=3,pady=3)
        
        AddSwitch = Button(self.wSwitches, text = "Add Switch",command = lambda: add_switch(), font=("Times New Roman", 9))
        AddSwitch.pack(fill =X,padx=3,pady=3)
        global Lb2
        Lb2 = Listbox(self.wLinks, exportselection =0)
        Lb2.grid(row=1, column=1, sticky=W+E+N+S, padx=5, pady=5)
        
        def add_switch():
            self.sCount +=1
            s = "S"+str(self.sCount)
            Lb2.insert(END, s)
            self.Switch_file.close()
            self.sName.append(s)
            #self.Switch_file.write("[%s]\nhosts=%s\nbw =%d\nloss =%d\ndelay =%d\njitter =%d\n\n"%(s,None,g_bw.get(),g_Loss.get(),g_delay.get(),g_jitter.get()))
            print("Switch %s created"%s)
            
            config = configparser.ConfigParser()
            config.read('switches2.txt')
            config.add_section(s)
            config.set(s, 'hosts', 'None')
            config.set(s, 'bw', str(g_bw.get()))
            config.set(s, 'loss',str(g_Loss.get()))
            config.set(s, 'delay',str(g_delay.get()))
            config.set(s, 'jitter',str(g_jitter.get()))
            
            with open('switches2.txt','w') as configfile:
                config.write(configfile)
            
            return

    def CreateHostWidget(self, widget):
        lbl0 = Label(self.wHosts,text = "Host Name", font=("Times New Roman", 9))
        lbl0.pack(fill =X,padx=3,pady=3)
        ID = StringVar()
        ID.set('e.g. Host_1')

        def callback(event):
            ID.set('')
        e0 = Entry(self.wHosts, textvariable=ID, fg = 'grey')
        e0.pack(padx=3,pady=3)
        e0.bind('<Button-1>', callback)
        
        
            
        lbl1 = Label(self.wHosts,text = "CONNECTION PARAMETERS\n------------------\nBandwidth (MBit)", font=("Times New Roman", 9))
        lbl1.pack(fill =X,padx=3,pady=3)
        bw = DoubleVar()
        e1 = Entry(self.wHosts, textvariable=bw)
        e1.pack(padx=3,pady=3)
        
        lbl2 = Label(self.wHosts,text = "Loss (%)", font=("Times New Roman", 9))
        lbl2.pack(fill =X,padx=3,pady=3)
        Loss = IntVar()
        e2 = Entry(self.wHosts, textvariable=Loss)
        e2.pack(padx=3,pady=3)
        
        lbl3 = Label(self.wHosts,text = "Delay (ms)", font=("Times New Roman", 9))
        lbl3.pack(fill =X,padx=3,pady=3)
        delay = IntVar()
        e3 = Entry(self.wHosts, textvariable=delay)
        e3.pack(padx=3,pady=3)
        
        lbl4 = Label(self.wHosts,text = "Jitter", font=("Times New Roman", 9))
        lbl4.pack(fill =X,padx=3,pady=3)
        jitter = IntVar()
        e4 = Entry(self.wHosts, textvariable=jitter)
        e4.pack(padx=3,pady=3)
        
        check = IntVar()
        c = Checkbutton(self.wHosts, text="Inherit Switch Parameters", variable = check, command = lambda: if_checked(), font=("Times New Roman", 9))
        c.pack(padx=3,pady=3)

        AddHost = Button(self.wHosts,text = "Add Host", command = lambda: add_Host(), font=("Times New Roman", 9))
        AddHost.pack(fill =X,padx=3,pady=3)
        global Lb1
        Lb1 = Listbox(self.wLinks,selectmode=MULTIPLE, exportselection =0)
        Lb1.grid(row=1, column=0, sticky=W+E+N+S, padx=5, pady=5)
        
        def add_Host():
            h = ID.get()
            self.hCount += 1
            default_h = "h"+str(self.hCount)
            
            if h in ('e.g. Host_1', '', default_h):
                default = 'h'+str(self.hCount+1)
                ID.set('')
                ID.set(default)
                h = 'h'+str(self.hCount)
            self.Host_file.close()   
            Lb1.insert(END, h)
            self.hName.append(h)
            #self.Host_file.write("[%s]\nbw =%d\nloss =%d\ndelay =%d\njitter =%d\n\n"%(h,bw.get(),Loss.get(),delay.get(),jitter.get()))
            print("Host %s created"%h)

            config = configparser.ConfigParser()
            config.read('hosts2.txt')
            config.add_section(h)
            config.set(h, 'bw', str(bw.get()))
            config.set(h, 'loss',str(Loss.get()))
            config.set(h, 'delay',str(delay.get()))
            config.set(h, 'jitter',str(jitter.get()))
            
            with open('hosts2.txt','w') as configfile:
                config.write(configfile)


            
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
        
    def move_box(self, event=None):
        deltax = event.x - self.x
        deltay = event.y - self.y
        closest = self.canvas.find_closest(event.x,  event.y, halo=1, start=None)

        #print("first: "+str(closest[0]))
        if closest[0] == 1 or closest[0] == 2:
            closest = "s"
        #print(str(closest[0]))
        if closest != "s":
            for x in range (3, self.hCount*3+3):
                if x == closest[0]:
                    x = (x-5)/3 +1
                    closest = 'r'+str(math.ceil(x))
                    break
            #print('closest: '+str(closest))
            arrow = "to_r"+str(math.ceil(x))
        self.canvas.move(closest, deltax, deltay)
        
        
        #print('arrow: '+arrow)
        #coords = self.canvas.coords(arrow)
        if closest == 's':
            for x in range (1, self.hCount+1):
                coords = self.canvas.coords("to_r"+str(x))
                coords[2] += deltax
                coords[3] += deltay
                self.canvas.coords("to_r"+str(x), *coords)
        else:
            coords = self.canvas.coords(arrow)
            coords[0] += deltax
            coords[1] += deltay
            self.canvas.coords(arrow, *coords)

        self.x = event.x
        self.y = event.y
        
    def start_move(self, event=None):
        self.x = event.x
        self.y = event.y
        
    def CreateVisualsWidget(self, widget):
        self.canvas = Canvas(self.wVisuals, width = 500, height = 500, borderwidth=0, highlightthickness=0, bg="white")
        self.canvas.grid()
        self.canvas.bind("<B1-Motion>", self.move_box)
        self.canvas.bind("<ButtonPress-1>", self.start_move)

        
            
        parser = Parser(self.dir)
        parser.parse()
        
        hosts = parser.get_Hosts()

        switchs = parser.get_Switches()
        links = parser.get_Links()
        count = 0
        self.canvas.create_oval(50, 200, 150,250, fill="seagreen2", tags="s")
        self.canvas.create_text((50+150)/2,(200+250)/2,text="S1", tags = "s")
        for host in hosts:
            count += 1
            #---------------------
            self.x0 = (self.x0+60)
            self.y0 = 10
            self.x1 = (self.x1+60)
            self.y1 = 50
            #---------------------
            current_tag = "r"+str(count)
            self.canvas.create_rectangle(self.x0,self.y0,self.x1,self.y1, fill="turquoise1", tags=current_tag)
            self.canvas.create_text((self.x0+self.x1)/2,(self.y0+self.y1)/2,text=host.getHostName(), tags = current_tag)
            self.canvas.create_line((self.x0+self.x1)/2,self.y1, (50+150)/2, 200, arrow="last", tags="to_r"+str(count))
            print(host.getHostName())
            
        return

        
    def CreateLinkWidget(self, widget):
        print(self.dir)
        lbl1 = Label(self.wLinks,text = "Host", font=("Times New Roman", 9))
        lbl1.grid(row=0, column=0, sticky=W+E+N+S, padx=5, pady=5)
        
        lbl2 = Label(self.wLinks,text = "Switch", font=("Times New Roman", 9))
        lbl2.grid(row=0, column=1, sticky=W+E+N+S, padx=5, pady=5)

        Comp = Button(self.wLinks,text = "Complete",command = lambda: done(), bg = 'green', font=("Times New Roman", 9))
        Comp.grid(row=3, column=0, sticky=W+E+N+S, padx=5, pady=5)

        AddLink = Button(self.wLinks,text = "Add Link",command = lambda: add_Link(), font=("Times New Roman", 9))
        AddLink.grid(row=2, column=0, sticky=W+E+N+S, padx=5, pady=5)
        
        def add_Link():
            if Lb1.index("end") == 0:
                messagebox.showerror("Error", "Please add a Host(s)")
                return
            if Lb2.index("end") == 0:
                messagebox.showerror("Error", "Please add a Switch(es)")
                return
            
            self.host_list =''
            self.Switch_file.close()
            selected_hosts = Lb1.curselection()
            selected_switch = Lb2.get(ACTIVE)
            if not selected_hosts:
                 messagebox.showerror("Error", "Please select a Host(s) and switch to Connect")
                 return
            self.button_pressed += 1
            for i in selected_hosts:
                hosts = Lb1.get(i)
                self.links2.append(hosts)
                print('Link between %s and %s created'%(hosts, selected_switch))
               
                    
            self.host_list = ','.join(self.links2)
            
            config = configparser.ConfigParser()
            config.read('switches2.txt')
            
            config.set(selected_switch, 'hosts', self.host_list)
            f = config.get(selected_switch, 'hosts')
            
            with open('switches2.txt','w') as configfile:
                config.write(configfile)   
            return
            

        def done():
            if self.button_pressed != 0:
                self.Host_file.close()
                if self.found == 0:
                    top = Toplevel()
                    self.wVisuals = LabelFrame(top, text="Visuals", padx=self.p, pady=self.p, font=("Times New Roman", 10, 'bold'))
                    self.wVisuals.grid(columnspan = 3,row=1, column=0, sticky=W+E+N+S, padx=self.p, pady=self.p)
                    self.CreateVisualsWidget(self.wVisuals)
                    self.Switch_file.close()
                    self.Host_file.close()
                self.found = 1
            else:
                messagebox.showerror("Error", "Please add a Link")
            return
        


root = Tk()
app = MininetNetworkEmulator(root)
root.mainloop()

