<?php
if (PHP_SAPI !== 'cli') {
    die();
}
$nome = trim(fgets(STDIN));
echo "Olá, $nome\n";
