import libtcodpy
import DragonKeys
from Panel import Panel
from Console import Console


class txtbtn:
    def __init__(self, x, y, txt):
        self.x = x
        self.y = y
        self.w = len(txt) + 2
        self.h = 3
        self.panel = Panel(x, y, len(txt), 3, border=True)
        self.panel.write(1, 1, txt)

    @property
    def x2(self):
        return self.x + self.w

    @property
    def y2(self):
        return self.y + self.h

    def inside(self, mx, my):
        if mx >= self.x and mx <= self.x2 and my >= self.y and my <= self.y2:
            return True
        else:
            return False


binding = DragonKeys.KeyHandler()
binding.load('Keybindings/test.csv')
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
TEXT_WIDTH = SCREEN_WIDTH - 1
TEXT_HEIGHT = SCREEN_HEIGHT - 6
con = Console(SCREEN_WIDTH, SCREEN_HEIGHT, 'DragonKeybinder')
BTN = {}
temp = 'New'
BTN['NEW'] = Panel(0, 0, len(temp) + 2, 3, border=True)
BTN['NEW'].write(1, 1, temp)
temp = 'Load'
BTN['LOAD'] = Panel(BTN['NEW'].x2 + 1, 0, len(temp) + 2, 3, border=True)
BTN['LOAD'].write(1, 1, temp)
temp = 'Save'
BTN['SAVE'] = Panel(BTN['LOAD'].x2 + 1, 0, len(temp) + 2, 3, border=True)
BTN['SAVE'].write(1, 1, temp)
temp = 'Save As'
BTN['SAVE_AS'] = Panel(BTN['SAVE'].x2 + 1, 0, len(temp) + 2, 3, border=True)
BTN['SAVE_AS'].write(1, 1, temp)
temp = ''.ljust(SCREEN_WIDTH - BTN['SAVE_AS'].x2 - 3)
BTN['NAME'] = Panel(BTN['SAVE_AS'].x2 + 1, 0, len(temp) + 2, 3, border=True)
BTN['NAME'].write(1, 1, temp)
temp = 'Add Binding'
BTN['ADD_BIND'] = Panel(0, SCREEN_HEIGHT - 3, len(temp) + 2, 3, border=True)
BTN['ADD_BIND'].write(1, 1, temp)
temp = 'Remove Binding'
BTN['REM_BIND'] = Panel(BTN['ADD_BIND'].x2 + 1, SCREEN_HEIGHT - 3,
                        len(temp) + 2, 3, border=True)
BTN['REM_BIND'].write(1, 1, temp)
temp = 'New Output'
BTN['NEW_OUT'] = Panel(SCREEN_WIDTH - len(temp) - 2, SCREEN_HEIGHT - 3,
                       len(temp) + 2, 3, border=True)
BTN['NEW_OUT'].write(1, 1, temp)
textpanel = Panel(0, 3, TEXT_WIDTH, TEXT_HEIGHT, border=True)
workpanel = Panel(1, 1, TEXT_WIDTH - 2, TEXT_HEIGHT - 2)
bindingspanel = Panel(0, 0, TEXT_WIDTH - 2, 1)
scrollpanel = Panel(SCREEN_WIDTH - 1, 3, 1, SCREEN_HEIGHT - 6)
mouse = libtcodpy.Mouse()
key = libtcodpy.Key()
while not con.is_window_closed:
    con.clear
    workpanel.clear
    textpanel.clear
    scrollpanel.clear
    bindingspanel.clear
    scrollpanel.write(0, 0, '^')
    scrollpanel.write(0, TEXT_HEIGHT - 1, 'v')
    libtcodpy.sys_check_for_event(libtcodpy.EVENT_KEY_PRESS |
                                  libtcodpy.EVENT_MOUSE,
                                  key, mouse)
    bindingspanel.write(0, 0, str((mouse.cx, mouse.cy)))
    for name, value in BTN.iteritems():
        if value.inside(mouse.cx, mouse.cy) and name != 'NAME':
            bindingspanel.write(10, 0, name)
            value.blit(ffade=0.7)
            # if mouse.lbutton_pressed:
            #     buttonpressed(name)
        else:
            value.blit()
    bindingspanel.blit(dst=workpanel.body)
    workpanel.blit(dst=textpanel.body)
    textpanel.blit()
    scrollpanel.blit()
    con.flush
