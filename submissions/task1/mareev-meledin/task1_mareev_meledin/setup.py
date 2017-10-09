from setuptools import setup


# Функция для загрузки подробного описания проекта.
def readme():
    with open('README.rst') as f:
        return f.read()


      # Имя пакета.
setup(name='task1_mareev_meledin',
      # Версия.
      version='1.4.48',
      # Краткое описание пакета.
      description='Workshop 3 course. Autumn 17-18. Exercise 1.',
      # Авторы.
      author='Mareev Gleb and Meledin Stanislav',
      # Контактный email.
      author_email='wowmagic.gm@gmail.com',
      # Лицензия, под которой распространяется пакет.
      license='MIT',
      # packages=['task1_mareev_meledin'],
      # Зависимости от других пакетов.
      install_requires=[
          'numpy',
          'scipy'
      ],
      # Подробное описание проекта.
      long_description=readme(),
      # Добавление в пакет файлов с данными.
      include_package_data=True,
      # Ключевые слова, описывающие пакет.
      keywords='task1 mareev maledin cs msu',
      # Адрес пакета в интернете.
      # url='http://github.com/storborg/funniest',
      # Категории пакета.
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Mathematics',
      ],
      zip_safe=False)
