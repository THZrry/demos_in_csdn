// simply taking screenshot in Windows platform
#include <windows.h>
#include <wingdi.h>

BITMAPINFO bmi;
HDC srcdc;
HDC memdc;
HGDIOBJ bmp;
CURSORINFO pci;
int _GRABMODE;

int _init(){
	bmi.bmiHeader.biSize = sizeof(BITMAPINFOHEADER);
	bmi.bmiHeader.biPlanes = 1;
	bmi.bmiHeader.biBitCount = 32;
	bmi.bmiHeader.biCompression = 0;
	bmi.bmiHeader.biClrUsed = 0;
	bmi.bmiHeader.biClrImportant = 0;
	pci.cbSize = sizeof(pci);
	_GRABMODE = SRCCOPY|CAPTUREBLT;
	return 1;
}

int _switch_window(HWND hwnd){
	srcdc = GetWindowDC(hwnd);
	memdc = CreateCompatibleDC(srcdc);
	return 1;
}

HICON _get_cursor_hicon(){
	if (GetCursorInfo(&pci)){
		return pci.hCursor;
	}
	return 0;
}

int _get_cursor(){
	bmi.bmiHeader.biWidth = 32;
	bmi.bmiHeader.biHeight= -32;
	bmp = CreateCompatibleBitmap(srcdc, 32, 32);
	SelectObject(memdc, bmp);
	return DrawIcon(memdc,0,0,_get_cursor_hicon());
}

int _set_grab(int width,int height){
	bmi.bmiHeader.biWidth = width;
	bmi.bmiHeader.biHeight= -height;
	bmp = CreateCompatibleBitmap(srcdc, width, height);
	SelectObject(memdc, bmp);
	return 1;
}

int _grab(int x, int y, int width, int height){
	return BitBlt(memdc,0,0,width,height,srcdc,x,y,_GRABMODE);
}

int _grab_with_mouse(int x, int y, int width, int height,int xsub, int ysub){
	_grab(x, y, width, height);
	HICON cur = _get_cursor_hicon();
	return DrawIcon(memdc,pci.ptScreenPos.x-xsub,pci.ptScreenPos.y-ysub,cur);
}

int _getdata(char data[],int width,int height){
	int bits = GetDIBits(memdc, bmp, 0, height, data, &bmi, DIB_RGB_COLORS);
	//DeleteObject(&bmp);
	return (bits == height);
}
