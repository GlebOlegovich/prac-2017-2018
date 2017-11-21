# Задание 1

## Цель

Задание 1 состоит в численном решении антагонистической матричной игры. В рамках данного задания мы должны
написать код, решающий матричную игру путем сведения ее к паре двойственных задач линейного программирования,
проиллюстрировать работу данного кода путем визуализации спектров оптимальных стратегий.
Цель задания 1 заключается в том, чтобы познакомиться с языком программирования Python, библиотекой SciPy и интерактивной средой разработки Jupyter.

## Краткое описание задания

1) *(50 баллов)* Необходимо написать функцию ```nash_equilibrium(a)```, которая принимает матрицу выигрыша и возвращает значение игры и оптимальные стратегии первого и второго игроков.

2) *(50 баллов)* Проиллюстрировать работу вашего кода путем решения нескольких игр и визуализации спектров оптимальных стратегий игроков в Jupyter. В частности, нужно привести игры, в которых:
    1) спектр оптимальной стратегии состоит из одной точки (т.е. существует равновесие Нэша в чистых стратегиях),
    2) спектр оптимальной стратегии неполон (т.е. некоторые чистые стратегии не используются),
    3) спектр оптимальной стратегии полон.

## Подход к решению

1. Написание функции ```nash_equilibrium(a)```
* На вход подается матрица выигрыша, реализующая антагонистическую матричную игру
* Задача сводится к решению пары двойственных задач линейного программирования
* Решение задач находим с помощью симплекс-метода, который позволяет получить на выходе оптимальные стратегии игроков и значение игры

2. Написание части, реализующей визуализацию спектров оптимальных стратегий игроков в Jupyter
* Необходимо использовать объекты и методы из библиотеки ```matplotlib.pyplot``` и подобрать необходимые матрицы, чтобы визуализировать решение с помощью гистограммы

## Аналитическое пояснение

Необходимо решить антагонистическую матричную игру. Игрой называется тройка <A, {Bi} i из A, {Hi} i из A>, где A = {1,2, ..., n} - множество занумерованных игроков, Bi - множество возможных действий i-го игрока; s = (s1,...,sn) - ситуация, si из Bi, Hi(s) называется функцией выигрыша игрока i.
Матричная игра называется антагонистической, если в ней участвуют два игрока и значения функций выигрыша в каждой ситуации равны по величине и противоположны по знаку.
Решением матричной игры называется процесс нахождения её значения и оптимальных стратегий игроков.
Чистой стратегией игрока называется стратегия, однозначно выбираемая игроком.
Смешанной стратегией игрока называется произвольное распределение вероятностей на множестве его чистых стратегий. Антагонистическая игра задана матрицей выигрыша А=(aij) размера n на m, для которой необходимо найти цену игры и оптимальные стратегии игроков.
Прежде чем применять стандартный подход: сведение исходной задачи к двойственной задаче линейного программирования, необходимо проверить: не содержит ли матрица седловой точки, тогда задача разрешена в чистых стратегиях (существует равновесие Нэша).
Если aij - седловая точка матрицы А (aij - минимальный элемент в строке i и максимальный элемент в строке j), то цена игры равна aij, и первый игрок выбирает стратегию i, а второй игрок стратегию j.
Если матрица игры A не имеет седловой точки, то исходная задача сводится к двойственной задаче линейного программирования. Благодаря этому становится возможным применение симплекс-метода для решения матричных игр.

