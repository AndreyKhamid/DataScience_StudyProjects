
# <center> Анализ вакансий Headhunter </center>
## Оглавление
1. [Описание проекта](#title1)
2. [Описание данных](#title2)
3. [Зависимости](#title3)
4. [Установка проекта](#title4)
5. [Использование проекта](#title5)
6. [Авторы](#title6)
7. [Выводы](#title7)

## <a id="title1">Описание проекта</a>

**Данный проект включает в себя несколько этапов:**  

- знакомство с данными;  
- предварительный анализ данных;  
- детальный анализ вакансий;  
- анализ работодателей;  
- предметный анализ.

**Данный проект** направлен на демонстрацию анализа данных посредством инструментов СУБД *PostgresSQL*, в т.ч. посредством запросов *SQL* через язык *Python*.

**О структуре проекта:**
* [Project_2_анализ_вакансий.ipynb](https://github.com/AndreyKhamid/DataScience_StudyProjects/blob/main/PROJECT-2.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D0%B2%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%B8%D0%B9%20%D0%B8%D0%B7%20HeadHunter/Project_2_%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7_%D0%B2%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%B8%D0%B9.ipynb) - jupyter-ноутбук, содержащий основной код проекта, в котором демонстрируются методы и подходы решения задач по анализу данных с использованием запросов *SQL* к СУБД *PostgresSQL*. 


## <a id="title2">Описание данных</a>
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


## <a id="title3">Используемые зависимости</a>
* Python (3.9):
    * [pandas (2.2.1)](https://pandas.pydata.org)
    * [psycopg2](https://www.psycopg.org/)
    * [matplotlib (3.4.3)](https://matplotlib.org)
    * [seaborn (0.13.2)](https://seaborn.pydata.org)
    * [requests (2.31.0)](https://requests.readthedocs.io/en/latest/)
    * [BeautifulSoap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## <a id="title4">Установка проекта</a>

```PowerShell
git clone https://github.com/AndreyKhamid/DataScience_StudyProjects.git
```

## <a id="title5">Использование</a>
Вся информация о работе представлена в jupyter-ноутбуке *Project_2_анализ_вакансий.ipynb.*

## <a id="title6">Авторы</a>

* [Khamidulin Andrey](https://github.com/AndreyKhamid)

## <a id="title7">Выводы</a>

В результате проведенной работы по анализу вакансий Headhunter сделаны выводы о количестве вакансий в разных регионах, доминирующих работодателях на рынке труда, а также о требованиях к соискателям, которые необходимо учитывать при размещении вакансий в настоящее время.
