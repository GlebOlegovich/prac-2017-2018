  # Задание:

  1. Необходимо написать функцию nash_equilibrium(a), которая принимает матрицу выигрыша и возвращает значение игры и оптимальные стратегии первого и второго игроков.
  2. Проиллюстрировать работу вашего кода путем решения нескольких игр и визуализации спектров оптимальных стратегий игроков в Jupyter.
     В частности, нужно привести игры, в которых:
     1. спектр оптимальной стратегии состоит из одной точки (т.е. существует равновесие Нэша в чистых стратегиях)
     2. спектр оптимальной стратегии неполон (т.е. некоторые чистые стратегии не используются)
     3. спектр оптимальной стратегии полон.
  3. Оформить ваше решение в виде пакета.
  4. Написать unit-тесты для функции nash_equilibrium(a).
  
  # Подход к решению:
  
Антагонистическая игра может быть представлена тройкой <X, Y, F>, где X и Y — множества стратегий первого и второго игроков,   соответственно; F — функция выигрыша первого игрока, ставящая в соответствие каждой паре стратегий (ситуации) (x,y), действительное  число, соответствующее выигрышу первого игрока в данной ситуации. Так как мы рассматриваем антагонистическую игру, функция F одновременно представляет и проигрыш второго игрока(он равен выигрышу первого).
Антагонистическая игра может быть представлена матрицей размера n на m. В этой матрице элемент aij=F(i,j).
Наша задача состоит в нахождении цены игры и оптимальных стратегий обоих игроков. Оптимальная стратегия первого игрока обладает тем свойством, что при любом поведении второго игрока обеспечивает выигрыш первому игроку, не меньший, чем цена игры. Для решения задачи сведем ее к паре двойственных задач линейного программирования. Это делается с помощью определений и подробно описано здесь: https://math.semestr.ru/games/linear-programming.php
  # Реализация решения:
  
 С массивами работаем с помощью библиотеки numpy:
 https://pythonworld.ru/numpy/1.html
 
 Пару двойственных задач линейного программирования будем решать с помощью функции linprog библиотеки scipy:
 https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.optimize.linprog.html
 
 После получения решения задачи нам надо визуализировать его. Это делается с помощью библиотеки matplotlib:  https://pythonworld.ru/novosti-mira-python/scientific-graphics-in-python.html
 
 После визуализации необходимо протестировать программу. Тесты будем делать с помощью библиотеки unittest:
 http://devpractice.ru/unit-testing-in-python-part-1/

  
  # Запуск программы:
  
   В командной строке Windows 10 пишем: cd путь-к-папке-с-прогарммой.
   Далее пишем: jupyter-notebook.
   Открываем файл с названием nash.ipynb.
   
   # Необходимое ПО:
   
   Windows 10, Anaconda3, Python 3.6, Jupyter Notebook.
     
   ## Используемые библиотеки:
   1) numpy
   2) scipy
   3) matplotlib
   4) unittest
   
   # Участники:
   Павлов Антон Сергеевич (311 группа):
   1) Разработка алгоритма выполнения программы
   2) Программная реализация задачи(процедуры nash_equilibrium)
   3) Реализация unit-тестов
   4) Подготовка отчетности
   
   Сметанин Даниил Алексеевич (311 группа):
   1) Разработка алгоритма выполнения программы
   2) Графическая демонстрация
   3) Оформления задания в виде пакетов
   4) Подоготовка файла Readme