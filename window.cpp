#include <QFormLayout>
#include <QLineEdit>
#include <QMessageBox>
#include <QProcess>
#include <QPushButton>
#include <QSpinBox>
#include <QStringList>
#include <QWidget>
#include <QLabel>
#include "window.h"
#include <iostream>
#include <QFileDialog>

void Window::run()
{
	QStringList arguments;
	arguments << "C:\\lab4\\script.py";
	arguments << QString(_input->text());
	arguments << QString(_output->text());

	if (_input->text().isEmpty() || _output->text().isEmpty() || _inter->text().isEmpty())
	{
		QMessageBox::critical(this, "Error", "Empty field");
		return;
	}

	QProcess process(this);
	process.start(_inter->text(), arguments);
	process.waitForFinished();

	auto err = process.readAllStandardError();
	if(err.size() != 0)
	{
		QMessageBox::warning(this, "Warning", err);
		return;
	}
	
	QMessageBox::information(this, "Information", "Complete!");
	
}

void Window::iPath()
{
	auto text = QFileDialog::getOpenFileName(this, "Directory input file.", "C:\\lab4");
	_input->setText(text);
}

void Window::oPath()
{
	auto text = QFileDialog::getOpenFileName(this, "Directory output file.", "C:\\lab4");
	_output->setText(text);
}

void Window::interPath()
{
	auto text = QFileDialog::getOpenFileName(this, "Directory interpreter.", "C:\\Python");
	_inter->setText(text);
}

Window::Window()
{

	_inter = new QLineEdit;
	auto interLabel = new QLabel("Interpeter PATH:");
	//_inter->setFixedWidth(WIDTH);

	_input = new QLineEdit;
	//_input->setFixedWidth(WIDTH);
	auto inputLabel = new QLabel("Input PATH: ");

	_output = new QLineEdit;
	//_output->setFixedWidth(WIDTH);
	auto outputLabel = new QLabel("Output PATH: ");
	
	auto button = new QPushButton("RUN!");
	connect(button, &QPushButton::clicked, this, &Window::run);

	auto iButton = new QPushButton("Select");
	connect(iButton, &QPushButton::clicked, this, &Window::iPath);

	auto oButton = new QPushButton("Select");
	connect(oButton, &QPushButton::clicked, this, &Window::oPath);

	auto interButton = new QPushButton("Select");
	connect(interButton, &QPushButton::clicked, this, &Window::interPath);

	auto layout = new QGridLayout;
	layout->addWidget(_inter, 0, 1);
	layout->addWidget(interLabel, 0, 0);
	layout->setAlignment(interLabel, Qt::AlignRight);
	layout->addWidget(interButton, 0, 2);
	layout->addWidget(_input, 1, 1);
	layout->addWidget(inputLabel, 1, 0);
	layout->setAlignment(inputLabel, Qt::AlignRight);
	layout->addWidget(iButton, 1, 2);
	layout->addWidget(_output, 2, 1);
	layout->addWidget(outputLabel, 2, 0);
	layout->setAlignment(outputLabel, Qt::AlignRight);
	layout->addWidget(oButton, 2, 2);
	layout->addWidget(button, 3, 0, 1, 3);

	setLayout(layout);
	setFixedSize(sizeHint());
}