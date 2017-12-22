from lxml.etree import ElementTree, Element, SubElement, Comment, tostring, parse, XSLT
import lxml.html as html
import subprocess
import os

sourcePath = os.path.dirname(os.path.realpath(__file__))

class HTMLGenerator:
    transformationDefinition = sourcePath + '/transform.xml'
    
    def __init__(self, traceFilePath):
        xslt = parse(HTMLGenerator.transformationDefinition)
        self.trace = parse(traceFilePath)
        self.transform = XSLT(xslt)
        self.html = None
        
    def generate(self, outputFile):
        self.html = self.transform(self.trace)
        self.html.write(outputFile, encoding='utf-8', method='html', pretty_print=True)
        self.write(outputFile)

    def write(self, outputFile):
        self.html.write(outputFile,
                        encoding='utf-8',
                        method='html',
                        pretty_print=True)        
        
        
if __name__ == '__main__':
    traceDirectory = sourcePath + '/../../simulations/'
    traces = [ 'almost-worst-fit-exemple100.xml',
               'best-fit-exemple100.xml',
               'first-fit-exemple100.xml',
               'next-fit-exemple100.xml',
               'worst-fit-exemple100.xml',
               'almost-worst-fit-exemple500.xml', 
               'best-fit-exemple500.xml',         
               'first-fit-exemple500.xml',        
               'next-fit-exemple500.xml',         
               'worst-fit-exemple500.xml',        
               'almost-worst-fit-exemple1000.xml', 
               'best-fit-exemple1000.xml',         
               'first-fit-exemple1000.xml',        
               'next-fit-exemple1000.xml',         
               'worst-fit-exemple1000.xml' ]

    for tracePath in traces:
        outputFile = sourcePath + '/target/' + tracePath.split('.')[0] + '.html'
        generator = HTMLGenerator(traceDirectory + tracePath)
        generator.generate(outputFile)
