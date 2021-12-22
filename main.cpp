#include <QApplication>
#include <QLineEdit>
#include <QLabel>
#include <QPushButton>
#include <QWidget>
#include "window.h"

int main(int argc, char** argv) {
    QApplication app(argc, argv);

    Window window;
    window.show();

    return QApplication::exec();
}
