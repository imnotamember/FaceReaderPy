__author__ = 'Joshua Zosky'
"""version for CPython implementation of Python for .Net"""

import clr
clr.AddReference("FaceReaderAPI")  # Load the FaceReaderAPI.dll from the Python DLL's folder
# from FaceReaderAPI import frAPI
from FaceReaderAPI import FaceReaderController as FRController
from FaceReaderAPI import Data as FRData


class Controller:

    def __init__(self, ipAdd, portNum):
        """define initial values and add an IP address(string) and Port number(integer)"""
        self.ipAddress = str(ipAdd)
        self.portNumber = int(portNum)
        self.FR_Controller = None
        self.FR_Data = FRData
        self.classification = None
        print ipAdd, portNum
        print self.ipAddress, self.portNumber
        print self.FR_Controller

    def check(self):
        """Check if the controller is instantiated and has an IP address and Port number"""
        try:
            print self.ipAddress
            print self.portNumber
        except NameError, e:
            print e
        if self.FR_Controller is not None:
            print 'It Exists'
            self.FR_Controller.Dispose()
        else:
            print "Doesn't exist"

        self.FR_Controller = FRController(self.ipAddress, self.portNumber)

        print "Just created", self.FR_Controller

    def connect(self):
        """Instantiate Event Handlers and attempt to connect to FaceReader"""
        self.FR_Controller.ClassificationReceived += self.frc_classification_received
        self.FR_Controller.Disconnected += self.frc_disconnected
        self.FR_Controller.Connected += self.frc_connected
        self.FR_Controller.ActionSucceeded += self.frc_action_succeeded
        self.FR_Controller.ErrorOccured += self.frc_error_occurred
        self.FR_Controller.AvailableStimuliReceived += self.frc_available_stimuli_received
        self.FR_Controller.AvailableEventMarkersReceived += self.frc_available_event_markers_received
        # # Connect to FaceReader. If the connection was successful,
        # # 'Connected' will fire, otherwise 'Disconnected' will fire.
        self.FR_Controller.ConnectToFaceReader()

    @staticmethod
    def frc_available_stimuli_received(source, args):
        print source
        print "Stimuli received:\n%s" % args.Stimuli

    @staticmethod
    def frc_available_event_markers_received(source, args):
        print source
        print "Event Markers received:\n%s" % args.EventMarkers

    @staticmethod
    def frc_error_occurred(source, args):
        print source
        print "Error occurred %s" % args.Message

    @staticmethod
    def frc_action_succeeded(source, args):
        print source
        print "Action Succeeded: %s" % args.Message

    @staticmethod
    def frc_connected(source, args):
        print source, args
        print "Connection to FaceReader was successful"

    @staticmethod
    def frc_disconnected(source, args):
        print source, args
        print "Disconnected"

    def frc_classification_received(self, source, args):
        """get the classification from the event arguments"""
        print source
        self.classification = args
        # FaceReaderAPI.Data.Classification classification = e.Classification
        # # if a classification was received
        if self.classification is not None:
            # if the classification is in the form of a StateLogs
            if self.classification.LogType == self.FR_Data.LogType.StateLog:
                # show the information
                print "State Log: %s" % self.classification
                # if the classification is in the form of a DetailedLog
            else:
                # show the information
                print "Detailed Log: %s" % self.classification

    def disconnect(self):
        """Disconnect from FaceReader, and print message if it is not connected yet"""
        if self.FR_Controller is not None:
            # # if there is a connection, disconnect
            if self.FR_Controller.IsConnected:
                self.FR_Controller.DisconnectFromFaceReader()
            else:
                print "There is no connection to disconnect"
        else:
            print "object doesn't exist"
