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

        outputFile = outputFile.split('.')[0] + '-animated.html'
        head = self.html.find('head')
        head.append(self.scriptElement('jquery.js'))
        head.append(self.scriptElement('animate.js'))
        self.write(outputFile)

    def scriptElement(self, path):
        script = Element('script')
        script.set('src', path)
        script.set('type', 'text/javascript')

        return script

    def write(self, outputFile):
        self.html.write(outputFile,
                        encoding='utf-8',
                        method='html',
                        pretty_print=True)        
        
        
if __name__ == '__main__':
    traceDirectory = sourcePath + '/../../simulations/'
    traces = [ 'almost-worst-fit-example100.xml',
               'best-fit-example100.xml',
               'first-fit-example100.xml',
               'next-fit-example100.xml',
               'worst-fit-example100.xml' ]

    for tracePath in traces:
        outputFile = sourcePath + '/target/' + tracePath.split('.')[0]
        generator = HTMLGenerator(traceDirectory + tracePath)
        generator.generate(outputFile)
