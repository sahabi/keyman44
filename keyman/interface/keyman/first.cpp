#include "first.h"
#include "ui_first.h"

first::first(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::first)
{
    ui->setupUi(this);
}

first::~first()
{
    delete ui;
}
