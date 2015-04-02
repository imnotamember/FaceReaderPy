__author__ = 'Joshua Zosky'
"""version for CPython implementation of Python for .Net"""

import clr
clr.AddReference("FaceReaderAPI")  # Load the FaceReaderAPI.dll from the Python DLL's folder
# from FaceReaderAPI import frAPI
from FaceReaderAPI import FaceReaderController as FRController
from FaceReaderAPI import Data as FRData


class Controller:

    def __init__(self, ipAdd, portNum):
        """

        Define initial values and add an IP address(string) and Port number(integer)
        :param self.onOff: Bool value, True = turn State Logging on; False = turn State Logging off
        """
        self.ipAddress = str(ipAdd)
        self.portNumber = int(portNum)
        self.FR_Controller = None
        self.FR_Data = FRData.Classification
        self.classification = self.FR_Data("")
        self.isRecording = False
        self.currentEvents = {}
        self.onOff = False
        print ipAdd, portNum
        print self.ipAddress, self.portNumber
        print self.FR_Controller

    # # Event Handlers # #
    @staticmethod
    def frc_available_stimuli_received(args):
        print "Stimuli received:\n%s" % args.Stimuli

    @staticmethod
    def frc_available_event_markers_received(args):
        print "Event Markers received:\n%s" % args.EventMarkers

    @staticmethod
    def frc_error_occurred(args):
        print "Error occurred %s" % args.Message

    @staticmethod
    def frc_action_succeeded(args):
        print "Action Succeeded: %s" % args.Message

    @staticmethod
    def frc_connected():
        print "Connection to FaceReader was successful"

    @staticmethod
    def frc_disconnected():
        print "Disconnected"

    def frc_classification_received(self, source, args):
        """get the classification from the event arguments"""
        print source
        self.classification = args.Classification
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

    # # Methods # #
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
        if self.FR_Controller is not None:
            print 'It Exists'
            self.FR_Controller.Dispose()
        else:
            print "Doesn't exist"

        self.FR_Controller = FRController(self.ipAddress, self.portNumber)

        print "Just created", self.FR_Controller

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

    def start_recording(self):
        """Begin recording in FaceReader(FaceReader refers to this as ANALYSIS, but it's just recording video/data)"""
        self.isRecording = True
        try:
            self.FR_Controller.StartAnalyzing()
        except:
            self.isRecording = False
            print "Not connected to FaceReader"


    def stop_recording(self):
        """End recording in FaceReader(FaceReader refers to this as ANALYSIS, but it's just recording video/data)"""
        self.isRecording = False
        try:
            self.FR_Controller.StopAnalyzing()
        except:
            print "Not connected to FaceReader"

    def start_event_marker(self, event_name):
        """

        :param event_name: a list of currently observed events(can be multiple with different names)
        Send starting point of event called event_name.
        This event must be followed by an 'end_event_marker' to end the event.
        In FaceReader an event is a time frame of interest in a recording,
        which has both a start and stopping point.
        The event is thusly added to the currentEvents list to
        check later if it has been started in order to stop.
        """
        event_name = str(event_name)
        self.currentEvents[event_name] = True
        self.FR_Controller.ScoreEventMarker(event_name)

    def stop_event_marker(self, event_name):
        """

        :param event_name: a list of currently observed events(can be multiple with different names)
        Send stopping point of event called event_name.
        This event must be preceded by a 'start_event_marker' to begin the event.
        In FaceReader an event is a time frame of interest in a recording,
        which has both a start and stopping point.
        The event is thusly removed from the currentEvents list to
        prevent mistakenly trying to stop an already stopped event.
        """
        event_name = str(event_name)
        try:
            if self.currentEvents[event_name]:
                self.FR_Controller.ScoreEventMarker(event_name)
                self.currentEvents[event_name] = False
            else:
                print "%s hasn't been restarted yet." % event_name
        except:
            print "%s hasn't been started yet." % event_name

    def state_log(self):
        """Toggle State Logging to console on/off"""
        if self.onOff:
            self.FR_Controller.StopLogSending(LogType.StateLog)
            self.onOff = False
        else:
            self.FR_Controller.StartLogSending(LogType.StateLog)
            self.onOff = True
