
# <center> Анализ вакансий Headhunter </center>
## Оглавление
1. [Описание проекта](#Описание-проекта)
2. [Описание данных](#Описание-данных)
3. [Зависимости](#Зависимости)
4. [Установка проекта](#Установка-проекта)
5. [Использование проекта](#Использование-проекта)
6. [Авторы](#Авторы)
7. [Выводы](Использование-проекта)

## Описание проекта

**Данный проект включает в себя несколько этапов:**  

- знакомство с данными;  
- предварительный анализ данных;  
- детальный анализ вакансий;  
- анализ работодателей;  
- предметный анализ.

**Данный проект** направлен на демонстрацию анализа данных посредством инструментов СУБД *PostgresSQL*, в т.ч. посредством запросов *SQL* через язык *Python*.

**О структуре проекта:**
* [Project_2_анализ_вакансий.ipynb](./Project_2_анализ_вакансий.ipynb) - jupyter-ноутбук, содержащий основной код проекта, в котором демонстрируются методы и подходы решения задач по анализу данных с использованием запросов *SQL* к СУБД *PostgresSQL*. 


## Описание данных
В этом проекте используются таблицы, находящиеся в схеме `public` базы данных `project_sql`.

![](https://lms.skillfactory.ru/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block@SQL_pj2_2_1.png)

- Таблица *VACANCIES* хранит в себе данные по вакансиям и содержит следующие столбцы:
![](https://lms.skillfactory.ru/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block@SQL_pj2_2_2.png)

- Таблица-справочник *AREAS*, которая хранит код региона и его название:
![](https://lms.skillfactory.ru/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block@SQL_pj2_2_3.png)

- Таблица-справочник *EMPLOYERS* со списком работодателей:
![](https://lms.skillfactory.ru/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block@SQL_pj2_2_4.png)

- Таблица-справочник вариантов сфер деятельности работодателей *INDUSTRIES*:
![](https://lms.skillfactory.ru/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block@SQL_pj2_2_5.png)

- Дополнительная таблица *EMPLOYERS_INDUSTRIES*, которая существует для организации связи между работодателями и сферами их деятельности:
![](https://lms.skillfactory.ru/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block@SQL_pj2_2_6.png)


## Используемые зависимости
* Python (3.9):
    * [pandas (2.2.1)](https://pandas.pydata.org)
    * [psycopg2](https://www.psycopg.org/)
    * [matplotlib (3.4.3)](https://matplotlib.org)
    * [seaborn (0.13.2)](https://seaborn.pydata.org)
    * [requests (2.31.0)](https://requests.readthedocs.io/en/latest/)
    * [BeautifulSoap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Установка проекта

```PowerShell
git clone https://github.com/AndreyKhamid/DataScience_StudyProjects.git
```

## Использование
Вся информация о работе представлена в jupyter-ноутбуке *Project_2_анализ_вакансий.ipynb.*

## Авторы

* [Khamidulin Andrey](https://github.com/AndreyKhamid)

## Выводы

В результате проведенной работы по анализу вакансий Headhunter сделаны выводы о количестве вакансий в разных регионах, доминирующих работодателях на рынке труда, а также о требованиях к соискателям, которые необходимо учитывать при размещении вакансий в настоящее время.
