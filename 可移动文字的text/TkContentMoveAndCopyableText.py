import tkinter as tk
import sys
class TkContentMoveAndCopyableText(tk.Text):
    "取这个名字纯粹是用来恶心人的"
    def __init__(self,*a,**b):
        super().__init__(*a,**b)
        self.content = ""
        self.draging = False
        self.ctrl = False
        self.bind("<KeyPress>",self.ctrldown,1)
        self.bind("<KeyRelease>",self.ctrlup,1)
        self.bind("<B1-Motion>",self.handledrag,1)
        self.bind("<Button-1>",self.handledown,1)
        self.bind("<ButtonRelease-1>",self.handleup,1)
    def ctrlup(self,e):
        if e.keycode == 17:
            self.ctrl = False
    def ctrldown(self,e):
        if e.keycode == 17:
            self.ctrl=True
    def handledown(self,e):
        try:
            if self.insel(e):
                self.content = self.get("sel.first","sel.last")
                self.sel = (self.index("sel.first") , self.index("sel.last"))
                return "break"
        except:
            self.content = ""
    def handledrag(self,e):
        if self.content:
                self.draging = True
                self.mark_set("insert","@%d,%d"%(e.x,e.y))
                return "break"
    def handleup(self,e):
        if self.draging:
            if not self.ctrl:
                self.delete(*self.sel)
            self.insert("insert",self.content)
            self.draging = False
            self.content = ""
        else:
            if self.content:
                self.tag_remove("sel","1.0","end")
                self.content = ""
                self.mark_set("insert","@%d,%d"%(e.x,e.y))
    def insel(self,e):
        "其实可以用text.compare代替，判断insert标记是否在sel标签里"
        try:
            y1,x1 = map(int,self.index("sel.first"       ).split("."))
            y2,x2 = map(int,self.index("@%d,%d"%(e.x,e.y)).split("."))
            y3,x3 = map(int,self.index("sel.last"        ).split("."))
            if y3 > y2 > y1:
                return 1
            if y2 == y1 and x2 > x1:
                return 1
            elif y2 == y3 and x2 < x3:
                return 1
        except:
            pass
def test():
    root = tk.Tk()
    root.title("TextPlus")
    TextPlus().pack(expand=1,fill="both")
    root.mainloop()
if __name__ == "__main__":
    test()
