from lightshows.InstructionModel import Instruction
from lightshows.ReadInstructions import ReadInstructions


class ReadInstructionsImpl(ReadInstructions):

    faultyLines = []
    lineIter = 0
    listOfInstructions = []

    def getListOfInstructions(self,ds):  # returns a list of Instruction[command, start, finnish]

        turnOn = "turn on"
        turnOff = "turn off"
        toggle = "toggle"

        source = ds.getSourceData()

        with open (source) as myfile:
         for line in myfile:
            self.lineIter += 1
            if line.lower().startswith(turnOn):
                self.listOfInstructions.append(Instruction(turnOn,line.split()[2],line.split()[4])) # @TODO replace this hacky way?
            elif line.lower().startswith("turn off"):
                self.listOfInstructions.append(Instruction(turnOff,line.split()[2],line.split()[4]))
            elif line.lower().startswith("toggle"):
                self.listOfInstructions.append(Instruction(toggle, line.split()[1], line.split()[3]))
            else:
                self.faultyLines.append("Line " + str(self.lineIter))

    # #@ TODO handle errors with customised error class

        for err in self.faultyLines:
            print(err) #" TODO replace with log

        return self.listOfInstructions

