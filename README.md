# HandCV
Hand Control

# Hand Контроллер
### Описание
Благодаря этому проекту можно будет управлять компьютером при помощи пальцев рук.
### Технологии
- Python 3.10
- absl-py==1.3.0
- attrs==22.1.0
- contourpy==1.0.5
- cvzone==1.5.6
- cycler==0.11.0
- fonttools==4.37.4
- kiwisolver==1.4.4
- matplotlib==3.6.1
- mediapipe==0.8.11
- numpy==1.23.4
- opencv-contrib-python==4.6.0.66
- opencv-python==4.6.0.66
- packaging==21.3
- Pillow==9.2.0
- protobuf==3.20.3
- pyparsing==3.0.9
- python-dateutil==2.8.2
- six==1.16.0

### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Замените в файле venv\lib\site-packages\cvzone\HandTrackingModule.py line 143
```
x1, y1, u1 = p1
x2, y2, u1 = p2
```

- В папке с файлом main.py выполните команду:
```
python main.py
```
### Автор
Majid