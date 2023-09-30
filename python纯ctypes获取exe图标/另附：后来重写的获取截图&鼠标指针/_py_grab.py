"""
This is the python version of _c_grab.c
to win32-86 or arm64, i haven't compile
an avaliable version, so use this instead.

using an unofficial version of mss.windows.
"""
from _mss_windows import *
from ctypes.wintypes import HICON, LONG
import ctypes

user32 = ctypes.windll.user32
gdi32  = ctypes.windll.gdi32

HCURSOR = HICON
class POINT(Structure):
    _fields_ = [
        ('x', LONG),
        ('y', LONG),
    ]

class CURSORINFO(Structure):
    _fields_ = [
        ("cbSize",DWORD),
        ("flags", DWORD),
        ("hCursor", HCURSOR),
        ("ptScreenPos", POINT)
        ]

bmi = BITMAPINFO()
srcdc = HDC()
memdc = HDC()
bmp = HGDIOBJ()
pci = CURSORINFO()
_GRABMODE = SRCCOPY|CAPTUREBLT

def _init():
    global pci
    bmi.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    bmi.bmiHeader.biPlanes = 1
    bmi.bmiHeader.biBitCount = 32
    bmi.bmiHeader.biCompression = 0
    bmi.bmiHeader.biClrUsed = 0
    bmi.bmiHeader.biClrImportant = 0
    pci.cbSize = ctypes.sizeof(pci)
    return 1

def _switch_window(hwnd):
    global srcdc, memdc
    srcdc = user32.GetWindowDC(hwnd)
    memdc = gdi32.CreateCompatibleDC(srcdc)
    return 1

def _get_cursor_hicon():
    if user32.GetCursorInfo(ctypes.byref(pci)):
        return pci.hCursor
    return 0

def _get_cursor():
    global bmp
    bmi.bmiHeader.biWidth = 32
    bmi.bmiHeader.biHeight= -32
    bmp = gdi32.CreateCompatibleBitmap(srcdc, 32, 32)
    gdi32.SelectObject(memdc, bmp)
    return user32.DrawIcon(memdc,0,0,_get_cursor_hicon())

def _set_grab(width, height):
    global bmp
    bmp = gdi32.CreateCompatibleBitmap(srcdc, width, height)
    bmi.bmiHeader.biWidth = width
    bmi.bmiHeader.biHeight= -height
    gdi32.SelectObject(memdc, bmp)

def _grab(x, y, width, height):
    return gdi32.BitBlt(memdc,0,0,width,height,srcdc,x,y,_GRABMODE)

def _grab_with_mouse(x, y, width, height, xsub, ysub):
    _grab(x, y, width, height)
    cur = _get_cursor_hicon()
    return user32.DrawIcon(memdc, pci.ptScreenPos.x-xsub, pci.ptScreenPos.y-ysub, cur)

def _getdata(data, width, height):
    bits = gdi32.GetDIBits(memdc, bmp, 0, height, data, ctypes.byref(bmi), DIB_RGB_COLORS)
    #gdi32.DeleteObject(bmp)
    return (bits == height)
