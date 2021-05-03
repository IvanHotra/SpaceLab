class BuilderPC:
    def __init__(self,graphics = None,processor = None,ROM = None, RAM = None):
        self.graphics = graphics
        self.processor = processor
        self.ROM = ROM
        self.RAM = RAM
        self.spec = []
    def putGraphics(self):
        self.spec.append(self.graphics)
    def putProcessor(self):
        self.spec.append(self.processor)
    def putRAM(self):
        self.spec.append(self.RAM)
    def putROM(self):
        self.spec.append(self.ROM)
    def __repr__(self):
        print('Configuratin is %s' % [x for x in self.spec])

MAC_PRO = BuilderPC('vega64','inter7700k','sumsungSSD','16gbDDR4')
MAC_PRO.putGraphics()
MAC_PRO.putProcessor()
MAC_PRO.putROM()
MAC_PRO.putRAM()
print(MAC_PRO.spec)
print(MAC_PRO)
