<img src='images/kaggle.png' width=150px>

<img src='images/booking.png' width=300px>

# <center> Построение модели на основе данных рейтинга отелей Booking.com </center>

## Оглавление
1. [Описание проекта](#title1)
2. [Описание данных](#title2)
3. [Зависимости](#title3)
4. [Установка проекта](#title4)
5. [Использование проекта](#title5)
6. [Авторы](#title6)
7. [Выводы](#title7)

## <a id="title1">Описание проекта</a>

Исходные данные и задачи проекта взяты из соревнования на платформе ***Kaggle***, а именно из [[SF-DST] Booking reviews](https://www.kaggle.com/competitions/sf-booking) (Прогнозирование рейтинга отеля на Booking), представленное от платформы ***Skill Factory***. 

**Бизнес-задача проекта:**  
> Мы работаем датасаентистом в компании *Booking.com*. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов нахождения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель играет нечестно, и его стоит проверить.

**Данный проект включает в себя несколько этапов:**  

- предварительная работа с данными (подгрузка, описательный анализ исходных данных, их очистка);  

- разведывательный анализ данных (*Exploratory Data Analysis*), в т.ч.:
    - визуальный анализ данных;
    - проектирование признаков (*Feature Engineering*);
    - кодирование признаков (*Feature Coding*);
    - отбор признаков (*Feature Sellection*).

- обучение модели (*Model Building*).

**Данный проект** направлен на построение модели предсказания оценки отеля `reviewer_score`. Метрика качества модели определяется по *MAPE* *(Mean Absolute Precentage Error)*. Основаня задача проекта – демонстрация навыков разведывательного анализа данных (*EDA*).

**О структуре проекта:**
* [project-3-eda-feature-engineering.ipynb](https://github.com/AndreyKhamid/DataScience_StudyProjects/blob/main/PROJECT-3._EDA_+_Feature_Engineering._Соревнование_на_Kaggle\PROJECT-3_(Kaggle_version)\project-3-eda-feature-engineering.ipynb) - jupyter-ноутбук, содержащий основной код проекта, в котором демонстрируются навыки *EDA* и *MB*.

## <a id="title2">Описание данных</a>
**Файлы для соревнования:**  
- `hotels_train.csv` - набор данных для обучения;  
- `hotels_test.csv` - набор данных для оценки качества;  
- `submission.csv` - файл сабмишна в нужном формате.

***Указанные файлы необходимо скачать по [ссылке](https://drive.google.com/file/d/1gEuAEHzkvx7TTI3MblPPAAoH1jDU9vaM/view?usp=sharing)***

## <a id="title3">Используемые зависимости</a>
* Python (3.9):
    * [pandas (2.2.2)](https://pandas.pydata.org)
    * [numpy (1.26.4)](https://numpy.org/)
    * [matplotlib (3.9.0)](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
    * [seaborn (0.13.2)](https://seaborn.pydata.org/)
    * [statistics (1.0.3.5)](https://docs.python.org/3/library/statistics.html)
    * [category_encoders (2.6.3)](https://contrib.scikit-learn.org/category_encoders/)
    * [sklearn (1.5.0)](https://scikit-learn.org/stable/)
    * [scipy (1.13.1)](https://scipy.org/)
    * [termcolor (2.4.0)](https://pypi.org/project/termcolor/)
    * [geopy (2.4.1)](https://geopy.readthedocs.io/)


## <a id="title4">Установка проекта</a>

```PowerShell
git clone https://github.com/AndreyKhamid/DataScience_StudyProjects.git
```

## <a id="title5">Использование</a>

- Основаня информация о работе представлена в jupyter-ноутбуке *project-3-eda-feature-engineering.ipynb*;  

- Итоговый сабмишн соревнования представлен в файле *submission_result.csv*.

- Файл *requirements.txt* – версии библитоек для воспроизводимости кода. Установка:
   
   ```PowerShell
   pip install -r requirements.txt
   ```

## <a id="title6">Авторы</a>

* [Khamidulin Andrey](https://github.com/AndreyKhamid)

## <a id="title7">Выводы</a>

В результате проведенной работы метрика качества *MAPE* модели предсказания оценки отеля от рецензента получена на уровне 13,61 %, вместе с тем отмечается как положительная сторона данной работы (хоть и не с выском показателем итоговой метрики *MAPE*) проектирование признака пропорции положительных слов в отзые и отрицательных слов `review_total_positive_word_prop`, который в построенной модели оказал решающую роль в предсказании.
