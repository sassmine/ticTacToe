self.restartButton.clicked.connect(self.restartButtonTriggeredHandler)
        self.preferencesButton.clicked.connect(self.preferencesSelectButtonTriggeredHandler)

        self.pickleFileName = pickleFileNameDefault

        self.restoreSettings()

        if path.exists(self.pickleFileName):
            self.userPlayingWithMark, self.userWins, self.userLoses, self.gameInProgress, self.messageString, self.markLabelButton, self.spot, self.board, self.game = self.restoreGame()

        else:
            self.restartGame()

    def saveGame(self):
        saveItems = (self.winsCount, self.lossesCOunt)
        if self.appSettings.contains('pickleFileName'):
            with open(path.join(path.dirname(path.realpath(__file__)), self.appSettings.value('pickleFileName', type= str)), 'wb') as pickleFile:
                dump(saveItems, pickleFile)
        else:
            self.logger.critical("No pickle Filename")
    def saveSettings(self):
        radioButtonXDefault = False
        radioButtonODefault = False
        if self.appSettings.contains('radioButtonX'): #implement X
            self.radioButtonX = self.appSettings.value('radioButtonX', type=bool)
        else:
            self.radioButtonX = radioButtonXDefault
            self.appSettings.setValue('radioButtonX', self.radioButtonX)
        if self.appSettings.contains('radioButtonO'): #implement O
            self.radioButtonO = self.appSettings.value('radioButtonO', type=bool)
        else:
            self.radioButtonO = radioButtonODefault
            self.appSettings.setValue('radioButtonO', self.radioButtonO)
        if self.appSettings.contains('createLogFile'):
            self.createLogFile=appSettings.value('createLogFile',type=bool)
        else:
            self.createLogFile= logFileNameDefault
            self.appSettings.setValue('createLogFile', self.createLogFile)
    def restoreGame(self):
        if self.appSettings.contains('pickleFileName'):
            pickleFileName = path.join(path.dirname(path.realpath(__file__)), self.appSettings.value('pickleFileName', type=str)) #is this right?
            try:
                with open(pickleFileName, 'rb') as pickleFile:
                    return load(pickleFile)
            except FileNotFoundError as errorVal:
                print('errorVal')
        else:
            self.logger.critical("No pickle Filename")
    def restoreSettings(self):
        self.startingMarkChoice = self.appSettings.value('startingMarkChoice')
        self.createLogFile = self.appSettings.value('createLogFile')
        self.logFileName = self.appSettings.value('pickleFileName')
        return True


    def updateUI(self):
        for squareNumber in range(1,9):
            if self.square.isEmpty(squareNumber): #check if the squareNumber is empty
                self.buttonList[squareNumber - 1].setText("") #if it is make sure it has no mark
            elif self.square.getMark(squareNumber) == 1: #if the player is X and they mark the square then set the text to X
                self.buttonList[squareNumber - 1].setText("X")
            else:
                self.buttonList[squareNumber - 1].setText("O") #if the player is O and they mark the square then set the text to O
        self.winsLabel.setText("%i" % self.userWins) #set the users winsLabel to whatever their winCount is
        self.lossesLabel.setText("%i" % self.userLosses) #set the users lossesLabel to whatever their lossesCount is
        self.resultsLabel.setText(self.messageString) #set the resultsLabel to whatever the messageString is set to
        if self.userPlayingWithMark == 1: #if the user selects X, set the value to 1
            self.markLabelButton.setText("X")
        elif self.userPlayingWithMark == 2: #if the user select O, set the value to 2
            self.markLabelButton.setText("O")
        else:
            self.markLabelButton.setText("-") #otherwise leave the value at None

    def setUserPlayerWithMark(self, playerNumber):
        if playerNumber == 1 or playerNumber == 2:
            self.userPlayingWithMark = playerNumber
        else:
            self.logger.error("invalid playerNumber in setUserPlayerNumber: {0}".format(playerNumber))

    def clearUserPlayerWithMark(self):
        self.userPlayingWithMark = self.startingMarkChoice

    def getUserPlayingWithMark(self):
        return self.userPlayingWithMark

