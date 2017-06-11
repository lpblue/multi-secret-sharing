from PyQt5 import QtCore, QtWidgets

class Ui_multisecret_gui(object):
    def __init__(self):
        self.secrets = 3
        self.users = 3
    
    def setupUi(self, multisecret_gui):
        multisecret_gui.setObjectName("multisecret_gui")
        multisecret_gui.resize(733, 468)
        self.tabWidget = QtWidgets.QTabWidget(multisecret_gui)
        #self.tabWidget.setGeometry(QtCore.QRect(0, 0, 751, 481))
        self.tabWidget.setObjectName("tabWidget")

        # put QTabWidget in a layout to enable resizing
        layout = QtWidgets.QVBoxLayout(multisecret_gui)
        layout.addWidget(self.tabWidget)

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 711, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")

        self.button_split = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_split.setObjectName("button_split")
        self.gridLayout.addWidget(self.button_split, 4, 4, 1, 1)

        self.check_s2p1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_s2p1.setObjectName("check_s2p1")
        self.gridLayout.addWidget(self.check_s2p1, 2, 5, 1, 1)
        self.secret_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.secret_1.setObjectName("secret_1")
        self.gridLayout.addWidget(self.secret_1, 0, 4, 1, 1)
        self.label_secret2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_secret2.setObjectName("label_secret2")
        self.gridLayout.addWidget(self.label_secret2, 2, 0, 1, 1)
        self.prime = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.prime.setObjectName("prime")
        self.gridLayout.addWidget(self.prime, 5, 4, 1, 1)
        self.check_s3p2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_s3p2.setObjectName("check_s3p2")
        self.gridLayout.addWidget(self.check_s3p2, 3, 6, 1, 1)
        self.label_secret3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_secret3.setObjectName("label_secret3")
        self.gridLayout.addWidget(self.label_secret3, 3, 0, 1, 1)
        self.check_s1p2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_s1p2.setObjectName("check_s1p2")
        self.gridLayout.addWidget(self.check_s1p2, 0, 6, 1, 1)
        self.check_s1p1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_s1p1.setObjectName("check_s1p1")
        self.gridLayout.addWidget(self.check_s1p1, 0, 5, 1, 1)
        self.secret_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)

        self.secret_3.setObjectName("secret_3")
        self.gridLayout.addWidget(self.secret_3, 3, 4, 1, 1)

        self.check_s1p3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_s1p3.setObjectName("check_s1p3")
        self.gridLayout.addWidget(self.check_s1p3, 0, 7, 1, 1)
        self.check_s3p1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_s3p1.setObjectName("check_s3p1")
        self.gridLayout.addWidget(self.check_s3p1, 3, 5, 1, 1)
        self.label_prime = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_prime.setObjectName("label_prime")
        self.gridLayout.addWidget(self.label_prime, 5, 0, 1, 1)

        self.secret_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.secret_2.setObjectName("secret_2")
        self.gridLayout.addWidget(self.secret_2, 2, 4, 1, 1)

        self.check_s2p2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_s2p2.setObjectName("check_s2p2")
        self.gridLayout.addWidget(self.check_s2p2, 2, 6, 1, 1)
        self.label_secret1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_secret1.setObjectName("label_secret1")
        self.gridLayout.addWidget(self.label_secret1, 0, 0, 1, 1)
        self.check_s2p3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_s2p3.setObjectName("check_s2p3")
        self.gridLayout.addWidget(self.check_s2p3, 2, 7, 1, 1)
        self.check_s3p3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_s3p3.setObjectName("check_s3p3")
        self.gridLayout.addWidget(self.check_s3p3, 3, 7, 1, 1)
        self.statusbar = QtWidgets.QLabel(self.tab)
        self.statusbar.setGeometry(QtCore.QRect(10, 417, 721, 20))
        self.statusbar.setObjectName("statusbar")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 711, 391))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 6, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.button_combine = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_combine.setObjectName("button_combine")
        self.gridLayout_2.addWidget(self.button_combine, 6, 0, 1, 1)
        self.button_load_share_1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_load_share_1.setObjectName("button_load_share_1")
        self.gridLayout_2.addWidget(self.button_load_share_1, 0, 2, 1, 1)
        self.button_load_share_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_load_share_2.setObjectName("button_load_share_2")
        self.gridLayout_2.addWidget(self.button_load_share_2, 3, 2, 1, 1)
        self.button_load_share_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_load_share_3.setObjectName("button_load_share_3")
        self.gridLayout_2.addWidget(self.button_load_share_3, 4, 2, 1, 1)
        self.button_load_public_info = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_load_public_info.setObjectName("_button_load_public_info")
        self.gridLayout_2.addWidget(self.button_load_public_info, 5, 2, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 691, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.number_of_secrets = QtWidgets.QSpinBox(self.layoutWidget)
        self.number_of_secrets.setMinimum(2)
        self.number_of_secrets.setMaximum(16)
        self.number_of_secrets.setProperty("value", 3)
        self.number_of_secrets.setObjectName("number_of_secrets")
        self.gridLayout_3.addWidget(self.number_of_secrets, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)
        self.number_of_users = QtWidgets.QSpinBox(self.layoutWidget)
        self.number_of_users.setMinimum(2)
        self.number_of_users.setProperty("value", 3)
        self.number_of_users.setObjectName("number_of_users")
        self.gridLayout_3.addWidget(self.number_of_users, 0, 3, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")

        #
        # Dynamically created split tab
        #
        self.tab_dyn = QtWidgets.QWidget()
        self.tab_dyn.setObjectName("tab_dyn")
        self.gridLayoutWidget_dyn = QtWidgets.QWidget(self.tab_dyn)
        self.gridLayoutWidget_dyn.setGeometry(QtCore.QRect(10, 40, 711, 391))
        self.gridLayoutWidget_dyn.setObjectName("gridLayoutWidget_dyn")
        self.gridLayout_dyn = QtWidgets.QGridLayout(self.gridLayoutWidget_dyn)
        self.gridLayout_dyn.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_dyn.setObjectName("gridLayout_dyn")

        _translate = QtCore.QCoreApplication.translate
        self.secret_labels = [None]*self.secrets
        self.secret_inputs = [None]*self.secrets
        self.checkboxes = [[[None] for _ in range(self.users)] for _ in range(self.secrets)]

        for secret in range(self.secrets):
            self.secret_labels[secret] = QtWidgets.QLabel(self.gridLayoutWidget_dyn)
            self.secret_labels[secret].setObjectName("secret_label"+str(secret))
            self.gridLayout_dyn.addWidget(self.secret_labels[secret], secret, 0, 1, 1)

            self.secret_inputs[secret] = QtWidgets.QLineEdit(self.gridLayoutWidget_dyn)
            self.secret_inputs[secret].setObjectName("secret_input"+str(secret))
            self.gridLayout_dyn.addWidget(self.secret_inputs[secret], secret, 1, 1, 1)

            for user in range(self.users):
                self.checkboxes[secret][user] = QtWidgets.QCheckBox(self.gridLayoutWidget_dyn)
                self.checkboxes[secret][user].setObjectName("check_s{}p{}".format(secret, user))
                self.gridLayout_dyn.addWidget(self.checkboxes[secret][user], secret, 2+user, 1, 1)
                self.checkboxes[secret][user].setText(_translate("multisecret_gui", "User "+str(user+1)))

        self.button_split_dyn = QtWidgets.QPushButton(self.gridLayoutWidget_dyn)
        self.button_split_dyn.setObjectName("button_split")
        self.gridLayout_dyn.addWidget(self.button_split_dyn, 4, 1, 1, 3)
        self.button_split_dyn.setText('Split secrets')

        self.button_split_dyn.clicked.connect(self.split_secret_dynamic)

        self.tabWidget.addTab(self.tab_dyn, "")
        # end of tab

        #
        # Dynamically created reconstruction tab
        #
        self.tab_dyn_reconstr = QtWidgets.QWidget()
        self.tab_dyn_reconstr.setObjectName("tab_dyn_reconstr")
        self.gridLayoutWidget_dyn_reconstr = QtWidgets.QWidget(self.tab_dyn_reconstr)
        self.gridLayoutWidget_dyn_reconstr.setGeometry(QtCore.QRect(10, 40, 711, 391))
        self.gridLayoutWidget_dyn_reconstr.setObjectName("gridLayoutWidget_dyn_reconstr")
        self.gridLayout_dyn_reconstr = QtWidgets.QGridLayout(self.gridLayoutWidget_dyn_reconstr)
        self.gridLayout_dyn_reconstr.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_dyn_reconstr.setObjectName("gridLayout_dyn_reconstr")

        _translate = QtCore.QCoreApplication.translate
        self.reconstr_user_labels = [None] * self.users
        self.user_data_reconstr_buttons = [None] * self.users

        self.button_load_public_info_dyn = QtWidgets.QPushButton(self.gridLayoutWidget_dyn_reconstr)
        self.gridLayout_dyn_reconstr.addWidget(self.button_load_public_info_dyn, 0, 0, 1, 1)
        for user in range(self.users):
            self.user_data_reconstr_buttons[user] = QtWidgets.QPushButton(self.gridLayoutWidget_dyn_reconstr)
            self.gridLayout_dyn_reconstr.addWidget(self.user_data_reconstr_buttons[user], user+1, 0, 1, 1)

        self.button_reconstr_dyn = QtWidgets.QPushButton(self.gridLayoutWidget_dyn_reconstr)
        self.gridLayout_dyn_reconstr.addWidget(self.button_reconstr_dyn, 0, 1, 1, 1)
        self.button_reconstr_dyn.clicked.connect(self.combine_secret_dynamic)

        self.textBrowser_dyn = QtWidgets.QTextBrowser(self.gridLayoutWidget_dyn_reconstr)
        self.textBrowser_dyn.setObjectName("textBrowser_dyn")
        self.gridLayout_dyn_reconstr.addWidget(self.textBrowser_dyn, 1, 1, 4, 1)

        self.tabWidget.addTab(self.tab_dyn_reconstr, "")
        # end of tab

        self.actionSetSecretsNumber = QtWidgets.QAction(multisecret_gui)
        self.actionSetSecretsNumber.setObjectName("actionSetSecretsNumber")

        self.retranslateUi(multisecret_gui)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(multisecret_gui)


    def retranslateUi(self, multisecret_gui):
        _translate = QtCore.QCoreApplication.translate
        multisecret_gui.setWindowTitle(_translate("multisecret_gui", "Multi-secret Sharing Tool"))
        self.button_split.setText(_translate("multisecret_gui", "Split secrets"))
        self.check_s2p1.setText(_translate("multisecret_gui", "User 1"))
        self.label_secret2.setText(_translate("multisecret_gui", "Secret 2"))
        self.check_s3p2.setText(_translate("multisecret_gui", "User 2"))
        self.label_secret3.setText(_translate("multisecret_gui", "Secret 3"))
        self.check_s1p2.setText(_translate("multisecret_gui", "User 2"))
        self.check_s1p1.setText(_translate("multisecret_gui", "User 1"))
        self.check_s1p3.setText(_translate("multisecret_gui", "User 3"))
        self.check_s3p1.setText(_translate("multisecret_gui", "User 1"))
        self.label_prime.setText(_translate("multisecret_gui", "Prime"))
        self.check_s2p2.setText(_translate("multisecret_gui", "User 2"))
        self.label_secret1.setText(_translate("multisecret_gui", "Secret 1"))
        self.check_s2p3.setText(_translate("multisecret_gui", "User 3"))
        self.check_s3p3.setText(_translate("multisecret_gui", "User 3"))
        self.statusbar.setText(_translate("multisecret_gui", "Status Bar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("multisecret_gui", "Roy-Adhikari split"))
        self.label_4.setText(_translate("multisecret_gui", "User 2"))
        self.label_8.setText(_translate("multisecret_gui", "User 1"))
        self.label_6.setText(_translate("multisecret_gui", "User 3"))
        self.button_combine.setText(_translate("multisecret_gui", "Combine secrets"))
        self.button_load_share_1.setText(_translate("multisecret_gui", "Load pseudo share..."))
        self.button_load_share_2.setText(_translate("multisecret_gui", "Load pseudo share..."))
        self.button_load_share_3.setText(_translate("multisecret_gui", "Load pseudo share..."))
        self.button_load_public_info.setText(_translate("multisecret_gui", "Load public information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("multisecret_gui", "Combine secret from file"))
        self.label.setText(_translate("multisecret_gui", "Number of secrets"))
        self.label_2.setText(_translate("multisecret_gui", "Number of users"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("multisecret_gui", "Problem size"))
        
        for secret in range(self.secrets):
            self.secret_labels[secret].setText(_translate("multisecret_gui", "Secret "+str(secret+1)))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dyn), _translate("multisecret_gui", "Dynamic split"))

        # Dynamic reconstruction tab
        for user in range(self.users):
            self.user_data_reconstr_buttons[user].setText(_translate("multisecret_gui", "Load pseudo share from user "+str(user+1)+"..."))
        self.button_reconstr_dyn.setText(_translate("multisecret_gui", "Reconstruct secrets"))
        self.button_load_public_info_dyn.setText(_translate("multisecret_gui", "Load public info"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dyn_reconstr), _translate("multisecret_gui", "Dynamic reconstruction"))

        self.actionSetSecretsNumber.setText(_translate("multisecret_gui", "setSecretsNumber"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    multisecret_gui = QtWidgets.QDialog()
    ui = Ui_multisecret_gui()
    ui.setupUi(multisecret_gui)
    multisecret_gui.show()
    sys.exit(app.exec_())

