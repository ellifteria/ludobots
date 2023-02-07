import pyrosim_modded.commonFunctions as commonFunctions

class MODEL:

    def __init__(self,modelName,pos):

        self.depth = 1

        self.pos = pos

        self.modelName = modelName

    def Save_Start_Tag(self,f):

        commonFunctions.Save_Whitespace(self.depth,f)

        f.write('<model name="' + self.modelName + '">\n')

        commonFunctions.Save_Whitespace(self.depth,f)

        pose = str(self.pos[0]) + ' ' + str(self.pos[1]) + ' ' + str(self.pos[2])

        if len(self.pos) == 4 and self.pos[3] == 'static':
             f.write('    <pose>' + pose + ' 0 0 0 </pose>\n        <static>true</static>\n')
        else:
            f.write('    <pose>' + pose + ' 0 0 0 </pose>\n')

    def Save_End_Tag(self,f):

        commonFunctions.Save_Whitespace(self.depth,f)

        f.write("</model>\n")
