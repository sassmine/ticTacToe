

    def updateUI(self):
        self.spot1View.setPixmap(QtGui.QPixmap(":/" + str(self.spot1.getValue())))
        self.spot2View.setPixmap(QtGui.QPixmap(":/" + str(self.spot2.getValue())))
        self.spot3View.setPixmap(QtGui.QPixmap(":/" + str(self.spot3.getValue())))
        self.spot4View.setPixmap(QtGui.QPixmap(":/" + str(self.spot4.getValue())))
        self.spot5View.setPixmap(QtGui.QPixmap(":/" + str(self.spot5.getValue())))
        self.spot6View.setPixmap(QtGui.QPixmap(":/" + str(self.spot6.getValue())))
        self.spot7View.setPixmap(QtGui.QPixmap(":/" + str(self.spot7.getValue())))
        self.spot8View.setPixmap(QtGui.QPixmap(":/" + str(self.spot8.getValue())))
        self.spot9View.setPixmap(QtGui.QPixmap(":/" + str(self.spot9.getValue())))
        # Add your code here to update the GUI view so it matches the game state.
        self.resultsLabel.setText(self.results)
        self.winsLabel.setText(str(self.wins))
        self.lossesLabel.setText(str(self.losses))



    def restartGame(self):
        self.spot1 = Board()
        self.spot2 = Board()
        self.spot3 = Board()
        self.spot4 = Board()
        self.spot5 = Board()
        self.spot6 = Board()
        self.spot7 = Board()
        self.spot8 = Board()
        self.spot9 = Board()
        self.spot1.setValue()
        self.spot2.setValue()
        self.spot3.setValue()
        self.spot4.setValue()
        self.spot5.setValue()
        self.spot6.setValue()
        self.spot7.setValue()
        self.spot8.setValue()
        self.spot9.setValue()

       # self.firstRoll = True
        self.results = ""
        self.playerLost = False
       # self.firstRollValue = 0
        #self.buttonText = "Roll"
        self.wins = 0
        self.losses = 0
        self.point = 0


    def saveGame(self):
        saveItems = (self.spot1, self.spot2, self.spot3, self.spot4, self.spot5, self.spot6, self.spot7, self.spot8, self.spot9, self.firstRoll, self.results, self.playerLost, self.firstRollValue,
                     self.buttonText, self.wins, self.losses, self.point)
        if self.appSettings.contains('pickleFilename'):
            with open(path.join(path.dirname(path.realpath(__file__)), self.appSettings.value('pickleFilename',
                 type=str)), 'wb') as pickleFile:
                dump(saveItems, pickleFile)
        else:
            self.logger.critical("No pickle Filename")

    def restoreGame(self):
        if self.appSettings.contains('pickleFilename'):
            self.appSettings.value('pickleFilename', type=str)
            with open(path.join(path.dirname(path.realpath(__file__)), self.appSettings.value('pickleFilename', type=str)), 'rb') as pickleFile:
                return load(pickleFile)
        else:
            self.logger.critical("No pickle Filename")

    def preferencesSelectButtonClickedHandler(self):
        print("Setting preferences")
        preferencesDialog = PreferencesDialog()
        preferencesDialog.show()
        preferencesDialog.exec_()
        self.restoreSettings()
        self.updateUI()


    def restartButtonClickedHandler(self):
        self.restartGame()
        self.saveGame()
        self.updateUI()

    def restoreSettings(self):
        # Restore settings values, write defaults to any that don't already exist

        if self.appSettings.contains("createLogFile"):
            self.createLogFile = self.appSettings.value('createLogFile')
        else:
            self.createLogFile = logFilenameDefault
            self.appSettings.setValue('createLogFile', self.createLogFile)

        if self.appSettings.contains('logFile'):
            self.logFilename = self.appSettings.value('logFile', type=str)
        else:
            self.logFilename = 'pythonGraderLog.txt'
            self.appSettings.setValue('logFile', self.logFilename)

        if self.appSettings.contains('pickleFilename'):
            self.pickleFilename = self.appSettings.value('pickleFilename', type=str)
        else:
            self.pickleFilename = ".crapsSavedObjects.pl"
            self.appSettings.setValue('pickleFilename', self.pickleFilename)

    # @pyqtSlot()
    def preferencesButtonClickedHandler(self):
        print("Setting preferences")
        preferencesDialog = PreferencesDialog()
        preferencesDialog.show()
        preferencesDialog.exec_()
        self.restoreSettings()
        self.updateUI()

    def restoreSettings(self):
        if appSettings.contains('inputPlayerLetter')
        if self.appSettings.contains('createLogFile'):
            self.createLogFile = appSettings.value('createLogFile', type=bool)
        else:
            self.createLogFile = logFileNameDefault
            self.appSettings.setValue('createLogFile', self.createLogFile)
    #set a break point before restore settings and look at all variables and they should have

    @pyqtSlot()   #Player asked to quit the game.
    def closeEvent(self, event):
        self.logger.debug("Closing app event")
        if self.quitCounter == 0:
            self.quitCounter += 1
            quitMessage = "Are you sure you want to quit?"
            reply = QMessageBox.question(self, 'Message', quitMessage, QMessageBox.Yes, QMessageBox.No)

            if reply ==QMessageBox.Yes:
                self.saveGame()
                event.accept()
            else:
                event.ignore()
            return super().closeEvent(event)

class PreferencesDialog(QDialog):
    def __init__(self, parent = Board):
        super(PreferencesDialog, self).__init__()

        uic.loadUi('preferencesDialog.ui', self)

        self.appSettings = QSettings()
        if self.appSettings.contains('playerLetterDefault'):
            self.player = self.appSettings.value('inputPlayerLetter', type=str)
        else:
            self.player = startingDefault
            self.appSettings.setValue('startingBank',self.startingBank)

        if self.appSettings.contains('createLogFile'):
            self.createLogFile = self.appSettings.value('createLogFile', type = bool)
        else:
            self.createLogFile = logFilenameDefault
            self.appSettings.setValue('createLogFile', self.createLogFile)

        self.buttonBox.rejected.connect(self.cancelClickedHandler)
        self.buttonBox.accepted.connect(self.okayClickedHandler)
        self.startingBankValue.editingFinished.connect(self.startingBankValueChanged)
        self.maximumBetValue.editingFinished.connect(self.maximumBetValueChanged)
        self.minimumBetValue.editingFinished.connect(self.minimumBetValueChanged)
       # self.createLogFileCheckBox.stateChanged.connect(self.createLogFileChanged)
        self.updateUI()

    def updateUI(self):
        self.startingBankValue.setText(str(self.startingBank))
        self.maximumBetValue.setText(str(self.maximumBet))
        self.minimumBetValue.setText(str(self.minimumBet))