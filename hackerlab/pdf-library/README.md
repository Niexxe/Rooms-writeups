# PDF Library — HackerLab
*Level: Easy*






![Шаг 1](images/01.png)

Переходим по ip и видим что у нас есть 2 ссылки на файлы\
![Шаг 2](images/02.png)

1.  ![Шаг 3](images/03.png)

2.  ![Шаг 4](images/04.png)

Сделаем сканирование через nmap

nmap -sC -sV 62.173.140.174 -p 16081

![Шаг 5](images/05.png)

Результат:

-   Открыт порт 16081 → HTTP (Apache)

-   Заголовок страницы: PDF-библиотека (как видно из http-title)

-   Нет других открытых портов

**Переходим в DevTools → Network, и вот что мы видим:**

При клике на \"Открыть\" файл grafik-kursov.pdf --- браузер делает
запрос:

GET /index.php?file=67726166696b2d6b7572736f762e706466

**А это --- не обычное имя файла, а hex-кодировка**

![Шаг 6](images/06.png)

декодируем его из hex в ASCII чтобы убедиться:

![Шаг 7](images/07.png)

Попробуем закодировать фразу «flag.pdf» и посмотрим что будет при
отправке запроса

![Шаг 8](images/08.png)

Теперь оправим сам запрос через curl

![Шаг 9](images/09.png)

Получили ответ что «файл не найден»

**Попробуем получить Index.php**

Закодируем index.php

![Шаг 10](images/10.png)

Здесь мы видим подсказку

// \$txt_files = array_slice(\[\'test.txt\',
\'flag_for_hackerlab_ctfplayers.txt\'\], 0, 2); // Moved to upper
directory

flag_for_hackerlab_ctfplayers.txt -- название флага

/ он находится в выше стоящей директории

Закодируем ее в hex **../flag_for_hackerlab_ctfplayers.txt**

И отправим запрос через curl

curl
\'http://62.173.140.174:16081/index.php?file=2e2e2f666c61675f666f725f6861636b65726c61625f637466706c61796572732e747874\'

И получаем флаг!



![Шаг 11](images/11.png)


---

[← Все write-ups](../../README.md)
