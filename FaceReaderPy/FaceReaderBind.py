__author__ = 'Joshua Zosky'
#version for Iron Python

import clr
clr.AddReferenceToFile("FaceReaderAPI.dll")
import FaceReaderAPI as frAPI


class Controller:

    def __init__(self, ipAdd, portNum):
        self.ipAddress = str(ipAdd)
        self.portNumber = int(portNum)
        print((ipAdd, portNum))
        print((self.ipAddress, self.portNumber))

    def connect(self):
        try:
            print((self.ipAddress))
            print((self.portNumber))
        except NameError:
            print("ipAddress and/or portNumber is not defined")
        try:
            print((self.FR_Controller, 'It Exists'))
            self.FR_Controller.Dispose()
        except:
            print("It doesn't exist")

        self.FR_Controller = frAPI.FaceReaderController(self.ipAddress, self.portNumber)
        print(("Just created", self.FR_Controller))

        try:
            '''
            ## register the events ##
            --------Need to analyze this for potential use in the future.
            FR_Controller.ClassificationReceived += EventHandler<ClassificationEventArgs>(a_faceReaderController_ClassificationReceived)
            FR_Controller.Disconnected += EventHandler(a_faceReaderController_Disconnected)
            FR_Controller.Connected += EventHandler(a_faceReaderController_Connected)
            FR_Controller.ActionSucceeded += EventHandler<MessageEventArgs>(a_faceReaderController_ActionSucceeded)
            FR_Controller.ErrorOccured += EventHandler<ErrorEventArgs>(a_faceReaderController_ErrorOccured)
            FR_Controller.AvailableStimuliReceived += EventHandler<AvailableStimuliEventArgs>(a_faceReaderController_AvailableStimuliReceived)
            FR_Controller.AvailableEventMarkersReceived += EventHandler<AvailableEventMarkersEventArgs>(a_faceReaderController_AvailableEventMarkersReceived)
            '''
            ## connect to FaceReader. If the connection was succesful,
            ##  Connected will fire, otherwise Disconnected will fire.
            self.FR_Controller.ConnectToFaceReader()
        except:
            print('FaceReader is not connected')
            print((self.FR_Controller.Connected))