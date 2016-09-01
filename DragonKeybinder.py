import libtcodpy
import DragonKeys
from Panel import Panel
from Console import Console


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
temp = 'Save As'
BTN['SAVE_AS'] = Panel(BTN['LOAD'].x2 + 1, 0, len(temp) + 2, 3, border=True)
BTN['SAVE_AS'].write(1, 1, temp)
temp = ''.ljust(SCREEN_WIDTH - BTN['SAVE_AS'].x2 - 3)
BTN['NAME'] = Panel(BTN['SAVE_AS'].x2 + 1, 0, len(temp) + 2, 3, border=True)
BTN['NAME'].write(1, 1, temp)
temp = 'Add Binding'
BTN['ADD_BIND'] = Panel(0, SCREEN_HEIGHT - 3,
                        len(temp) + 2, 3, border=True)
BTN['ADD_BIND'].write(1, 1, temp)
temp = 'Edit Binding'
BTN['EDIT_BIND'] = Panel(BTN['ADD_BIND'].x2 + 1, SCREEN_HEIGHT - 3,
                         len(temp) + 2, 3, border=True)
BTN['EDIT_BIND'].write(1, 1, temp)
temp = 'Remove Binding'
BTN['REM_BIND'] = Panel(BTN['EDIT_BIND'].x2 + 1, SCREEN_HEIGHT - 3,
                        len(temp) + 2, 3, border=True)
BTN['REM_BIND'].write(1, 1, temp)
BTN['SCROLL_UP'] = Panel(SCREEN_WIDTH - 1, 3, 1, 1)
BTN['SCROLL_UP'].write(0, 0, unichr(30))
BTN['SCROLL_DOWN'] = Panel(SCREEN_WIDTH - 1, 2 + TEXT_HEIGHT, 1, 1)
BTN['SCROLL_DOWN'].write(0, 0, unichr(31))
textpanel = Panel(0, 3, TEXT_WIDTH, TEXT_HEIGHT, border=True)
workpanel = Panel(1, 1, TEXT_WIDTH - 2, TEXT_HEIGHT - 2)
bindingspanel = Panel(0, 0, TEXT_WIDTH - 2, 1)
scrollpanel = Panel(SCREEN_WIDTH - 1, 4, 1, SCREEN_HEIGHT - 8)
mouse = libtcodpy.Mouse()
key = libtcodpy.Key()
toprow = 0
selected = False


def windowpanel(x, y, w, h, title, bf=0.0):
    blank = Panel(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    blank.blit(bfade=bf)
    window = Panel(x, y, w, h)
    window.write(1, 1, title)
    titlelength = len(title) + 2
    titleheight = len(title.split('\n')) + 2
    window.rect(0, 0, titlelength, titleheight, False)
    window.rect(0, titleheight - 1, w, h - titleheight + 1, False)
    window.write(0, titleheight - 1, unichr(195))
    window.write(titlelength - 1, titleheight - 1, unichr(193))
    window.blit()
    con.flush
    return window


def dataentry(title, x=20, y=20, w=40, h=5):
    datapanel = windowpanel(x, y, w, h, title, 0.7)
    datakey = libtcodpy.console_wait_for_keypress(True)
    newdata = ''
    while (datakey.vk != libtcodpy.KEY_ENTER and
           datakey.vk != libtcodpy.KEY_KPENTER):
        if (datakey.vk == libtcodpy.KEY_CHAR or
                datakey.vk == libtcodpy.KEY_SPACE):
            if len(newdata) < w - 2:
                newdata = newdata + chr(datakey.c)
                datapanel.write(1, 3, newdata)
        elif datakey.vk == libtcodpy.KEY_BACKSPACE:
            newdata = newdata[:-1]
            datapanel.write(len(newdata) + 1, 3, ' ')
        elif datakey.vk == libtcodpy.KEY_ESCAPE:
            return False
        datapanel.blit(bfade=0.7)
        con.flush
        datakey = libtcodpy.console_wait_for_keypress(True)
    return newdata


def msg(title, message, x=20, y=20, w=40, h=5):
    errorpanel = windowpanel(x, y, w, h, title, 0.7)
    errorpanel.write(1, 3, message)
    errorpanel.blit()
    con.flush
    return libtcodpy.console_wait_for_keypress(True)


def buttonpressed(name):
    if name == 'NEW':
        newname = dataentry('New Name')
        if newname:
            defaultoutput = dataentry('DEFAULT Output')
            if defaultoutput:
                binding.new(newname, defaultoutput)
    elif name == 'LOAD':
        loadpath = dataentry('Path of file to Load')
        if loadpath:
            binding.load(loadpath)
    elif name == 'SAVE_AS':
        newname = dataentry('Save As')
        if newname:
            binding.save_as(newname)
    elif name == 'ADD_BIND':
        newbind = msg('Enter Key to Bind',
                      'Please press the key you want to bind')
        if newbind.vk == libtcodpy.KEY_CHAR:
            newbind = chr(newbind.c)
        else:
            newbind = str(newbind.vk)
        if newbind in binding.dict:
            msg('Duplicate Key',
                'An output already exists for that keypress', w=44)
        else:
            newoutput = dataentry('Enter Output Now')
            if newoutput:
                binding.add_specified_binding(newbind, newoutput)
                binding.save()


while not con.is_window_closed:
    con.clear
    workpanel.clear
    textpanel.clear
    scrollpanel.clear
    bindingspanel.clear
    libtcodpy.sys_check_for_event(libtcodpy.EVENT_KEY_PRESS |
                                  libtcodpy.EVENT_MOUSE,
                                  key, mouse)
    bindingtxt = ''
    tempbindlist = []
    for bind, output in binding.dict.iteritems():
        if bindingtxt:
            bindingtxt = bindingtxt + '\n'
        if selected:
            if output == selected[0] and bind == selected[1]:
                bindingtxt = bindingtxt + '> '
        bindingtxt = bindingtxt + output + ': ' + bind
        tempbindlist.append((output, bind))
    bindheight = len(bindingtxt.split('\n'))
    if bindheight != bindingspanel.panelheight:
        bindingspanel = Panel(0, 0, TEXT_WIDTH - 2, bindheight)
    bindingspanel.write(0, 0, bindingtxt)
    if binding.active:
        BTN['NAME'].write(1, 1, binding.active_bindings.ljust(
            SCREEN_WIDTH - BTN['SAVE_AS'].x2 - 3))
    pressed = False
    for name, value in BTN.iteritems():
        if binding.active or (name == 'NEW' or name == 'LOAD'):
            if value.inside(mouse.cx, mouse.cy) and name != 'NAME':
                value.blit(ffade=0.7)
                if mouse.lbutton_pressed:
                    pressed = name
            else:
                value.blit()
    if workpanel.inside(mouse.cx, mouse.cy - 3):
        py = mouse.cy - 4
        if py <= bindheight:
            if mouse.lbutton_pressed:
                selected = tempbindlist[py + toprow]

    bindingspanel.blit(dst=workpanel.body, ydst=toprow)
    workpanel.blit(dst=textpanel.body)
    textpanel.blit()
    scrollpanel.blit()
    con.flush
    if pressed:
        buttonpressed(pressed)