Алгоритм симплекс-метода заключается в том, что из множества вершин, принадлежащих границе множества решений системы неравенств, выбрается такая вершина, в которой значение целевой функции достигает максимума (минимума). По определенному правилу находится первоначальный опорный план (некоторая вершина области ограничений). Проверяется, является ли план оптимальным. Если да, то задача решена. Если нет, то переходим к другому улучшенному плану - к другой вершине. Значение целевой функции на этом плане (в этой вершине) заведомо лучше, чем в предыдущей. Алгоритм перехода осуществляется с помощью некоторого вычислительного шага, который удобно записывать в виде таблиц, называемых симплекс-таблицами. Так как вершин конечное число, то за конечное число шагов мы приходим к оптимальному решению.
Шаги:
    *1) Переход к канонической форме задачи линейного программирования путем введения неотрицательных дополнительных балансовых (базисных) переменных. Запись задачи в симплекс-таблицу. Между системой ограничений задачи и симплекс-таблицей взаимно-однозначное соответствие. Строчек в таблице столько, сколько равенств в системе ограничений, а столбцов - столько, сколько свободных переменных. Базисные переменные заполняют первый столбец, свободные - верхнюю строку таблицы. Нижняя строка называется индексной, в ней записываются коэффициенты при переменных в целевой функции. В правом нижнем углу первоначально записывается 0, если в функции нет свободного члена; если есть, то он записывается с противоположным знаком. На этом месте (в правом нижнем углу) будет значение целевой функции, которое при переходе от одной таблицы к другой должно увеличиваться по модулю.
    *2) Проверка опорного плана на оптимальность. Для этого необходимо анализировать строку целевой функции F. Если найдется хотя бы один коэффициент индексной строки меньше нуля, то план не оптимальный, и его необходимо улучшить. 
   * 3) Улучшение опорного плана. Из отрицательных коэффициентов индексной строки выбирается наибольший по абсолютной величине. Затем элементы столбца свободных членов симплексной таблицы делит на элементы того же знака ведущего столбца. Далее идет построение нового опорного плана. Переход к новому опорному плану осуществляется в результате пересчета симплексной таблицы методом Жордана—Гаусса.
  *  4) Выписываем оптимальное решение.

## Структура программы

**nash_equilibrium** - функция для поиска равновесия Нэша - в результате работы функции в count игровая сумма, в p[1] - стратегия первого игрока, в p[2] - стратегия второго игрока.
**art(p,q)** - рисуем гистограмму для визуализации результатов.
Функция **nash_equilibrium(a)**  получает на вход матрицу игры, сводит нахождение стратегий игроков к паре задач линейного программирования: максимизирует минимальный выигрыш первого игрока и минимизирует максимальный выигрыш второго
**m = А.shape[0]**  - в матрице m строк - количество чистых стратегий первого игрока
**line1 = np.ones((m))**  - создаем стобец длины m, заполняем его “1”
**Atr = -A.transpose( )** - транспонируем матрицу игры
**matrix = linprog(line1, A_ub = A, b_ub = koef1)** - с помощью функции linprog получаем решение задачи:
line1*𝑇*𝑥 → 𝑚𝑖𝑛
𝐴*𝑥 ≤ koef1
𝐴_𝑒𝑞*𝑥 = 𝑏_𝑒𝑞
𝑥 ≥ 0
**np.amin(A)** - находим минимальный элемент для каждой строки.
**np.ones(n)** - создаем вектор из n единиц.
Функция **art(p,q)** - строит графики, визуализирующие оптимальные стратегии игроков.
**st = plt.figure()** - создаем график для первого игрока
**plt.bar(f1, p)** - получаем вертикальную диаграмму
**plt.xlabel('Стратегия')** - подпись оси x
**plt.title("стратегия 1 игрока: ")** - написание заголовка 
**plt.show()** - вывод изображения на экран
**plt.ylabel(‘Вероятность')** - подпись оси y
**plt.xlim(0,len(p))** - устанавливаем предельные значения по х
**plt.ylim(0, np.max(p)+1)** - устанавливаем предельные значения по у


## Инструкции по запуску

```./task1.py``` - для первой части
Cell -> Run All  - для Jupiter

## Необходимое ПО

Для удобной и наглядной работы с Python можно воспользоваться интерактивной средой разработки Jupyter, вводя в окне терминала jupiter notebook  и открывая нужные проекты (в частности для запуска файлов с расширением .ipynb необходимо открыть файл и выбрать в верхнем меню Cell -> Run all)

### Библиотеки:

Для ```nash_equilibrium(a)```
* **SciPy** — библиотека с открытым исходным кодом, предназначенная для выполнения научных и инженерных расчётов. Она необходима для функции linprog из пакета scipy.optimize, который содержит в себе множество алгоритмов оптимизации. Цель функции linprog - минимизация линейной объективной функции с линейными ограничениями равенства и неравенства.
* **NumPy** — библиотека с открытым исходным с такими возможностями, как поддержка многомерных массивов (включая матрицы), поддержка высокоуровневых математических функций, предназначенных для работы с многомерными массивами.

Для второй части задания
* **Matplotlib** - библиотека для работы с графиками

### Программы:

1) **Wing 101**
2) **Jupyter** — инструмент для интерактивной работы с Python-кодом

## Участники

Капитанов Филипп - 312 группа
> Составил алгоритм для решения задачи
> Тестировал программу
> реализовал art(p,q) и построение диаграмм
Мешина Злата - 312 группа
> Встроила симплекс метод в программу
> Составила примеры, заявленные в задании
> реализовала nash_equilibrium