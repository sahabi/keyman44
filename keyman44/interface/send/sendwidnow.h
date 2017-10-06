#ifndef SENDWIDNOW_H
#define SENDWIDNOW_H

#include <QMainWindow>

namespace Ui {
class SendWidnow;
}

class SendWidnow : public QMainWindow
{
    Q_OBJECT

public:
    explicit SendWidnow(QWidget *parent = 0);
    ~SendWidnow();

private:
    Ui::SendWidnow *ui;
};

#endif // SENDWIDNOW_H
