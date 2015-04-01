__author__ = 'Joshua Zosky'
#version for CPython implemetation of 'Python for .Net

import clr
clr.AddReference("FaceReaderAPI")  # Load the FaceReaderAPI.dll from the Python DLL's folder
#from FaceReaderAPI import frAPI
from FaceReaderAPI import FaceReaderController as FRController


class Controller:

    def __init__(self, ipAdd, portNum):
        self.ipAddress = str(ipAdd)
        self.portNumber = int(portNum)
        self.FR_Controller = None
        print ipAdd, portNum
        print self.ipAddress, self.portNumber
        print self.FR_Controller

    def create(self):
        try:
            print self.ipAddress
            print self.portNumber
        except NameError, e:
            print e
        if self.FR_Controller != None:
            print 'It Exists'
            self.FR_Controller.Dispose()
        else:
            print "Doesn't exist"

        self.FR_Controller = FRController(self.ipAddress, self.portNumber)

        print "Just created", self.FR_Controller

    def connect(self):
        ## register the events ##--------Need to analyze this for potential use in the future.
        self.FR_Controller.ClassificationReceived += self.a_faceReaderController_ClassificationReceived
        self.FR_Controller.Disconnected += self.a_faceReaderController_Disconnected
        self.FR_Controller.Connected += self.a_faceReaderController_Connected
        self.FR_Controller.ActionSucceeded += self.a_faceReaderController_ActionSucceeded
        self.FR_Controller.ErrorOccured += self.a_faceReaderController_ErrorOccured
        self.FR_Controller.AvailableStimuliReceived += self.a_faceReaderController_AvailableStimuliReceived
        self.FR_Controller.AvailableEventMarkersReceived += self.a_faceReaderController_AvailableEventMarkersReceived
        ## connect to FaceReader. If the connection was succesful,
        ##  Connected will fire, otherwise Disconnected will fire.
        try:
            self.FR_Controller.ConnectToFaceReader()
            #self.FR_Controller.Connected
        except:
            #self.FR_Controller.Disconnected
            print 'excepted'

    def a_faceReaderController_AvailableStimuliReceived(self, source, args):
        # WriteInfo(rtbMessages, "Stimuli received:\n" + ToMultilineString(e.Stimuli))
        # # put in combobox
        # AddToCombobox(cmbStimuli, e.Stimuli)
        print "Stimuli received:"

    def a_faceReaderController_AvailableEventMarkersReceived(self, source, args):
        # WriteInfo(rtbMessages, "Event Markers received:\n" + ToMultilineString(e.EventMarkers))
        # # put in combobox
        # AddToCombobox(cmbEventMarkers, e.EventMarkers)
        print "Event Markers received:"

    def a_faceReaderController_ErrorOccured(self, source, args):
        # WriteInfo(rtbMessages, "Error occured\t-> " + e.Exception.Message)
        print "Error occurred"

    def a_faceReaderController_ActionSucceeded(self, source, args):
        # WriteInfo(rtbMessages, "Action Succeeded\t-> " + e.Message)
        print "Action Succeeded"

    def a_faceReaderController_Connected(self, source, args):
        print "Connection to FaceReader was successful"
        # WriteInfo(rtbMessages, "Connection to FaceReader was succesfull")

    def a_faceReaderController_Disconnected(self, source, args):
        print "Disconnected"
        # WriteInfo(rtbMessages, "Disconnected")

    def a_faceReaderController_ClassificationReceived(self, source, args):
        # # get the classification from the event arguments
        # FaceReaderAPI.Data.Classification classification = e.Classification
        #
        # # if a classification was received
        # if (classification != null)
        #     # if the classification is in the form of a StateLogs
        #     if (classification.LogType == FaceReaderAPI.Data.LogType.StateLog)
        #         # show the information
        #         WriteInfo(rtbStateClassification, classification.ToString());
        #         # if the classification is in the form of a DetailedLog
        #     else:
        #        # show the information
        #             WriteInfo(rtbDetailedClassification, classification.ToString())
        pass

    def disconnect(self):
        if self.FR_Controller != None:
            ## if there is a connection, disconnect
            if self.FR_Controller.IsConnected:
                self.FR_Controller.DisconnectFromFaceReader()
            else:
                print "There is no connection to disconnect"
        else:
            print "object doesn't exist"