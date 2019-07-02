import os
import yaml

class FileHelperObject:
    """description of class"""
    def __init__(self):
        print('Intialized file helper')
        global base
        base=dict()
   
    def ReadYAMLFile(self):
        with open('Config/Mappings.yaml','r+') as yaml_file:
            yamldata = yaml.safe_load(yaml_file)            
            for key, value in yamldata.get('DIRECT_MAP').items():
                base[key]=value
        return base


    def ReadSourceFiles(self):
       return os.listdir('SourceFiles/')
    
    def ReadFileContent(self,inputFile):
       return open('SourceFiles/'+inputFile,'r')
    
    def ReadFileContentLines(self,inputFile):
        with open('SourceFiles/'+inputFile) as f:
             return f.readlines()

    def CreateFile(self,fileName,fileContent):
        f=open('GeneratedFiles/'+fileName+'.txt',"w+")
        f.write(fileContent)
        f.close()
      
   
       


