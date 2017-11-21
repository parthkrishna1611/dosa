<?php
$name = $_GET['name'];
$cmd = "python3 scraper.py ".$name;
echo "$cmd";

echo shell_exec($cmd." 2>&1");

echo shell_exec($cmd);
$mean = file_get_contents('/home/parth/Desktop/proj/meaning.txt');
echo $mean;
$ex = file_get_contents('/home/parth/Desktop/proj/example.txt');
echo $ex;
?>
