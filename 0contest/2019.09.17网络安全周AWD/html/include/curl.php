<?php

        if(isset($_GET['address'])){
                $address = $_GET['address'];
                if(filter_var($address,FILTER_VALIDATE_URL)){
                        $filter_url = parse_url($address);
                        $url = $filter_url['host'].'?'.$filter_url['query'];
                        if(preg_match('/127.0.0.1/',$url)){
                                system('curl -v -s '.$url);
                        }
                }
        }

?>

