#import langid
from langdetect import detect
from langdetect import detect_langs
import os
import glob

# Langid works as a single file with pretrained models 
# enough to get the job done
filepath = 'tags/**/*.tag'



filesToAnalyze = glob.glob(filepath, recursive=True)

translation = []
for singleFile in filesToAnalyze:
    with open(singleFile, 'r') as f:
        for num, line in enumerate(f, start=1):
            if len(line) < 3:
                line =  line.ljust(3)
            try:              
                detectedLine = detect_langs(line)
                detectedLang = detectedLine[0].lang
                prob = detectedLine[0].prob
                if detectedLang == 'de':
                    infoLine = (line[:100] + (line[100:] and '..')).replace("\n", " ")
                    basefile=os.path.basename( f.name)
                    #+ " probability: "+str(detectedLine[1])+  
                    print('File: ' + basefile + ' line: ' + infoLine + ' linenumber:' + str(num)  + ' probability:' + str(prob)+"\n" )
            except:
                pass 