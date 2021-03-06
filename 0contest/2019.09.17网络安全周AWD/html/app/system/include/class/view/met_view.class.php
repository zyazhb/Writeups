<?php

load::sys_class('view/view_compile');
/**
 * 模板标签处理
 */
final class met_view
{

    /**
     * 模板变量
     *
     * @var array
     */
    public $vars = array();

    public $const = array();
    /**
     * 模版文件
     *
     * @var null
     */
    public $tplFile = null;
    /**
     * 编译文件
     *
     * @var null
     */
    public $compileFile = null;
    public $id;
    /**
     * 模板显示
     *
     * @param string $tplFile 模板文件
     * @param string $cachePath 缓存目录
     * @param int $cacheTime 缓存时间
     * @param string $contentType 文件类型
     * @param bool $show 是否显示
     *
     * @return bool|string
     */
    public function display(
        $tplFile = null, $cacheTime = -1, $cachePath = null,
        $contentType = "text/html", $show = true
    )
    {
        global $_M;


        //缓存文件名
        $cacheName = md5($_SERVER['REQUEST_URI']);

        //缓存时间
        $cacheTime = is_numeric($cacheTime)
            ? $cacheTime
            : -1;
        //缓存路径
        $cachePath = $cachePath ? $cachePath : TEMP_CACHE_PATH;

        //内容
        $content = null;


        if (!$content) {
            /**
             * 全局变量定义
             * 模板使用{$c.xx}方式调用
             */
            load::sys_class('view/ui_compile');
            $ui_compile = new ui_compile();

            $this->vars['g'] = $ui_compile->list_public_config();
            $this->vars['c'] = $ui_compile->replace_sys_config();
            $this->vars['url'] = $_M['url'];
            $templates = $ui_compile->list_templates_config();
            $this->vars['user'] = load::sys_class('user', 'new')->get_login_user_info();

            /**
             * 模板使用$lang.xxx调用模板标签配置
             */
            $this->vars['lang'] = $templates;
            $this->vars['word'] = $_M['word'];

            /**
             * 获得模板文件
             */
            $this->tplFile = $this->getTemplateFile($tplFile);

            if (!$this->tplFile) {
                return;
            }


            //编译文件
            $this->compileFile
                = $cachePath
                . '/_' . substr(md5($this->tplFile), 0, 8) . '.php';


            // 编译文件不存在或DEBUG时都会重新编译
            if ($this->compileInvalid($tplFile)) {

                //执行编译
                $this->compile();
            }

            //加载全局变量
            if (!empty($this->vars)) {
                extract($this->vars);
            }

            ob_start();
            include($this->compileFile);
            $content = ob_get_clean();

        }


        if ($show) {
            $charset = "UTF-8";
            if (!headers_sent()) {
                header("Content-type:" . $contentType . ';charset=' . $charset);
            }

            echo $content;die;
        } else {
            return $content;
        }
    }

    /**
     * 获得视图内容
     *
     * @param null $tplFile 模板文件
     * @param null $cacheTime 缓存时间
     * @param null $cachePath 缓存路径
     * @param string $contentType 文档类型
     *
     * @return bool|string
     */
    public function fetch(
        $tplFile = null, $cacheTime = null, $cachePath = null,
        $contentType = "text/html"
    )
    {

        return $this->display(
            $tplFile, $cacheTime, $cachePath, $contentType, false
        );
    }

    /**
     * 验证缓存是否过期
     *
     * @param string $cachePath 缓存目录
     *
     * @return bool
     */
    public function isCache($cachePath = null)
    {
        $cachePath = $cachePath ? $cachePath : TEMP_CACHE_PATH;
        $cacheName = md5($_SERVER['REQUEST_URI']);

        return true;
    }

    /**
     * 获得模版文件
     *
     * @param $file 模板文件
     *
     * @return bool|string
     */
    private function getTemplateFile($file)
    {
        global $_M;

        if (!is_file($file)) {
            if(strstr($file, 'ui_ajax/')){
                $file = PATH_WEB . 'public/ui/v2/module/ajax/' . str_replace('ui_ajax/', '', $file);
            }elseif(strstr($file, 'ui_v2')){
                $file = PATH_WEB . 'public/ui/v2/' . str_replace('ui_v2/', '', $file);
            }else{
                $file = PATH_TEM . $file;
            }

            /**
             * 添加后缀
             */
             if (!preg_match('/\.[a-z]+$/i', $file)) {
                $file .= '.php';
            }

        }
        /**
         * 模板文件检测
         */
        if (is_file($file)) {

            return $file;
        } else {
            return false;
        }
    }

    /**
     * 编译是否失效
     *
     * @return bool true 失效
     */
    private function compileInvalid()
    {
        $tplFile = $this->tplFile;
        $compileFile = $this->compileFile;
        return !file_exists($compileFile) || DEBUG
        || (filemtime($tplFile) > filemtime($compileFile));
    }

    /**
     * 编译模板
     */
    public function compile()
    {
        /**
         * 编译是否失效
         */

        if (!$this->compileInvalid()) {
            return;
        }
        $compileObj = new view_compile();
        $compileObj->id = $this->id;
        $compileObj->run($this);
    }

    /**
     * 向模板中传入变量
     *
     * @param string|array $var 变量名
     * @param mixed $value 变量值
     *
     * @return bool
     */
    public function assign($var, $value)
    {
        if (is_array($var)) {
            foreach ($var as $k => $v) {
                if (is_string($k)) {
                    $this->vars[$k] = $v;
                }
            }
        } else {
            $this->vars[$var] = $value;
        }
    }
}