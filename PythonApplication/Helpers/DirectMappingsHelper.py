from py_linq import Enumerable
from Helpers.FileHelper import FileHelperObject
import re
import pathlib


class DirectMappingsObject:
    """description of class"""
    global fileName
    def __init__(self):
        print('Intialized DirectMappings helper')
        global fileName
        global yamlConfigs
        global fileHelper         
        fileHelper=FileHelperObject()
        yamlConfigs = fileHelper.ReadYAMLFile()
        for yamlConfig in yamlConfigs:
            print(yamlConfig)
    
   #Process mappings
    def ProcessMappings(self,inputFile):
        print("Map Started")   
        self.fileName=pathlib.Path(inputFile).stem
        fileContentLines = fileHelper.ReadFileContentLines(inputFile)
        self.ProcessReplacements(fileContentLines)

    #Process to replace direct mappings
    def ProcessReplacements(self,fileContentLines):     
        resultContents=dict()
        my_collection = Enumerable(fileContentLines)       
        for index, line in enumerate(fileContentLines):
            for keyConfig,valueConfig in yamlConfigs.items():     
                  if len(line)!=0 and line !="\n":
                    resultContent=self.PrepareReplacements(keyConfig,valueConfig,line)         
                    resultContents[index]=resultContent
        self.PrepareScripts(resultContents)
    
    #Prepare to replace direct mappings in all possible ways
    def PrepareReplacements(self,keyConfig,valueConfig,lineContent):
         resultContent=re.sub(keyConfig, valueConfig, lineContent)       
         return resultContent;

    #Prepare scripts and generate output file
    def PrepareScripts(self,resultContents):
        resultString=""
        for index,line in resultContents.items():          
            resultString=resultString+line+"\n"
        fileHelper.CreateFile(self.fileName,resultString);

   
         


           




