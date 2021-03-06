<?php
# MetInfo Enterprise Content Management System
# Copyright (C) MetInfo Co.,Ltd (http://www.metinfo.cn). All rights reserved.

defined('IN_MET') or exit('No permission');

/**
 * parameter标签类
 */

class parameter_op {
	public $preg;
	/**
	 * 初始化，继承类需要调用
	*/
	public function __construct() {
		global $_M;
		if(IN_ADMIN){
			$this->preg = '/^info_([0-9]+)/';
		}else{
			$this->preg = '/^para([0-9]+)/';
		}
	}

	public function name_to_num($module) {
		switch ($module) {
			case 'product':
				$mod = 3;
			break;
			case 'download':
				$mod = 4;
			break;
			case 'img':
				$mod = 5;
			break;
			case 'message':
				$mod = 6;
			break;
			case 'job':
				$mod = 7;
			break;
			case 'feedback':
				$mod = 8;
			break;
		}
		return $mod;
	}

	/**
	 * 获取字段内容，前台产品，图片，下载模块使用
	 * @param  string  $module  表单模块类型(feedback, message, job)
	 * @param  number  $id      一级栏目
	 * @return array            表单数组
	 */
	public function insert($listid, $module, $paras) {
		global $_M;
		$mod = $this->name_to_num($module);
		$list = array();
		foreach ($paras as $key => $val) {
			preg_match($this->preg, $key, $out);
			if ($out[1]) {
				$list[$out[1]] .= $val.',';
			}
		}
		foreach ($list as $key => $val) {
			$val = trim($val, ',');
			$paraid = load::mod_class('parameter/parameter_database', 'new')->insert_list($listid, $key, $val, '', $_M['lang'], $module);
		}
		return ture;
	}

	/**
	 * 获取字段内容，前台产品，图片，下载模块使用
	 * @param  string  $module  表单模块类型(feedback, message, job)
	 * @param  number  $id      一级栏目
	 * @return array            表单数组
	 */
	public function update($listid, $module, $paras) {
		global $_M;
		$mod = $this->name_to_num($module);
		$list = array();
		foreach ($paras as $key => $val) {
			preg_match($this->preg, $key, $out);
			if ($out[1]) {
				$list[$out[1]] .= $val.',';
			}
		}
		foreach ($list as $key => $val) {
			$val = trim($val, ',');
			$paraid = load::mod_class('parameter/parameter_database', 'new')->update_list($listid, $key, $val, '', $module);
		}
		return ture;
	}

	public function paratem($listid,$module,$class1,$class2,$class3){
		global $_M;
		if($listid)$para = $this->get_para($listid,$module,$class1,$class2,$class3);
		$paralist = $this->get_para_list($module,$class1,$class2,$class3);
		require PATH_WEB.'app/system/include/public/ui/admin/paratype.php';
	}

	public function get_para($listid,$module,$class1,$class2,$class3){
		global $_M;
		$paralist = $this->get_para_list($module,$class1,$class2,$class3);
		$list = load::mod_class('parameter/parameter_database', 'new')->get_list($listid, $module);
		foreach($paralist as $val){
			$para = $list[$val['id']];
			if($val['type']==7){
				$para7 = explode(",",$para['info']) ;
				$list['info_'.$val['id'].'_1'] = $para7[0];
				$list['info_'.$val['id'].'_2'] = $para7[1];
				if($para7[2])$list['info_'.$val['id'].'_3'] = $para7[2];
			}
			$list['info_'.$val['id']] = $para['info'];
			if(!$para){
				load::mod_class('parameter/parameter_database', 'new')->insert_list($listid, $val['id'], '', '', $_M['lang'], $module);
			}
		}

		return $list;
	}

	public function get_para_list($module,$class1,$class2,$class3){
		global $_M;
		// if(!$this->paralist[$module][$this->lang]){
		// 	$this->paralist[$module][$this->lang] = cache::get("para/paralist_{$module}_{$this->lang}");
		// 	if(!$this->paralist[$module][$this->lang]){
		// 		$query = "SELECT * FROM {$_M['table']['parameter']} WHERE module='{$module}' and lang='{$_M['lang']}' order by no_order ASC, id ASC";
		// 		$result = DB::query($query);
		// 		while($list = DB::fetch_array($result)){
		// 			if($list['options']){
		// 				$lists = explode("$|$",$list['options']);
		// 				$list['list'] = $lists;
		// 			}
		// 			$this->paralist[$module][$this->lang][$list['id']] = $list;
		// 		}
		// 		cache::put("para/paralist_{$module}_{$this->lang}", $this->paralist[$module][$this->lang]);
		// 	}
		// }
		// $re = $this->paralist[$module][$this->lang];
		$re = load::mod_class('parameter/parameter_database', 'new')->get_parameter($module);
		$paralists = array();
		foreach($re as $val){
			$val['list'] = $val['para_list'];
			if($val['class1']){
				if($val['class1']==$class1){
					if($val['class2']==0&&$val['class3']==0)$paralists[] = $val;
					if($val['class2']&&$val['class2']==$class2&&$val['class3']==0)$paralists[] = $val;
					if($val['class3']&&$val['class3']==$class3)$paralists[] = $val;
				}
			}else{
				$paralists[] = $val;
			}
		}
		$re = $paralists;
		return $re;
	}

	//复制字段内容
	public function copy_list($module, $listid, $paraid, $tolistid, $toparaid, $tolang){
		$para_list = load::mod_class('parameter/parameter_list_database', 'new');
		$para_list->construct($module);
		$list = $para_list->select_by_listid_paraid($listid, $paraid);
		if($list['id']){
			$list['id'] = '';
			$list['listid'] = $tolistid;
			$list['paraid'] = $toparaid ? $toparaid : $list['paraid'];
			$list['lang'] = $tolang ? $tolang : $list['paraid'];
			return $para_list->insert($list);
		}
	}

	//复制字段
	public function copy_parameter($classnow, $toclass1, $toclass2, $toclass3, $tolang){
		$c = load::sys_class('label', 'new')->get('column')->get_column_id($classnow);
		$paras = load::mod_class('parameter/parameter_database', 'new')->get_list_by_class_no_next($classnow);
		foreach($paras as $key => $val) {
			$list = $val;
			$list['class1'] = $toclass1;
			$list['class2'] = $toclass2;
			$list['class3'] = $toclass3;
			$list['lang'] = $tolang;
			unset($list['id']);
			$pids[$val['id']] = load::mod_class('parameter/parameter_database', 'new')->insert($list);
		}
		return $pids;
	}

}

# This program is an open source system, commercial use, please consciously to purchase commercial license.
# Copyright (C) MetInfo Co., Ltd. (http://www.metinfo.cn). All rights reserved.
?>
