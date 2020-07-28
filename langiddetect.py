
import langid
import os
import glob

# Langid works as a single file with pretrained models 
# enough to get the job done
filepath = './responsive/**/*.jsp'

filesToAnalyze = glob.glob(filepath, recursive=True)

translation = []
for singleFile in filesToAnalyze:
    with open(singleFile, 'r') as f:
        for num, line in enumerate(f, start=1):
            if len(line) < 3:
                line =  line.ljust(3)
            detectedLine = langid.classify(line)
            if detectedLine[0] == 'de':
                infoLine = (line[:75] + (line[75:] and '..')).replace("\n", " ")
                basefile=os.path.basename( f.name)
                #+ " probability: "+str(detectedLine[1])+  
                print('File: ' + basefile + ' line: ' + infoLine + ' linenumber:' + str(num) +"\n")

  
