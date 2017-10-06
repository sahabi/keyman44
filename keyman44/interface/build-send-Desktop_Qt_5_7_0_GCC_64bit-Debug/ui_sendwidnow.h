/********************************************************************************
** Form generated from reading UI file 'sendwidnow.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SENDWIDNOW_H
#define UI_SENDWIDNOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_SendWidnow
{
public:
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QWidget *centralWidget;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *SendWidnow)
    {
        if (SendWidnow->objectName().isEmpty())
            SendWidnow->setObjectName(QStringLiteral("SendWidnow"));
        SendWidnow->resize(400, 300);
        menuBar = new QMenuBar(SendWidnow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        SendWidnow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(SendWidnow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        SendWidnow->addToolBar(mainToolBar);
        centralWidget = new QWidget(SendWidnow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        SendWidnow->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(SendWidnow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        SendWidnow->setStatusBar(statusBar);

        retranslateUi(SendWidnow);

        QMetaObject::connectSlotsByName(SendWidnow);
    } // setupUi

    void retranslateUi(QMainWindow *SendWidnow)
    {
        SendWidnow->setWindowTitle(QApplication::translate("SendWidnow", "SendWidnow", 0));
    } // retranslateUi

};

namespace Ui {
    class SendWidnow: public Ui_SendWidnow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SENDWIDNOW_H
