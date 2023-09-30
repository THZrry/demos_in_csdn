WIDTH = 2160
HEIGHT = 1440
# dll版
import ctypes
dll = ctypes.cdll.LoadLibrary("_c_grab.dll")
dll._init()
dll._switch_window(0)
dll._set_grab(WIDTH,HEIGHT)
# python移植版
import _py_grab as pdll
pdll._init()
pdll._switch_window(0)
pdll._set_grab(WIDTH,HEIGHT)
# 对照：mss
import mss

def dll_example():
    _grab_with_mouse = dll._grab_with_mouse
    _getdata = dll._getdata
    st = ctypes.create_string_buffer(WIDTH*HEIGHT*4)

    _grab_with_mouse(0,0,WIDTH,HEIGHT,0,0)
    _getdata(st,WIDTH,HEIGHT)
    return bytes(st)

def pdll_example():
    _grab_with_mouse = pdll._grab_with_mouse
    _getdata = pdll._getdata
    st = ctypes.create_string_buffer(WIDTH*HEIGHT*4)

    _grab_with_mouse(0,0,WIDTH,HEIGHT,0,0)
    _getdata(st,WIDTH,HEIGHT)
    return bytes(st)

def mss_example(cntr,end):
    " 不带鼠标指针 "
    aaa = 0
    m = mss.mss()
    mon = m.monitors[0]
    return m.grab(mon).raw

def raw_to_rgb(raw):
    rgb = bytearray(WIDTH*HEIGHT*3)
    rgb[::3] = bst[2::4]
    rgb[1::3] = bst[1::4]
    rgb[2::3] = bst[::4]
    return bytes(rgb)
"""
dll/pdll 使用
init完后， _grab截图，_grab_with_mouse带鼠标指针，_get_cursor获取鼠标指针，再用
  st = ctypes.create_string_buffer(WIDTH*HEIGHT*4)
  _getdata(st,WIDTH,HEIGHT)
获取raw(bgra)数据。
为保证性能， 每次修改分辨率需要手动调整，且只能从0，0开始（主要是懒得搞）
"""
