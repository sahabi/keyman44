#include "sendwidnow.h"
#include "ui_sendwidnow.h"

SendWidnow::SendWidnow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::SendWidnow)
{
    ui->setupUi(this);
}

SendWidnow::~SendWidnow()
{
    delete ui;
}
