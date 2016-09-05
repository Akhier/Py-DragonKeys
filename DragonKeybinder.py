# by Akhier Dragonheart
>>>>>>> refs/remotes/origin/stable
import libtcodpy
import DragonKeys
from Panel import Panel
from Console import Console


keydict = {
    '1': 'KEY_ESCAPE', '2': 'KEY_BACKSPACE', '3': 'KEY_TAB', '4': 'KEY_ENTER',
    '5': 'KEY_SHIFT', '6': 'KEY_CONTROL', '7': 'KEY_ALT', '8': 'KEY_PAUSE',
    '9': 'KEY_CAPSLOCK', '10': 'KEY_PAGEUP', '11': 'KEY_PAGEDOWN',
    '12': 'KEY_END', '13': 'KEY_HOME', '14': 'KEY_UP', '15': 'KEY_LEFT',
    '16': 'KEY_RIGHT', '17': 'KEY_DOWN', '18': 'KEY_PRINTSCREEN',
    '19': 'KEY_INSERT', '20': 'KEY_DELETE', '21': 'KEY_LWIN', '22': 'KEY_RWIN',
    '23': 'KEY_APPS', '24': 'KEY_0', '25': 'KEY_1', '26': 'KEY_2',
    '27': 'KEY_3', '28': 'KEY_4', '29': 'KEY_5', '30': 'KEY_6', '31': 'KEY_7',
    '32': 'KEY_8', '33': 'KEY_9', '34': 'KEY_KP0', '35': 'KEY_KP1',
    '36': 'KEY_KP2', '37': 'KEY_KP3', '38': 'KEY_KP4', '39': 'KEY_KP5',
    '40': 'KEY_KP6', '41': 'KEY_KP7', '42': 'KEY_KP8', '43': 'KEY_KP9',
    '44': 'KEY_KPADD', '45': 'KEY_KPSUB', '46': 'KEY_KPDIV', '47': 'KEY_KPMUL',
    '48': 'KEY_KPDEC', '49': 'KEY_KPENTER', '50': 'KEY_F1', '51': 'KEY_F2',
    '52': 'KEY_F3', '53': 'KEY_F4', '54': 'KEY_F5', '55': 'KEY_F6',
    '56': 'KEY_F7', '57': 'KEY_F8', '58': 'KEY_F9', '59': 'KEY_F10',
    '60': 'KEY_F11', '61': 'KEY_F12', '62': 'KEY_NUMLOCK',
    '63': 'KEY_SCROLLLOCK', '64': 'KEY_SPACE', '65': 'KEY_CHAR'}
binding = DragonKeys.KeyHandler()
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
    newkey = libtcodpy.console_wait_for_keypress(False)
    isshift = libtcodpy.console_is_key_pressed(libtcodpy.KEY_SHIFT)
    if isshift:
        newkey = libtcodpy.console_wait_for_keypress(True)
    return newkey


def buttonpressed(name, selected):
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
    elif name == 'EDIT_BIND' and selected:
        if selected[1] != 'DEFAULT':
            newbind = msg('Enter new Key to Bind',
                          'Please press the key you want to bind')
            if newbind.vk == libtcodpy.KEY_CHAR:
                newbind = chr(newbind.c)
            else:
                newbind = str(newbind.vk)
            binding.remove_specified_binding(selected[1])
            binding.add_specified_binding(newbind, selected[0])
            selected = (selected[0], newbind)
            binding.save()
        else:
            msg('Unable to Edit Default', 'As DEFAULT is a required binding' +
                ' of\nthe DragonKeys keyhandler to prevent\nproblems editing' +
                ' it with this program\nhas been disallowed\n(you could ' +
                'still edit the csv\nfile itself of course)', h=10)
            selected = False
    elif name == 'REM_BIND' and selected:
        if selected[1] != 'DEFAULT':
            binding.remove_specified_binding(selected[1])
            selected = False
            binding.save()
        else:
            msg('Unable to Delete Default', 'DEFAULT is a required part ' +
                'of the\nDragonKeys keyhandler so may not\nbe deleted', h=7)
            selected = False


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
        bindingtxt = bindingtxt + output + ': '
        if bind in keydict:
            bindingtxt = bindingtxt + keydict[bind]
        else:
            bindingtxt = bindingtxt + bind
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
        buttonpressed(pressed, selected)
