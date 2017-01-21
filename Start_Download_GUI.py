from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import maine
import os
"""
=========================================================
====                                                 ====
==== By Aymen benchiheub                             ====
==== my twitter: https://twitter.com/BenchiheubAymen ====
==== my gmail : benchiheub.aymen@gmail.com           ====
=========================================================
"""
d = main.download()
path = os.getcwd()
print(path)
app = QApplication(sys.argv)
main_window = QWidget()
main_window.setWindowTitle('Videos Downloader')
main_window.resize(500,200)
main_window.move(500,150)
# Exit Button
exit_button = QPushButton('Exit',main_window)
exit_button.clicked.connect(exit)
exit_button.move(400,160)
# choose format
combo = QComboBox(main_window)
combo.move(200,15)
combo.addItem('1024p')
combo.addItem('720p')
combo.addItem('480p')
combo.addItem('360p')
combo.addItem('240p')
combo.addItem('144')
# label to choose format
choose = QLabel(main_window,text="<b>Choose video Format</b> ")
choose.move(10,20)
# line edit to enter the link
link = QLineEdit(main_window)
link.setPlaceholderText('Past The Link Here')
link.resize(400,30)
link.move(10,70)
# save at button
def get_path():
    path = QFileDialog.getSaveFileName(main_window,'save video at','video.mp4')
    path = str(path)
    platform = sys.platform
    if platform == 'linux':
        path_1 = path
        path_1 = path_1.split('/')
        print(path_1)
        name = path_1[-1]
        path = path.replace(name,'')
    else:
        a = "\\"
        path_1 = path
        path_1 = path_1.split(a)
        name = path_1[-1]
        path = path.replace(name,'')
        print(path)
save_button = QPushButton('...',main_window)
save_button.resize(40,30)
save_button.move(430,70)
save_button.clicked.connect(get_path)
# start download Button
def start_():
    url = link.text()
    if url == "":
        msg_ = "please Enter the link of the video"
        msg = QMessageBox.warning(main_window,"No Video Found !",msg_,QMessageBox.Ok)
    else:
        pass
    video_quality = str(combo.currentText())
    video_type = video_quality
    place = path
    print(place)
    d.start_download(url,video_type,place)
    msg_finish = QMessageBox.information(main_window,'Download finish','download video is finish',QMessageBox.Ok)



download_button = QPushButton('Start Download',main_window)
download_button.clicked.connect(start_)
download_button.move(170,110)
def about():
    msg_1 = """
    This programme created by aymen Benchiheub
    For any information or to get the source code
    ask me on facebook
    my Facebook : https://www.facebook.com/Benchiheub
    """

    msg = QMessageBox.information(main_window,'About',msg_1,QMessageBox.Ok)
about_button = QPushButton('About',main_window)
about_button.move(300,160)
about_button.clicked.connect(about)
#------------------------------------------
main_window.show()
app.exec_()
