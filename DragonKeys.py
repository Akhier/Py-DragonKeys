import libtcodpy
import os.path
import csv


class KeyHandler:
    def __init__(self):
        self.bindingname = ''
        self.bindingpath = ''
        self.bindingdict = {}

    def clear(self):
        self.bindingname = ''
        self.bindingpath = ''
        self.bindingdict = {}

    def load(self, csvpath):
        if not os.path.isfile(csvpath):
            return False
        else:
            self.clear()
            outputdict = {}
            with open(csvpath) as file:
                reader = csv.reader(file)
                for entry in reader:
                    outputdict[entry[0]] = entry[1]
            self.bindingdict = outputdict
            self.bindingpath = csvpath
            csvpath = csvpath.replace('/', '.').replace('\\', '.')
            temp = csvpath.lower().split('.')
            self.bindingname = csvpath.split('.')[temp.index('csv') - 1]

    def save_as(self, name):
        path = name + '.csv'
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            for binding, output in self.bindingdict.iteritems():
                writer.writerow(binding, output)
            self.bindingname = name
            self.bindingpath = path

    def save(self):
        self.save_as(self.bindingname)

    def new(self, name, defaultouptut):
        self.clear()
        self.bindingdict['DEFAULT'] = defaultouptut
        self.save_as(name)


if __name__ == '__main__':
    from Panel import Panel
    from Console import Console
    SCREEN_WIDTH = 40
    SCREEN_HEIGHT = 25
    con = Console(SCREEN_WIDTH, SCREEN_HEIGHT, 'test')
    pan = Panel(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    testkey = getattr(libtcodpy, 'KEY_UP')
    print(testkey)
    if testkey == libtcodpy.KEY_UP:
        print('true')
    while not con.is_window_closed:
        con.clear
        key = libtcodpy.console_check_for_keypress(True)
        if key.vk != libtcodpy.KEY_NONE:
            if key.vk != libtcodpy.KEY_CHAR:
                pan.clear
                pan.write(0, 0, str(key.vk))
            else:
                pan.clear
                pan.write(0, 0, chr(key.c))
        if key.vk == libtcodpy.KEY_ESCAPE:
            break
        pan.blit()
        con.flush
    teststr = 'asdf/zxcv/test.csv'
    teststr = teststr.replace('/', '.').replace('\\', '.')
    temp = teststr.lower().split('.')
    print(teststr.split('.')[temp.index('csv') - 1])
    teststr = 'test.csv'
    teststr = teststr.replace('/', '.').replace('\\', '.')
    temp = teststr.lower().split('.')
    print(teststr.split('.')[temp.index('csv') - 1])
    teststr = 'asdf/zxcv/Test.CSV'
    teststr = teststr.replace('/', '.').replace('\\', '.')
    temp = teststr.lower().split('.')
    print(teststr.split('.')[temp.index('csv') - 1])
    teststr = 'TEST.CSV'
    teststr = teststr.replace('/', '.').replace('\\', '.')
    temp = teststr.lower().split('.')
    print(teststr.split('.')[temp.index('csv') - 1])
