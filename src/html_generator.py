from lxml.etree import ElementTree, Element, SubElement, Comment, tostring
import subprocess

class HTMLGenerator:
    def generate(self, traceFilePath):
        f = open('output.html', 'w')
        subprocess.call(['xsltproc  transform.xml ', almost-worst-fit-example100.xml], stdout=f)

if __name__ == '__main__':
    traceFile = 'almost-worst-fit-example100.xml'
    filePath = filePath + '/../simulations/' + traceFile
    
    generator = HTMLGenerator()
    generator.generate(filePath)
