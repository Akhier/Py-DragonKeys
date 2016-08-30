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
    def y2(self):
        return self.y + self.h - 1


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
con = Console(SCREEN_WIDTH, SCREEN_HEIGHT, 'DragonKeybinder')
filepanel = Panel(0, 0, SCREEN_WIDTH, 3)
textpanel = Panel(0, 3, TEXT_WIDTH, TEXT_HEIGHT)
workpanel = Panel(1, 1, TEXT_WIDTH - 2, TEXT_HEIGHT - 2)
bindingspanel = Panel(0, 0, TEXT_WIDTH - 2, 1)
buttonpanel = Panel(0, SCREEN_HEIGHT - 3, SCREEN_WIDTH, 3)
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
    addbtntxt = 'Add Binding'
    btntxtx = 1
    buttonpanel.rect(0, 0, len(addbtntxt) + 2, 3, False)
    buttonpanel.write(btntxtx, 1, addbtntxt)
    btntxtx = btntxtx + len(addbtntxt) + 1
    rmvbtntxt = 'Remove Binding'
    buttonpanel.rect(btntxtx, 0, len(rmvbtntxt) + 2, 3, False)
    btntxtx = btntxtx + 1
    buttonpanel.write(btntxtx, 1, rmvbtntxt)
    newbtntxt = 'New Output'
    buttonpanel.rect(SCREEN_WIDTH - len(newbtntxt) - 2, 0,
                     len(newbtntxt) + 2, 3, False)
    buttonpanel.write(SCREEN_WIDTH - len(newbtntxt) - 1, 1, newbtntxt)
    scrollpanel.write(0, 0, '^')
    scrollpanel.write(0, TEXT_HEIGHT - 1, 'v')
    libtcodpy.sys_check_for_event(libtcodpy.EVENT_KEY_PRESS |
                                  libtcodpy.EVENT_MOUSE,
                                  key, mouse)
    bindingspanel.write(0, 0, str((mouse.cx, mouse.cy)))
    filepanel.blit()
    bindingspanel.blit(dst=workpanel.body)
    workpanel.blit(dst=textpanel.body)
    textpanel.blit()
    buttonpanel.blit()
    scrollpanel.blit()
    con.flush
