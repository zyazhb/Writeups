<?php
# MetInfo Enterprise Content Management System
# Copyright (C) MetInfo Co.,Ltd (http://www.metinfo.cn). All rights reserved.

defined('IN_MET') or exit('No permission');


/**
 * 系统标签类
 */
 class engine {
 	public function dodisplay($file,$mod = array())
    {
        global $_M;
        define("TEMP_CACHE_PATH" , PATH_WEB.'cache/templates');
        define("PATH_TEM" , PATH_WEB.'templates/'.$_M['config']['met_skin_user'].'/');
        define("DEBUG", TRUE);
        load::sys_class('view/met_view');
        $view = new met_view();
        $view->assign('data',$mod);
        $view->display($file);
        return  $view->compileFile;
    }
}

# This program is an open source system, commercial use, please consciously to purchase commercial license.
# Copyright (C) MetInfo Co., Ltd. (http://www.metinfo.cn). All rights reserved.
?>
