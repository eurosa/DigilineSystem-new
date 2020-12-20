/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef MAINWINDOW_AUTO_H
#define MAINWINDOW_AUTO_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QLabel *time_show;
    QLabel *elapsedTimeLabel;
    QLabel *elapsedTimeShow;
    QToolButton *toolButton;
    QToolButton *toolButton_9;
    QToolButton *toolButton_10;
    QToolButton *toolPower_button;
    QToolButton *toolDownButton_1;
    QToolButton *toolUpButton_1;
    QToolButton *toolDownButton_2;
    QToolButton *toolUpButton_2;
    QToolButton *toolButton_16;
    QLabel *label_3;
    QLabel *label_2;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *tick_show;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QPushButton *otLighteningDetails;
    QPushButton *ventiLationDetails;
    QPushButton *gasIndicator;
    QPushButton *historyDetails;
    QPushButton *multiMediaDetails;
    QHBoxLayout *horizontalLayout;
    QPushButton *btnOn;
    QPushButton *btnOff;
    QWidget *horizontalLayoutWidget_2;
    QHBoxLayout *horizontalLayout_3;
    QToolButton *toolButton_3;
    QToolButton *toolButton_4;
    QToolButton *toolButton_5;
    QToolButton *toolButton_6;
    QToolButton *toolButton_2;
    QToolButton *toolButton_7;
    QToolButton *toolButton_8;
    QWidget *horizontalLayoutWidget_3;
    QHBoxLayout *horizontalLayout_7;
    QLabel *label;
    QWidget *horizontalLayoutWidget_4;
    QHBoxLayout *horizontalLayout_8;
    QToolButton *toolSettings_button;
    QToolButton *toolHome_button;
    QWidget *horizontalLayoutWidget_5;
    QHBoxLayout *horizontalLayout_10;
    QToolButton *toolPlay_button;
    QToolButton *toolPause_button;
    QToolButton *toolClose_button;
    QToolButton *toolButton_19;
    QToolButton *toolButton_20;
    QLabel *day_date_show;
    QWidget *horizontalLayoutWidget;
    QHBoxLayout *horizontalLayout_2;
    QToolButton *toolButton_22;
    QWidget *centralwidget;
    QLabel *time_label;
    QLabel *elapsedTimeShow_2;
    QLabel *elapsedTimeLabel_2;
    QPushButton *pushButton_6;
    QPushButton *pushButton_7;
    QLabel *elapsedTimeShow_3;
    QLabel *elapsedTimeShow_4;
    QLabel *label_6;
    QLabel *label_7;
    QLabel *elapsedTimeShow_5;
    QLabel *elapsedTimeShow_6;
    QLabel *label_8;
    QLabel *label_9;
    QLabel *label_10;
    QLabel *label_11;
    QLabel *elapsedTimeShow_7;
    QLabel *elapsedTimeShow_8;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->setEnabled(true);
        MainWindow->resize(1348, 824);
        QFont font;
        font.setUnderline(false);
        font.setStrikeOut(false);
        MainWindow->setFont(font);
        MainWindow->setLayoutDirection(Qt::LeftToRight);
        MainWindow->setAutoFillBackground(false);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        time_show = new QLabel(centralWidget);
        time_show->setObjectName(QString::fromUtf8("time_show"));
        time_show->setGeometry(QRect(0, 0, 281, 131));
        QFont font1;
        font1.setPointSize(64);
        font1.setUnderline(false);
        font1.setStrikeOut(false);
        time_show->setFont(font1);
        elapsedTimeLabel = new QLabel(centralWidget);
        elapsedTimeLabel->setObjectName(QString::fromUtf8("elapsedTimeLabel"));
        elapsedTimeLabel->setGeometry(QRect(580, 0, 91, 19));
        elapsedTimeShow = new QLabel(centralWidget);
        elapsedTimeShow->setObjectName(QString::fromUtf8("elapsedTimeShow"));
        elapsedTimeShow->setGeometry(QRect(440, 0, 361, 121));
        QFont font2;
        font2.setPointSize(48);
        font2.setUnderline(false);
        font2.setStrikeOut(false);
        elapsedTimeShow->setFont(font2);
        toolButton = new QToolButton(centralWidget);
        toolButton->setObjectName(QString::fromUtf8("toolButton"));
        toolButton->setGeometry(QRect(20, 120, 81, 29));
        toolButton_9 = new QToolButton(centralWidget);
        toolButton_9->setObjectName(QString::fromUtf8("toolButton_9"));
        toolButton_9->setGeometry(QRect(820, 690, 27, 29));
        toolButton_10 = new QToolButton(centralWidget);
        toolButton_10->setObjectName(QString::fromUtf8("toolButton_10"));
        toolButton_10->setGeometry(QRect(860, 690, 27, 29));
        toolPower_button = new QToolButton(centralWidget);
        toolPower_button->setObjectName(QString::fromUtf8("toolPower_button"));
        toolPower_button->setGeometry(QRect(900, 690, 121, 31));
        QIcon icon;
        icon.addFile(QString::fromUtf8("icon/power_white.png"), QSize(), QIcon::Normal, QIcon::Off);
        toolPower_button->setIcon(icon);
        toolDownButton_1 = new QToolButton(centralWidget);
        toolDownButton_1->setObjectName(QString::fromUtf8("toolDownButton_1"));
        toolDownButton_1->setGeometry(QRect(960, 380, 51, 41));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8("icon/down-white.png"), QSize(), QIcon::Normal, QIcon::Off);
        toolDownButton_1->setIcon(icon1);
        toolUpButton_1 = new QToolButton(centralWidget);
        toolUpButton_1->setObjectName(QString::fromUtf8("toolUpButton_1"));
        toolUpButton_1->setGeometry(QRect(1010, 380, 51, 41));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8("icon/up-white.png"), QSize(), QIcon::Normal, QIcon::Off);
        toolUpButton_1->setIcon(icon2);
        toolDownButton_2 = new QToolButton(centralWidget);
        toolDownButton_2->setObjectName(QString::fromUtf8("toolDownButton_2"));
        toolDownButton_2->setGeometry(QRect(1180, 380, 51, 41));
        toolDownButton_2->setIcon(icon1);
        toolUpButton_2 = new QToolButton(centralWidget);
        toolUpButton_2->setObjectName(QString::fromUtf8("toolUpButton_2"));
        toolUpButton_2->setGeometry(QRect(1230, 380, 51, 41));
        toolUpButton_2->setIcon(icon2);
        toolButton_16 = new QToolButton(centralWidget);
        toolButton_16->setObjectName(QString::fromUtf8("toolButton_16"));
        toolButton_16->setGeometry(QRect(740, 120, 61, 31));
        QFont font3;
        font3.setPointSize(6);
        font3.setUnderline(false);
        font3.setStrikeOut(false);
        toolButton_16->setFont(font3);
        toolButton_16->setLayoutDirection(Qt::LeftToRight);
        toolButton_16->setAutoRaise(false);
        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(1200, 210, 67, 19));
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(910, 250, 61, 61));
        label_2->setPixmap(QPixmap(QString::fromUtf8("icon/thermometer_60_60.png")));
        label_4 = new QLabel(centralWidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(1140, 250, 51, 61));
        label_4->setPixmap(QPixmap(QString::fromUtf8("icon/humidity_60_60.png")));
        label_5 = new QLabel(centralWidget);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(980, 210, 91, 21));
        tick_show = new QLabel(centralWidget);
        tick_show->setObjectName(QString::fromUtf8("tick_show"));
        tick_show->setGeometry(QRect(290, 50, 81, 51));
        QFont font4;
        font4.setPointSize(32);
        font4.setUnderline(false);
        font4.setStrikeOut(false);
        tick_show->setFont(font4);
        verticalLayoutWidget = new QWidget(centralWidget);
        verticalLayoutWidget->setObjectName(QString::fromUtf8("verticalLayoutWidget"));
        verticalLayoutWidget->setGeometry(QRect(0, 290, 222, 281));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        otLighteningDetails = new QPushButton(verticalLayoutWidget);
        otLighteningDetails->setObjectName(QString::fromUtf8("otLighteningDetails"));
        otLighteningDetails->setEnabled(true);
        otLighteningDetails->setSizeIncrement(QSize(0, 0));
        QFont font5;
        font5.setBold(true);
        font5.setItalic(false);
        font5.setUnderline(false);
        font5.setWeight(75);
        font5.setStrikeOut(false);
        otLighteningDetails->setFont(font5);
        otLighteningDetails->setAutoFillBackground(false);
        otLighteningDetails->setStyleSheet(QString::fromUtf8("QPushButton#pushButton {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#pushButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
""));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8("icon/lighting_white.png"), QSize(), QIcon::Normal, QIcon::Off);
        otLighteningDetails->setIcon(icon3);
        otLighteningDetails->setIconSize(QSize(19, 19));
        otLighteningDetails->setAutoRepeat(true);
        otLighteningDetails->setAutoExclusive(true);
        otLighteningDetails->setFlat(false);

        verticalLayout->addWidget(otLighteningDetails);

        ventiLationDetails = new QPushButton(verticalLayoutWidget);
        ventiLationDetails->setObjectName(QString::fromUtf8("ventiLationDetails"));
        ventiLationDetails->setStyleSheet(QString::fromUtf8("QPushButton#pushButton_2 {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#pushButton_2:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
""));
        QIcon icon4;
        icon4.addFile(QString::fromUtf8("icon/fan_white.png"), QSize(), QIcon::Normal, QIcon::Off);
        ventiLationDetails->setIcon(icon4);
        ventiLationDetails->setIconSize(QSize(19, 19));

        verticalLayout->addWidget(ventiLationDetails);

        gasIndicator = new QPushButton(verticalLayoutWidget);
        gasIndicator->setObjectName(QString::fromUtf8("gasIndicator"));
        gasIndicator->setEnabled(true);
        gasIndicator->setLayoutDirection(Qt::LeftToRight);
        gasIndicator->setStyleSheet(QString::fromUtf8("QPushButton#pushButton_3{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#pushButton_3:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
""));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8("icon/pressure_white.png"), QSize(), QIcon::Normal, QIcon::Off);
        gasIndicator->setIcon(icon5);
        gasIndicator->setIconSize(QSize(19, 19));

        verticalLayout->addWidget(gasIndicator);

        historyDetails = new QPushButton(verticalLayoutWidget);
        historyDetails->setObjectName(QString::fromUtf8("historyDetails"));
        historyDetails->setStyleSheet(QString::fromUtf8("QPushButton#pushButton_4{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#pushButton_4:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
""));
        QIcon icon6;
        icon6.addFile(QString::fromUtf8("icon/report_white.png"), QSize(), QIcon::Normal, QIcon::Off);
        historyDetails->setIcon(icon6);
        historyDetails->setIconSize(QSize(19, 19));

        verticalLayout->addWidget(historyDetails);

        multiMediaDetails = new QPushButton(verticalLayoutWidget);
        multiMediaDetails->setObjectName(QString::fromUtf8("multiMediaDetails"));
        multiMediaDetails->setStyleSheet(QString::fromUtf8("QPushButton#pushButton_5{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#pushButton_5:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
""));
        QIcon icon7;
        icon7.addFile(QString::fromUtf8("icon/multimedia_white.png"), QSize(), QIcon::Normal, QIcon::Off);
        multiMediaDetails->setIcon(icon7);
        multiMediaDetails->setIconSize(QSize(19, 19));

        verticalLayout->addWidget(multiMediaDetails);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        btnOn = new QPushButton(verticalLayoutWidget);
        btnOn->setObjectName(QString::fromUtf8("btnOn"));

        horizontalLayout->addWidget(btnOn);

        btnOff = new QPushButton(verticalLayoutWidget);
        btnOff->setObjectName(QString::fromUtf8("btnOff"));

        horizontalLayout->addWidget(btnOff);


        verticalLayout->addLayout(horizontalLayout);

        ventiLationDetails->raise();
        gasIndicator->raise();
        historyDetails->raise();
        multiMediaDetails->raise();
        otLighteningDetails->raise();
        horizontalLayoutWidget_2 = new QWidget(centralWidget);
        horizontalLayoutWidget_2->setObjectName(QString::fromUtf8("horizontalLayoutWidget_2"));
        horizontalLayoutWidget_2->setGeometry(QRect(320, 680, 451, 51));
        horizontalLayout_3 = new QHBoxLayout(horizontalLayoutWidget_2);
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        horizontalLayout_3->setContentsMargins(0, 0, 0, 0);
        toolButton_3 = new QToolButton(horizontalLayoutWidget_2);
        toolButton_3->setObjectName(QString::fromUtf8("toolButton_3"));

        horizontalLayout_3->addWidget(toolButton_3);

        toolButton_4 = new QToolButton(horizontalLayoutWidget_2);
        toolButton_4->setObjectName(QString::fromUtf8("toolButton_4"));

        horizontalLayout_3->addWidget(toolButton_4);

        toolButton_5 = new QToolButton(horizontalLayoutWidget_2);
        toolButton_5->setObjectName(QString::fromUtf8("toolButton_5"));

        horizontalLayout_3->addWidget(toolButton_5);

        toolButton_6 = new QToolButton(horizontalLayoutWidget_2);
        toolButton_6->setObjectName(QString::fromUtf8("toolButton_6"));

        horizontalLayout_3->addWidget(toolButton_6);

        toolButton_2 = new QToolButton(horizontalLayoutWidget_2);
        toolButton_2->setObjectName(QString::fromUtf8("toolButton_2"));

        horizontalLayout_3->addWidget(toolButton_2);

        toolButton_7 = new QToolButton(horizontalLayoutWidget_2);
        toolButton_7->setObjectName(QString::fromUtf8("toolButton_7"));

        horizontalLayout_3->addWidget(toolButton_7);

        toolButton_8 = new QToolButton(horizontalLayoutWidget_2);
        toolButton_8->setObjectName(QString::fromUtf8("toolButton_8"));

        horizontalLayout_3->addWidget(toolButton_8);

        horizontalLayoutWidget_3 = new QWidget(centralWidget);
        horizontalLayoutWidget_3->setObjectName(QString::fromUtf8("horizontalLayoutWidget_3"));
        horizontalLayoutWidget_3->setGeometry(QRect(330, 640, 121, 41));
        horizontalLayout_7 = new QHBoxLayout(horizontalLayoutWidget_3);
        horizontalLayout_7->setSpacing(6);
        horizontalLayout_7->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        horizontalLayout_7->setContentsMargins(0, 0, 0, 0);
        label = new QLabel(horizontalLayoutWidget_3);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_7->addWidget(label);

        horizontalLayoutWidget_4 = new QWidget(centralWidget);
        horizontalLayoutWidget_4->setObjectName(QString::fromUtf8("horizontalLayoutWidget_4"));
        horizontalLayoutWidget_4->setGeometry(QRect(1130, 680, 101, 51));
        horizontalLayout_8 = new QHBoxLayout(horizontalLayoutWidget_4);
        horizontalLayout_8->setSpacing(6);
        horizontalLayout_8->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_8->setObjectName(QString::fromUtf8("horizontalLayout_8"));
        horizontalLayout_8->setContentsMargins(0, 0, 0, 0);
        toolSettings_button = new QToolButton(horizontalLayoutWidget_4);
        toolSettings_button->setObjectName(QString::fromUtf8("toolSettings_button"));
        QIcon icon8;
        icon8.addFile(QString::fromUtf8("icon/settings_white.png"), QSize(), QIcon::Normal, QIcon::Off);
        toolSettings_button->setIcon(icon8);
        toolSettings_button->setIconSize(QSize(24, 24));

        horizontalLayout_8->addWidget(toolSettings_button);

        toolHome_button = new QToolButton(horizontalLayoutWidget_4);
        toolHome_button->setObjectName(QString::fromUtf8("toolHome_button"));
        QIcon icon9;
        icon9.addFile(QString::fromUtf8("icon/home_white.png"), QSize(), QIcon::Normal, QIcon::Off);
        toolHome_button->setIcon(icon9);
        toolHome_button->setIconSize(QSize(24, 24));

        horizontalLayout_8->addWidget(toolHome_button);

        horizontalLayoutWidget_5 = new QWidget(centralWidget);
        horizontalLayoutWidget_5->setObjectName(QString::fromUtf8("horizontalLayoutWidget_5"));
        horizontalLayoutWidget_5->setGeometry(QRect(480, 120, 241, 41));
        horizontalLayout_10 = new QHBoxLayout(horizontalLayoutWidget_5);
        horizontalLayout_10->setSpacing(6);
        horizontalLayout_10->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_10->setObjectName(QString::fromUtf8("horizontalLayout_10"));
        horizontalLayout_10->setContentsMargins(0, 0, 0, 0);
        toolPlay_button = new QToolButton(horizontalLayoutWidget_5);
        toolPlay_button->setObjectName(QString::fromUtf8("toolPlay_button"));
        QIcon icon10;
        icon10.addFile(QString::fromUtf8("icon/play_white.png"), QSize(), QIcon::Normal, QIcon::Off);
        toolPlay_button->setIcon(icon10);

        horizontalLayout_10->addWidget(toolPlay_button);

        toolPause_button = new QToolButton(horizontalLayoutWidget_5);
        toolPause_button->setObjectName(QString::fromUtf8("toolPause_button"));
        QIcon icon11;
        icon11.addFile(QString::fromUtf8("icon/pause_white.png"), QSize(), QIcon::Normal, QIcon::Off);
        toolPause_button->setIcon(icon11);

        horizontalLayout_10->addWidget(toolPause_button);

        toolClose_button = new QToolButton(horizontalLayoutWidget_5);
        toolClose_button->setObjectName(QString::fromUtf8("toolClose_button"));
        QIcon icon12;
        icon12.addFile(QString::fromUtf8("icon/close_white.png"), QSize(), QIcon::Normal, QIcon::Off);
        toolClose_button->setIcon(icon12);

        horizontalLayout_10->addWidget(toolClose_button);

        toolButton_19 = new QToolButton(horizontalLayoutWidget_5);
        toolButton_19->setObjectName(QString::fromUtf8("toolButton_19"));

        horizontalLayout_10->addWidget(toolButton_19);

        toolButton_20 = new QToolButton(horizontalLayoutWidget_5);
        toolButton_20->setObjectName(QString::fromUtf8("toolButton_20"));

        horizontalLayout_10->addWidget(toolButton_20);

        day_date_show = new QLabel(centralWidget);
        day_date_show->setObjectName(QString::fromUtf8("day_date_show"));
        day_date_show->setGeometry(QRect(190, 120, 171, 31));
        horizontalLayoutWidget = new QWidget(centralWidget);
        horizontalLayoutWidget->setObjectName(QString::fromUtf8("horizontalLayoutWidget"));
        horizontalLayoutWidget->setGeometry(QRect(0, 180, 211, 71));
        horizontalLayout_2 = new QHBoxLayout(horizontalLayoutWidget);
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        toolButton_22 = new QToolButton(horizontalLayoutWidget);
        toolButton_22->setObjectName(QString::fromUtf8("toolButton_22"));
        toolButton_22->setStyleSheet(QString::fromUtf8("QToolButton#toolButton_22 {\n"
"\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QToolButton#toolButton_22:pressed {\n"
"    background-color:gray;\n"
"    border-style: inset;\n"
"}\n"
""));

        horizontalLayout_2->addWidget(toolButton_22);

        centralwidget = new QWidget(centralWidget);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        centralwidget->setGeometry(QRect(260, 180, 631, 441));
        centralwidget->setStyleSheet(QString::fromUtf8(""));
        time_label = new QLabel(centralWidget);
        time_label->setObjectName(QString::fromUtf8("time_label"));
        time_label->setGeometry(QRect(160, 0, 41, 19));
        elapsedTimeShow_2 = new QLabel(centralWidget);
        elapsedTimeShow_2->setObjectName(QString::fromUtf8("elapsedTimeShow_2"));
        elapsedTimeShow_2->setGeometry(QRect(880, 0, 361, 121));
        elapsedTimeShow_2->setFont(font2);
        elapsedTimeLabel_2 = new QLabel(centralWidget);
        elapsedTimeLabel_2->setObjectName(QString::fromUtf8("elapsedTimeLabel_2"));
        elapsedTimeLabel_2->setGeometry(QRect(1000, 0, 121, 19));
        pushButton_6 = new QPushButton(centralWidget);
        pushButton_6->setObjectName(QString::fromUtf8("pushButton_6"));
        pushButton_6->setGeometry(QRect(960, 430, 106, 40));
        pushButton_6->setFont(font5);
        pushButton_6->setStyleSheet(QString::fromUtf8("QPushButton#pushButton_6 {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"   min-width: 5em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#pushButton_6:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
""));
        QIcon icon13;
        icon13.addFile(QString::fromUtf8("icon/temp_graph.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_6->setIcon(icon13);
        pushButton_6->setIconSize(QSize(24, 24));
        pushButton_7 = new QPushButton(centralWidget);
        pushButton_7->setObjectName(QString::fromUtf8("pushButton_7"));
        pushButton_7->setGeometry(QRect(1180, 430, 106, 40));
        pushButton_7->setFont(font5);
        pushButton_7->setStyleSheet(QString::fromUtf8("QPushButton#pushButton_7 {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"   min-width: 5em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#pushButton_7:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
""));
        QIcon icon14;
        icon14.addFile(QString::fromUtf8("icon/humidity_graph.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_7->setIcon(icon14);
        pushButton_7->setIconSize(QSize(24, 24));
        elapsedTimeShow_3 = new QLabel(centralWidget);
        elapsedTimeShow_3->setObjectName(QString::fromUtf8("elapsedTimeShow_3"));
        elapsedTimeShow_3->setGeometry(QRect(980, 240, 91, 71));
        elapsedTimeShow_3->setFont(font2);
        elapsedTimeShow_4 = new QLabel(centralWidget);
        elapsedTimeShow_4->setObjectName(QString::fromUtf8("elapsedTimeShow_4"));
        elapsedTimeShow_4->setGeometry(QRect(1200, 240, 101, 71));
        elapsedTimeShow_4->setFont(font2);
        label_6 = new QLabel(centralWidget);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setGeometry(QRect(1000, 320, 31, 21));
        label_7 = new QLabel(centralWidget);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setGeometry(QRect(1220, 320, 31, 21));
        elapsedTimeShow_5 = new QLabel(centralWidget);
        elapsedTimeShow_5->setObjectName(QString::fromUtf8("elapsedTimeShow_5"));
        elapsedTimeShow_5->setGeometry(QRect(1000, 340, 51, 31));
        elapsedTimeShow_5->setFont(font2);
        elapsedTimeShow_6 = new QLabel(centralWidget);
        elapsedTimeShow_6->setObjectName(QString::fromUtf8("elapsedTimeShow_6"));
        elapsedTimeShow_6->setGeometry(QRect(1210, 340, 51, 31));
        elapsedTimeShow_6->setFont(font2);
        label_8 = new QLabel(centralWidget);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setGeometry(QRect(910, 560, 61, 61));
        label_8->setPixmap(QPixmap(QString::fromUtf8("icon/compressor.png")));
        label_8->setScaledContents(true);
        label_9 = new QLabel(centralWidget);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setGeometry(QRect(1130, 560, 51, 61));
        label_9->setPixmap(QPixmap(QString::fromUtf8("icon/air-filter-white.png")));
        label_9->setScaledContents(true);
        label_10 = new QLabel(centralWidget);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setGeometry(QRect(960, 520, 141, 21));
        label_11 = new QLabel(centralWidget);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setGeometry(QRect(1170, 520, 121, 20));
        elapsedTimeShow_7 = new QLabel(centralWidget);
        elapsedTimeShow_7->setObjectName(QString::fromUtf8("elapsedTimeShow_7"));
        elapsedTimeShow_7->setGeometry(QRect(1200, 560, 101, 71));
        elapsedTimeShow_7->setFont(font2);
        elapsedTimeShow_8 = new QLabel(centralWidget);
        elapsedTimeShow_8->setObjectName(QString::fromUtf8("elapsedTimeShow_8"));
        elapsedTimeShow_8->setGeometry(QRect(1010, 550, 91, 71));
        elapsedTimeShow_8->setFont(font2);
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1348, 25));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        otLighteningDetails->setDefault(false);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        time_show->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p><span style=\" font-size:72pt;\">00:00</span></p></body></html>", nullptr));
        elapsedTimeLabel->setText(QCoreApplication::translate("MainWindow", "Elapsed Time", nullptr));
        elapsedTimeShow->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p><span style=\" font-size:72pt; color:#e41313;\">00:00:</span><span style=\" font-size:36pt; color:#e41313;\">00</span></p></body></html>", nullptr));
        toolButton->setText(QCoreApplication::translate("MainWindow", "Set Time", nullptr));
        toolButton_9->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
        toolButton_10->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
        toolPower_button->setText(QCoreApplication::translate("MainWindow", "STANDBY/CLEAN", nullptr));
        toolDownButton_1->setText(QCoreApplication::translate("MainWindow", "Down", nullptr));
        toolUpButton_1->setText(QCoreApplication::translate("MainWindow", "Up", nullptr));
        toolDownButton_2->setText(QCoreApplication::translate("MainWindow", "Down", nullptr));
        toolUpButton_2->setText(QCoreApplication::translate("MainWindow", "Up", nullptr));
        toolButton_16->setText(QCoreApplication::translate("MainWindow", "ADDITIONAL \n"
"CHRONO", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "Humidity", nullptr));
        label_2->setText(QString());
        label_4->setText(QString());
        label_5->setText(QCoreApplication::translate("MainWindow", "Temperature", nullptr));
        tick_show->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p>: 00</p></body></html>", nullptr));
        otLighteningDetails->setText(QCoreApplication::translate("MainWindow", "        Lighting", nullptr));
        ventiLationDetails->setText(QCoreApplication::translate("MainWindow", "     Ventilation", nullptr));
        gasIndicator->setText(QCoreApplication::translate("MainWindow", "                  Gas", nullptr));
        historyDetails->setText(QCoreApplication::translate("MainWindow", "           History", nullptr));
        multiMediaDetails->setText(QCoreApplication::translate("MainWindow", "   Multimedia", nullptr));
        btnOn->setText(QCoreApplication::translate("MainWindow", "On", nullptr));
        btnOff->setText(QCoreApplication::translate("MainWindow", "Off", nullptr));
        toolButton_3->setText(QCoreApplication::translate("MainWindow", "N2O", nullptr));
        toolButton_4->setText(QCoreApplication::translate("MainWindow", "AIR", nullptr));
        toolButton_5->setText(QCoreApplication::translate("MainWindow", "AIR7", nullptr));
        toolButton_6->setText(QCoreApplication::translate("MainWindow", "CO2", nullptr));
        toolButton_2->setText(QCoreApplication::translate("MainWindow", "O2", nullptr));
        toolButton_7->setText(QCoreApplication::translate("MainWindow", "VAC", nullptr));
        toolButton_8->setText(QCoreApplication::translate("MainWindow", "IPS", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Medical Gas", nullptr));
        toolSettings_button->setText(QCoreApplication::translate("MainWindow", "Settings", nullptr));
        toolHome_button->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
        toolPlay_button->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
        toolPause_button->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
        toolClose_button->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
        toolButton_19->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
        toolButton_20->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
        day_date_show->setText(QCoreApplication::translate("MainWindow", "Date Show", nullptr));
        toolButton_22->setText(QCoreApplication::translate("MainWindow", "Just Click Me", nullptr));
        time_label->setText(QCoreApplication::translate("MainWindow", "Time", nullptr));
        elapsedTimeShow_2->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p><span style=\" font-size:72pt; color:#e4ce13;\">00:00:</span><span style=\" font-size:36pt; color:#e4ce13;\">00</span></p></body></html>", nullptr));
        elapsedTimeLabel_2->setText(QCoreApplication::translate("MainWindow", "Anaesthesia  Time", nullptr));
        pushButton_6->setText(QCoreApplication::translate("MainWindow", "GRAPH", nullptr));
        pushButton_7->setText(QCoreApplication::translate("MainWindow", "GRAPH", nullptr));
        elapsedTimeShow_3->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">15.1</span></p></body></html>", nullptr));
        elapsedTimeShow_4->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">64.0</span></p></body></html>", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "Set", nullptr));
        label_7->setText(QCoreApplication::translate("MainWindow", "Set", nullptr));
        elapsedTimeShow_5->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">00</span></p><p><br/></p></body></html>", nullptr));
        elapsedTimeShow_6->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">00</span></p><p><br/></p></body></html>", nullptr));
        label_8->setText(QString());
        label_9->setText(QString());
        label_10->setText(QCoreApplication::translate("MainWindow", "Diffrential Pressure", nullptr));
        label_11->setText(QCoreApplication::translate("MainWindow", "Hepa Filter Status", nullptr));
        elapsedTimeShow_7->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">95%</span></p><p><br/></p></body></html>", nullptr));
        elapsedTimeShow_8->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">90</span></p></body></html>", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // MAINWINDOW_AUTO_H
