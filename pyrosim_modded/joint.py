from pyrosim_modded.commonFunctions import Save_Whitespace

class JOINT: 

    def __init__(self,name,parent,child,type,position, axis, limit):

        self.name = name

        self.parent = parent

        self.child  = child

        self.type   = type

        self.position = position

        self.depth = 1

        self.axis = axis

        self.limit = limit

    def Save(self,f):

        Save_Whitespace(self.depth,f)
        f.write('<joint name="' + self.name + '" type="' + self.type + '">' + '\n')

        Save_Whitespace(self.depth,f)
        f.write('   <parent link="' + self.parent + '"/>' + '\n')

        Save_Whitespace(self.depth,f)
        f.write('   <child  link="' + self.child  + '"/>' + '\n')

        Save_Whitespace(self.depth,f)
        originString = str(self.position[0]) + " " + str(self.position[1]) + " " + str(self.position[2])
        f.write('   <origin rpy="0 0 0" xyz="' + originString + '" />\n')

        Save_Whitespace(self.depth,f)
        axis_string = str(self.axis[0]) + " " + str(self.axis[1]) + " " + str(self.axis[2])
        f.write('   <axis xyz="' + axis_string + '"/>\n')

        Save_Whitespace(self.depth,f)
        f.write('   <limit effort="' + str(self.limit[0]) + '" lower="' + str(self.limit[1]) + '" upper="' + str(self.limit[2]) + '" velocity="' + str(self.limit[3]) + '"/>\n')

        Save_Whitespace(self.depth,f)
        f.write('</joint>' + '\n')

