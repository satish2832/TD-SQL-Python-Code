from Helpers.FileHelper import FileHelperObject
from Helpers.DirectMappingsHelper import DirectMappingsObject




# Read file from folder
def InitializeWithFile():
    fileHelper=FileHelperObject() 
    mappingHelper=DirectMappingsObject()
    inputFiles=fileHelper.ReadSourceFiles()
    for inputFile in inputFiles:
        print(inputFile)
        mappingHelper.ProcessMappings(inputFile)

InitializeWithFile()



