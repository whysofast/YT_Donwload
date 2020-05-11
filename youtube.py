import youtube_dl
import os
import sys
from PyQt5.QtWidgets import QStyleFactory, QApplication, QVBoxLayout, QGroupBox, QPushButton,\
     QDialog, QGridLayout, QLineEdit, QComboBox
from PyQt5.QtCore import Qt
from tkinter import Tk

class mainWindow(QDialog):

    def __init__(self):
        self.download_path = 'F:\Músicas\YT Songs'.replace('/','\\')
        #self.download_path = 'YT Songs'.replace('/','\\')
        self.mp3_options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320'
            }],
            'outtmpl': '%(title)s.%(ext)s',
            'prefer_ffmpeg': True,
            'keepvideo': False,
        }

        self.mp4_options = {
            'format': 'bestvideo+bestaudio[ext=m4a]/best',
            #'format': '136+bestaudio[ext=m4a]/best',
            #'listformats': True,
            'outtmpl': '%(title)s.%(ext)s'
        }

        if not os.path.exists(self.download_path):
            os.mkdir(self.download_path)

        os.chdir(self.download_path)

        super(mainWindow, self).__init__()

        self.setWindowTitle("Youtube Downloader - by WhySoFast")
        self.setWindowModality(Qt.ApplicationModal)
        self.setStyle(QStyleFactory.create('Cleanlooks'))
        self.resize(400, 100)

        self.Dialog_Layout = QVBoxLayout()

        self.GroupBox = QGroupBox('Video or Playlist url: ')
        self.GroupBox_Layout = QGridLayout()
        self.GroupBox_Layout.setAlignment(Qt.AlignCenter)

        self.Download_Button = QPushButton("Download mp3")
        self.Download_Button.clicked.connect(self.download_btn)
        self.Download_Buttonmp4 = QPushButton("Download mp4")
        self.Download_Buttonmp4.clicked.connect(self.download_btnmp4)
        self.Close_Button = QPushButton("Close")
        self.Close_Button.clicked.connect(self.close)

        self.LineEdit = QLineEdit()
        self.LineEdit.setPlaceholderText("Enter a valid URL")
        self.LineEdit.setText(ctrlc)
        self.LineEdit.setMinimumWidth(150)

        self.QualityComboBox_GroupBox = QGroupBox("MP3 Quality")
        self.QualityComboBox_GroupBox_layout = QVBoxLayout()
        self.QualityComboBox_GroupBox_layout.setAlignment(Qt.AlignCenter)
        self.QualityComboBox = QComboBox()
        self.QualityComboBox.addItems(['64 kbps', '96 kbps', '128 kbps', '192 kbps', '256 kbps', '320 kbps'])
        self.QualityComboBox.setCurrentIndex(3)
        self.QualityComboBox.setMinimumWidth(150)
        self.QualityComboBox_GroupBox_layout.addWidget(self.QualityComboBox)
        self.QualityComboBox_GroupBox.setLayout(self.QualityComboBox_GroupBox_layout)

        self.Qualitymp4ComboBox_GroupBox = QGroupBox("MP4 Quality")
        self.Qualitymp4ComboBox_GroupBox_layout = QVBoxLayout()
        self.Qualitymp4ComboBox_GroupBox_layout.setAlignment(Qt.AlignCenter)
        self.Qualitymp4ComboBox = QComboBox()
        self.Qualitymp4ComboBox.addItems(['Best as possible', 'Force 720p', 'Force 480p'])
        self.Qualitymp4ComboBox.setCurrentIndex(0)
        self.Qualitymp4ComboBox.setMinimumWidth(150)
        self.Qualitymp4ComboBox_GroupBox_layout.addWidget(self.Qualitymp4ComboBox)
        self.Qualitymp4ComboBox_GroupBox.setLayout(self.Qualitymp4ComboBox_GroupBox_layout)
        self.QualityComboBox_GroupBox_layout.addWidget(self.Download_Button)
        self.Qualitymp4ComboBox_GroupBox_layout.addWidget(self.Download_Buttonmp4)

        self.GroupBox_Layout.addWidget(self.LineEdit, 0, 0)
        self.GroupBox_Layout.addWidget(self.Close_Button, 1,1)
        self.GroupBox_Layout.addWidget(self.QualityComboBox_GroupBox, 1, 0)
        self.GroupBox_Layout.addWidget(self.Qualitymp4ComboBox_GroupBox, 2, 0)

        self.GroupBox.setLayout(self.GroupBox_Layout)
        self.Dialog_Layout.addWidget(self.GroupBox)

        self.setLayout(self.Dialog_Layout)

    def download_btn(self):
        url = self.LineEdit.text()
        self.quality = self.QualityComboBox.currentText().split(" kbps")[0]
        self.mp3_options['postprocessors'][0]['preferredquality'] = self.quality
        self.mp3_options['outtmpl'] = '%(title)s - ' + self.QualityComboBox.currentText() + '.%(ext)s'
        #print(f'Quality of mp3 chosen: {self.quality}')
        try:
            with youtube_dl.YoutubeDL(self.mp3_options) as dl:
                dl.download([url])

        except:
            self.raise_error()

    def download_btnmp4(self):
        url = self.LineEdit.text()
        self.qualitymp4  = self.Qualitymp4ComboBox.currentText()
        if self.qualitymp4 == 'Best as possible':
            self.mp4_options['format']= 'bestvideo+bestaudio[ext=m4a]/best'
            self.mp4_options['outtmpl']= '%(title)s' + ' - Best' + '.%(ext)s'
        elif self.qualitymp4 == 'Force 720p':
            self.mp4_options['format']= '136+bestaudio[ext=m4a]/best'
            self.mp4_options['outtmpl']= '%(title)s' + ' - 720p' + '.%(ext)s'
        elif self.qualitymp4 == 'Force 480p':
            self.mp4_options['format']= '135+bestaudio[ext=m4a]/best'
            self.mp4_options['outtmpl']= '%(title)s' + ' - 480p' + '.%(ext)s'

        try:
            with youtube_dl.YoutubeDL(self.mp4_options) as dl:
                dl.download([url])
                #result = dl.extract_info("{}".format(url))
                #print(result)
                # print(result.get("id", None))
        except:
            self.raise_error()
            
    def raise_error(self):
        self.LineEdit.clear()
        self.LineEdit.setStyleSheet("color: red;")

if __name__ == '__main__':
    APP = QApplication(sys.argv)

    try:
        if Tk().clipboard_get().split("v=")[0][-1] == "?":
            ctrlc = Tk().clipboard_get()
        else:
            ctrlc = ""
    except:
        ctrlc = ""

    GUI = mainWindow()
    GUI.show()

    sys.exit(APP.exec())

