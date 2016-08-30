import libtcodpy
import DragonKeys
from Panel import Panel
from Console import Console


class txtbtn:
    def __init__(self, x, y, txt):
        self.x = x
        self.y = y
        self.txt = txt
        self.h = 3
        self.ry = y

    @property
    def tx(self):
        return self.x + 1

    @property
    def ty(self):
        return self.y + 1

    @property
    def w(self):
        return len(self.txt) + 2

    @property
    def x2(self):
        return self.x + self.w - 1

    @property
    def ry2(self):
        return self.ry + self.h - 1

    def inside(self, mx, my):
        if mx >= self.x and mx <= self.x2 and my >= self.ry and my <= self.ry2:
            return True
        else:
            return False


binding = DragonKeys.KeyHandler()
binding.load('Keybindings/test.csv')
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
TEXT_WIDTH = SCREEN_WIDTH - 1
TEXT_HEIGHT = SCREEN_HEIGHT - 6
BTN = {}
BTN['NEW'] = txtbtn(0, 0, 'New')
BTN['LOAD'] = txtbtn(BTN['NEW'].x2 + 1, 0, 'Load')
BTN['SAVE'] = txtbtn(BTN['LOAD'].x2 + 1, 0, 'Save')
BTN['SAVE_AS'] = txtbtn(BTN['SAVE'].x2 + 1, 0, 'Save As')
BTN['ADD_BIND'] = txtbtn(0, 0, 'Add Binding')
BTN['REM_BIND'] = txtbtn(BTN['ADD_BIND'].x2 + 1, 0, 'Remove Binding')
newouttxt = 'New Output'
BTN['NEW_OUT'] = txtbtn(SCREEN_WIDTH - len(newouttxt) - 2, 0, newouttxt)
con = Console(SCREEN_WIDTH, SCREEN_HEIGHT, 'DragonKeybinder')
filepanel = Panel(0, 0, SCREEN_WIDTH, 3)
textpanel = Panel(0, 3, TEXT_WIDTH, TEXT_HEIGHT)
workpanel = Panel(1, 1, TEXT_WIDTH - 2, TEXT_HEIGHT - 2)
bindingspanel = Panel(0, 0, TEXT_WIDTH - 2, 1)
buttonpanel = Panel(0, SCREEN_HEIGHT - 3, SCREEN_WIDTH, 3)
BTN['ADD_BIND'].ry += buttonpanel.y
BTN['REM_BIND'].ry += buttonpanel.y
BTN['NEW_OUT'].ry += buttonpanel.y
scrollpanel = Panel(SCREEN_WIDTH - 1, 3, 1, SCREEN_HEIGHT - 6)
mouse = libtcodpy.Mouse()
key = libtcodpy.Key()
while not con.is_window_closed:
    con.clear
    filepanel.clear
    workpanel.clear
    textpanel.clear
    buttonpanel.clear
    scrollpanel.clear
    bindingspanel.clear
    filepanel.rect(BTN['NEW'].x, BTN['NEW'].y,
                   BTN['NEW'].w, BTN['NEW'].h, False)
    filepanel.write(BTN['NEW'].tx, BTN['NEW'].ty, BTN['NEW'].txt)
    filepanel.rect(BTN['LOAD'].x, BTN['LOAD'].y,
                   BTN['LOAD'].w, BTN['LOAD'].h, False)
    filepanel.write(BTN['LOAD'].tx, BTN['LOAD'].ty, BTN['LOAD'].txt)
    if binding.active:
        filepanel.rect(BTN['SAVE'].x, BTN['SAVE'].y,
                       BTN['SAVE'].w, BTN['SAVE'].h, False)
        filepanel.write(BTN['SAVE'].tx, BTN['SAVE'].ty, BTN['SAVE'].txt)
        filepanel.rect(BTN['SAVE_AS'].x, BTN['SAVE_AS'].y,
                       BTN['SAVE_AS'].w, BTN['SAVE_AS'].h, False)
        filepanel.write(BTN['SAVE_AS'].tx, BTN[
                        'SAVE_AS'].ty, BTN['SAVE_AS'].txt)
        filepanel.rect(BTN['SAVE_AS'].x2 + 1, 0,
                       SCREEN_WIDTH - BTN['SAVE_AS'].x2 - 1, 3, False)
        filepanel.write(BTN['SAVE_AS'].x2 + 2, 1, binding.active_bindings)
    else:
        filepanel.rect(BTN['LOAD'].x2 + 1, 0,
                       SCREEN_WIDTH - BTN['LOAD'].x2, 3, False)
    textpanel.rect(0, 0, TEXT_WIDTH, TEXT_HEIGHT, False)
    buttonpanel.rect(BTN['ADD_BIND'].x, BTN['ADD_BIND'].y,
                     BTN['ADD_BIND'].w, BTN['ADD_BIND'].h, False)
    buttonpanel.write(BTN['ADD_BIND'].tx, BTN['ADD_BIND'].ty,
                      BTN['ADD_BIND'].txt)
    buttonpanel.rect(BTN['REM_BIND'].x, BTN['REM_BIND'].y,
                     BTN['REM_BIND'].w, BTN['REM_BIND'].h, False)
    buttonpanel.write(BTN['REM_BIND'].tx, BTN['REM_BIND'].ty,
                      BTN['REM_BIND'].txt)
    buttonpanel.rect(BTN['NEW_OUT'].x, BTN['NEW_OUT'].y,
                     BTN['NEW_OUT'].w, BTN['NEW_OUT'].h, False)
    buttonpanel.write(BTN['NEW_OUT'].tx, BTN['NEW_OUT'].ty,
                      BTN['NEW_OUT'].txt)
    scrollpanel.write(0, 0, '^')
    scrollpanel.write(0, TEXT_HEIGHT - 1, 'v')
    libtcodpy.sys_check_for_event(libtcodpy.EVENT_KEY_PRESS |
                                  libtcodpy.EVENT_MOUSE,
                                  key, mouse)
    bindingspanel.write(0, 0, str((mouse.cx, mouse.cy)))
    if BTN['NEW'].inside(mouse.cx, mouse.cy):
        bindingspanel.write(10, 0, 'Inside')
    filepanel.blit()
    bindingspanel.blit(dst=workpanel.body)
    workpanel.blit(dst=textpanel.body)
    textpanel.blit()
    buttonpanel.blit()
    scrollpanel.blit()
    con.flush
