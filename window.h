#pragma once
#include <QFormLayout>
#include <QLineEdit>
#include <QMessageBox>
#include <QProcess>
#include <QPushButton>
#include <QSpinBox>
#include <QStringList>
#include <QWidget>

class Window : public QWidget
{
	static const auto WIDTH = 100;
	QLineEdit* _input;
	QLineEdit* _output;
	QLineEdit* _inter;
	void run();
	void iPath();
	void oPath();
	void interPath();
public:
	Window();
	
};