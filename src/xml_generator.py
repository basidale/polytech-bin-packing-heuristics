from lxml.etree import ElementTree, Element, SubElement, Comment, tostring

class XMLGenerator:
    def __init__(self, simulation):
        self.simulation = simulation
        self.top = Element('execution',
                           { 'algorithm' : self.simulation.algorithm.NAME })
        self.stepNo = 0
        
    def generate(self, outputFilePath):
        self.generateState()

        while not self.simulation.isCompleted():
            self.simulation.step()
            self.stepNo += 1
            self.generateState()

        tree = ElementTree(self.top)
        tree.write(outputFilePath, pretty_print=True)
        #print(tostring(self.top, pretty_print=True).decode())        
        
        #step = SubElement(top, 'step')
    
    def generateState(self):
        step = SubElement(self.top, 'step')

        numeroElement = SubElement(step, 'numero')
        numeroElement.text = str(self.stepNo)
        
        remaining = SubElement(step, 'remaining')
        remaining.text = str(len(self.simulation.itemList))
        
        item = self.simulation.currentItem
        
        if item:
            itemsize = SubElement(step, 'item-size')
            itemsize.text = str(self.simulation.currentItem.size)
        
        bins = SubElement(step, 'bins')
        for index, b in enumerate(self.simulation.bins):
            binElement = SubElement(bins, 'bin')
            
            indexElement = SubElement(binElement, 'index')
            indexElement.text = str(index)
            
            capacity = SubElement(binElement, 'capacity')
            capacity.text = str(b.capacity)
            
            loading = SubElement(binElement, 'loading')
            loading.text = str(b.loading())
            
