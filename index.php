<?php
$cat = "http://www.liveinternet.ru/rating/ru/genealogy/index.html?page="; // url для загрузки файлов
$file = fopen("result.txt", "a+"); // открываем файл для записи результатов

for ($j = 1; $j<=9; $j++) { //  запускаем цикл на 9 страниц
	$url = file_get_contents($cat.$j); // парсим каждую страницу в цикле от первой до девятой
	preg_match_all('/<a name="(.*)"/', $url, $mathces); // регуляркой вытаскивам нужные url и помещаем в массив $matches

	$count = count($mathces[0]); // считаем количество полученных url (в данном случае тридцать
	for ($i = 0; $i<$count; $i++) {
		fwrite ($file, $mathces[1][$i]."\n"); // Записываем в файл результаты, каждый с новой строчки.
	}
}
fclose($file);
echo 'Готово';
?>