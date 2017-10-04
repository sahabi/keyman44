#include "sendwidnow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    SendWidnow w;
    w.show();

    return a.exec();
}
