<!DOCTYPE html>

<html>

    <head>
        <meta charset="utf-8">
        <title></title>
</head>
<body>

    <?php
    echo("<h1>String functions demo</h1>");
    echo("<hr>");
    $phrase = "This is a string<br>";
    echo("this is our starting string: $phrase <br>");
    echo("it is stored in \$phrase, which is a variable");
    echo("<hr>");

    echo("this is the strtolower function: ");
    echo(strtolower($phrase));

    echo("<br>this is the strtoupper function: ");
    echo(strtoupper($phrase));

    echo("<br>the strlen function tells us the length of the string: ");
    echo(strlen($phrase));
    echo("<br>");

    echo("<br>by typing echo \$phrase[2] we can access the third character of the string (since we start counting at 0): ");
    echo($phrase[2]);
    echo("<br>");

    echo("<br>by typing \$phrase[2] = 'x' we can access the third character of the string and change it to a x: ");
    $phrase[2] = 'x';
    echo($phrase);
    $phrase = "This is a string";
    echo("<br>");

    echo "by using the str_replace function, we can replace words in the string.  example: string -> sentence. <br>";
    echo str_replace("string", "sentence", $phrase);
    echo("<br>");
    echo("<br>");

    echo "by using the substr function, we can grab just a portion of a string. For this example, we are taking just the word 'is' out of the string.<br>";
    echo substr($phrase, 5,2);
    ?>


</body>


</html>