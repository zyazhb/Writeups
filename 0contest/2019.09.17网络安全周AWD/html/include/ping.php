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
	
	unserialize(base64_decode($_GET['ip']));
 
?>
