BComp-ng Helper v 2.1
	
	Данный проект - набор утилит для помощи в работе с БЭВМ.

	Перемещать файлы проекта нельзя.
	
	Основа - измененная bcomp-ng.jar, а именно изменены компоненты 
	Register, Memory(Соответсвующие .class файлы лежат в папке .class)
	в пакете ru/ifmo/cs/components в самом jar файле(Открыть в WinRar)

	Список утилит (будет дополняться):
		runner.py
		executor.exe
		reporter.py v 1.0

runner.py

	Эта утилита предназначена для инициализации BComp-ng.jar 
	Вашей программой. Она загружает Вашу программу в память и
	устанавливает IP на начало программы.

	Она переводит файл program.txt в !ip_init.txt !mem_init.txt, которые использует bcomp-ng.jar для инициализации,
	поэтому после изменения program.txt надо обязательно ее запустить, чтобы изменения вступили в силу.
	
	Для работы с данной программой надо записать Вашу 
	программу в файл 'user/porgram.txt'.
	Этот файл должен иметь структуру:
		Первая строка - 4-значный 16-ричный адрес начала Вашей программы.
		Далее инициализация ячеек:
			Первая строка - восклицательный знак и 4-значный адрес памяти
			с которой начнется запись.
			Следующие строки(хотя бы одна строка) - 4-значные значения ячеек памяти.  
	Например:
		057C		- адрес начала программы
		!0571		- Начальная ячейка инициализации памяти. 		(Часто на практике 
		0200		- Значений памяти, которое будет присвоено ячейке 571	это начало одной из функций 
		EE19		- Значений памяти, которое будет присвоено ячейке 572	в Вашей программе.)
		AE16		- 573
		0C00		- 574
		D6C3    	...
		0800
		0740
		0C00
		D6C3
		!059С            - Следующая начальная ячейка инициализации памяти.
		0700		 - Значений памяти, которое будет присвоено ячейке 59С
		4E05		 - 59D
		EE04		 - 59E
		0100		 ...
		0000
		0000
		0000
		0193
		!06C3		- И еще одна начальная ячейка инициализации памяти.
		AC01
		F001
		F306
		7E08
		F804
		F003


executor.exe
	
	Эта утилита предназначена для исполнения вашей программы 
	и составления примитивного файла трассировки.

	Для взаимодействия с bcom-ng.jar использует функции WinApi,
	следовательно работает только на Windows

	Перед запуском данной программы необходимо запустить 
	bcomp-ng.jar(Которая лежит в этой папке: с другой работать не будет.)
	
	При исполнении данной утилиты нельзя переключаться на другие окна 
	и скрывать данное окно.

reporter.py v 1.0

	Эта утилита составляет таблицу трассировки, таблицу подпрограмм в файле 
	Word reporter/trace.docx.

	Для работы данной программы надо скачать:
		pip install python-docx
			