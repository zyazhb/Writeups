<?php
class example{
    public $test;
    function __call($method,$parm){ //when a method not exist
         echo exec($parm[0]);
         echo "<br>";
        }
    function __wakeup(){
        $this->no($this->test);
    }
}
#$new = new example();
#$new->test = "whoami";
#echo serialize($new);
$ss = 'O:7:"example":1:{s:4:"test";s:6:"whoami";}';
unserialize($ss);
?>
