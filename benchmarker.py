import subprocess
#import os.system
import time
import pdb
import datetime
class Language:
    def __init__(self,name,prefix="",suffix=""):
        self.name = name
        self.prefix = prefix
        self.suffix = suffix
    def run(self,executable):
        myargs=[self.prefix+executable+self.suffix,""]
#        pdb.set_trace()
        subprocess.Popen(myargs, shell=True)

haskell = Language("haskell", "./")
python = Language("python","python ",".py")
c = Language("c","./")
languages = [c,python]

def bench(executable, iterations, languages):
    """String -> Int -> File; runs executable iterations number of times for different languages then outputs the execution times into a file"""
    outFile=createFile(executable)
    writeLanguageNames(outFile,languages)
    writeExecutionTimes(executable,outFile,languages,iterations)
    calculateStatistics(outFile)

def calculateStatistics(outFile):
    command = "R --no-restore --no-save --no-readline "+outFile.name+" graph.jpg <  statistics.R"
    subprocess.Popen(command, shell=True)
def createFile(executable):
    outFileName = executable
    return open(outFileName, 'w')

def writeLanguageNames(outFile,languages):
    for language in languages:
        outFile.write(language.name+' ')
    outFile.write('\n')

def writeExecutionTimes(executable,outFile,languages,iterations):
    for i in range(iterations):
        for language in languages:
            start_time = time.time()
            language.run(executable)
            end_time = time.time() - start_time
            outFile.write(str(end_time)+' ')
        outFile.write('\n')
    outFile.close()
bench("run_hello",10,languages)

        
        
