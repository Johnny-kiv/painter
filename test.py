from tkinter import *

class Paint(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.brush_size = 10
        self.color = "red"
        self.brush_color = self.color
        self.setUI()
        inp = open("descriptor.txt")
        lines = inp.read().split("\n")
        y = 0

        for line in lines:
            y += 1
            pixels = line.split("|")
            pixels.pop(-1)
            x = 0
            for pixel in pixels:
                p = pixel.split(" ")
                r = int(p[0])  # red
                g = int(p[1])  # green
                b = int(p[2])  # blue
                rgb = r, g, b
                self.canv.create_line(x, y, x + 1, y, fill=self.get_rgb(rgb))
                x += 1

    def get_rgb(self,rgb):
        r, g, b = rgb
        return f'#{r:02x}{g:02x}{b:02x}'
    def draw(self,event):
        self.canv.create_rectangle(event.x - self.brush_size,event.y - self.brush_size,event.x + self.brush_size,event.y + self.brush_size,fill=self.color,outline=self.brush_color)
    def set_color(self,new_color):
        self.color=new_color
        self.brush_color=self.color
    def set_brush_size(self,new_color):
        self.brush_size=new_color
    def setUI(self):
        self.parent.title = "Draw"
        self.pack(fill=BOTH,expand=1)
        self.columnconfigure(6,weight=1)
        self.rowconfigure(2,weight=1)
        self.canv = Canvas(self,bg="white",width=640,height=480)
        self.canv.grid(row=2,column=0,columnspan=7,padx = 5,pady=5,sticky=E+W+S+N)

        self.canv.bind("<B1-Motion>",self.draw)

        # Create canvas



        color_lab = Label(self,text="Color: ")
        color_lab.grid(row=0,column=1,padx=6)

        red_btn = Button(self,text="red",width=10,command=lambda: self.set_color("red"))
        red_btn.grid(row=0,column=2)
        yellow_btn = Button(self,text="yellow",width=10,command=lambda: self.set_color("yellow"))
        yellow_btn.grid(row=0,column=3)
        green_btn = Button(self,text="green",width=10,command=lambda: self.set_color("green"))
        green_btn.grid(row=0,column=4)
        blue_btn = Button(self,text="blue",width=10,command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0,column=5)
        black_btn = Button(self,text="black",width=10,command=lambda: self.set_color("black"))
        black_btn.grid(row=0,column=6)
        eraser_btn = Button(self,text="eraser",width=10,command=lambda: self.set_color("white"))
        eraser_btn.grid(row=0,column=7)
        clear_btn = Button(self,text="clear",width=10,command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0,column=8)


        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=1, column=1, padx=6)
        one_btn = Button(self, text="1", width=10, command=lambda: self.set_brush_size(1))
        one_btn.grid(row=1, column=2)
        two_btn = Button(self, text="2", width=10, command=lambda: self.set_brush_size(2))
        two_btn.grid(row=1, column=3)
        five_btn = Button(self, text="5", width=10, command=lambda: self.set_brush_size(5))
        five_btn.grid(row=1, column=4)
        seven_btn = Button(self, text="7", width=10, command=lambda: self.set_brush_size(7))
        seven_btn.grid(row=1, column=4)
        ten_btn = Button(self, text="10", width=10, command=lambda: self.set_brush_size(10))
        ten_btn.grid(row=1, column=5)
        twenty_btn = Button(self, text="20x", width=10, command=lambda: self.set_brush_size(20))
        twenty_btn.grid(row=1, column=6)
        fifty_btn = Button(self, text="50x", width=10, command=lambda: self.set_brush_size(50))
        fifty_btn.grid(row=1, column=7)
root = Tk()
root.geometry("2000x1000+300+300")
app = Paint(root)
root.mainloop()