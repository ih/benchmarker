import subprocess
#import os.system
import time
import pdb
class Language:
    def __init__(self,prefix="",suffix=""):
        self.prefix = prefix
        self.suffix = suffix

    def run(self,executable):
        myargs=[self.prefix+executable+self.suffix,""]
#        pdb.set_trace()
        subprocess.Popen(myargs, shell=True)

haskell = Language("./")
python = Language("python ",".py")
c = Language("./")
languages = [haskell,python]

def bench(executable, iterations):
    """String -> Int -> File; runs executable iterations number of times for different languages then outputs the execution times into a file"""
    for language in languages:

        for i in range(iterations):
            start_time = time.time()
            language.run(executable)
            end_time = time.time() - start_time
            print end_time, "seconds"
bench("run_hello",50)

        
        
