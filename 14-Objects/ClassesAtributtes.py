class PhoneFactory():
    branch = "Nokia"
    memory = 16
    space = 256

    def getBranch(self):
        return self.branch
    
    def getTimeToProcess(self, totalImages):
        return self.memory/totalImages

phone = PhoneFactory()
print (phone.branch)    
print (phone.getBranch())    
print ("Time to process: {}".format(phone.getTimeToProcess(4)))  