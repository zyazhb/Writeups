<?php
error_reporting(0);
$KEY = "D0g3!!!";
$str = $_GET['str'];
//echo serialize($KEY);
if (unserialize($str) === "$KEY")
{
    echo "flag";
}
show_source(__FILE__);
?>
