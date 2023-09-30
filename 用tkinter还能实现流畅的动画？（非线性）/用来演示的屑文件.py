import math
import time
import tkinter as tk
ANI_DUR = 11
ANIMATIONSPEED = 1
ALLOWANIMATION = 1
def animate1(start,end,duration,passed):
    " y=kx+b "
    return (passed/duration) * (end-start) + start

def animate2(start,end,duration,passed):
    x = passed / duration
    return start+(end-start)*(3*math.sin(x-5.7)-2)

def animate3(start,end,duration,passed):
    x = passed / duration
    return start+(end-start)*(math.sqrt(x))

def animate4(start,end,duration,passed):
    x = passed / duration
    return start+(end-start)*(x**3 - 0.3*x*math.sin(x*3.14))
def animate5(start,end,duration,passed):
    x = passed / duration
    return start+(end-start)*(x**2)
def animate6(start,end,duration,passed):
    x = passed / duration
    return start+(end-start)*(math.sin(x*3.14/2))

animate = animate3

class AnimateManager:
    def __init__(self,widget,duration,start,end,before,during,after,passtime=None,forceopen=0):
        self.widget = widget
        self._duration = duration
        self.start = start
        self.end = end
        # functions
        self.before = before
        self.during = during
        self.after = after
        # the pass time of two frames
        if passtime:
            self.passtime = passtime
        # the class saves the state of animating
        if not hasattr(widget,"animate"):
            self.widget.animate = 0
        self.func = animate
        self.func_extra = []
        self.forceopen = forceopen
        self._stopped = 0
        self.framesnum = 0
    def start_animate(self,nextani=None):
        " start an animation with default settings "
        # when there's a animate playing, set 0 to break it
        widget = self.widget
        if widget.animate:
            widget.animate = 0
        else:
            widget.animate = 1
        # prepare
        self.start_time = time.time()
        self.passed = 0
        self.duration = self._duration / ANIMATIONSPEED
        self.before()
        if ALLOWANIMATION or self.forceopen:
            self.widget.after(ANI_DUR,self.loop)
        else:
            self.during(self.end)
            self.after()
    def loop(self):
        " the loop of animation "
        if self._stopped:
            self._stopped = 0
            return
        widget = self.widget
        if widget.animate == 0:
            widget.animate = 1
            self.after()
            return
        passed = time.time() - self.start_time
        if passed >= self.duration:
            widget.animate = 0
            self.during(self.end)
            self.after()
            return
        self.framesnum += 1
        var = self.func(self.start,self.end,self.duration,passed,*self.func_extra)
        self.during(var)
        widget.after(ANI_DUR,self.loop)
    def stop(self):
        self._stopped = 1

def place_animate(wid,t,xs,xe,ys,ye,reverse=False,wait=0,kw=None):
    if not kw:
        kw = {}
    def during(var):
        wid.place(x=(xe-xs)*var+xs,y=(ye-ys)*var+ys,**kw)
    def after():
        wid.place(x=xe,y=ye,**kw)
    am = AnimateManager(wid,t,0,1,lambda:None,during,after)
    if reverse:
        am = AnimateManager(wid,t,1,0,lambda:None,during,after)
    if wait == 0:
        am.start_animate()
    else:
       wid.after(wait,am.start_animate)
    return am.stop

if __name__ == "__main__":
    def sttc():
        for am in (am1, am2, am3, am4, am5, am6):
            am.start_animate()
    def stpc():
        for am in (am1, am2, am3, am4, am5, am6):
            am.stop()
    root = tk.Tk()
    root.title("tkinter的动画")
    root.geometry("800x600")
    dur = 0.5
    stt = tk.Button(root,text="开始动画",command=sttc)
    stp = tk.Button(root,text="结束动画",command=stpc)
    stt.place(x=20,y=20,width=120,height=40)
    stp.place(x=160,y=20,width=120,height=40)
    #
    tk.Label(root,text="线性动画").place(x=20,y=80,width=120,height=40)
    frm1 = tk.Frame(root,bg="yellow")
    frm1.place(x=160,y=80,width=600,height=40)
    block1 = tk.Frame(frm1,bg="red")
    block1.place(x=0,y=0,width=40,height=40)
    am1 = AnimateManager(block1,dur,0,560,lambda:None,lambda x:block1.place(x=x),lambda:None)
    am1.func = animate1
    #
    tk.Label(root,text="非线性动画1").place(x=20,y=130,width=120,height=40)
    frm2 = tk.Frame(root,bg="yellow")
    frm2.place(x=160,y=130,width=600,height=40)
    block2 = tk.Frame(frm2,bg="red")
    block2.place(x=0,y=0,width=40,height=40)
    am2 = AnimateManager(block2,dur,0,560,lambda:None,lambda x:block2.place(x=x),lambda:None)
    am2.func = animate2
    #
    tk.Label(root,text="非线性动画2").place(x=20,y=180,width=120,height=40)
    frm3 = tk.Frame(root,bg="yellow")
    frm3.place(x=160,y=180,width=600,height=40)
    block3 = tk.Frame(frm3,bg="red")
    block3.place(x=0,y=0,width=40,height=40)
    am3 = AnimateManager(block3,dur,0,560,lambda:None,lambda x:block3.place(x=x),lambda:None)
    am3.func = animate3
    #
    tk.Label(root,text="非线性动画3").place(x=20,y=230,width=120,height=40)
    frm4 = tk.Frame(root,bg="yellow")
    frm4.place(x=160,y=230,width=600,height=40)
    block4 = tk.Frame(frm4,bg="red")
    block4.place(x=0,y=0,width=40,height=40)
    am4 = AnimateManager(block4,dur,0,560,lambda:None,lambda x:block4.place(x=x),lambda:None)
    am4.func = animate4
    #
    tk.Label(root,text="非线性动画4").place(x=20,y=280,width=120,height=40)
    frm5 = tk.Frame(root,bg="yellow")
    frm5.place(x=160,y=280,width=600,height=40)
    block5 = tk.Frame(frm5,bg="red")
    block5.place(x=0,y=0,width=40,height=40)
    am5 = AnimateManager(block5,dur,0,560,lambda:None,lambda x:block5.place(x=x),lambda:None)
    am5.func = animate5
    #
    tk.Label(root,text="非线性动画5").place(x=20,y=330,width=120,height=40)
    frm6 = tk.Frame(root,bg="yellow")
    frm6.place(x=160,y=330,width=600,height=40)
    block6 = tk.Frame(frm6,bg="red")
    block6.place(x=0,y=0,width=40,height=40)
    am6 = AnimateManager(block6,dur,0,560,lambda:None,lambda x:block6.place(x=x),lambda:None)
    am6.func = animate6
    #
    root.mainloop()
