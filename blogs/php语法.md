# PHP语法
2014-5-1

* PHP 脚本以 <?php 开头，以 ?> 结尾
* PHP 文件的默认文件扩展名是 ".php"

### 变量
* 变量以 $ 符号开头，其后是变量的名称
* 变量名称必须以字母或下划线开头
* 变量名称不能以数字开头
* 变量名称只能包含字母数字字符和下划线（A-z、0-9 以及 _）
* 变量名称对大小写敏感（$y 与 $Y 是两个不同的变量）
* 变量作用域：local、global、static

### 函数 & 类型
* echo & print
	* echo - 能够输出一个以上的字符串
	* print - 只能输出一个字符串，并始终返回 1
	* echo 比 print 稍快，因为它不返回任何值。
* 逻辑 true & false
* 数组 array
* 对象 class
* define() 宏定义
* foreach ($array as $value)
* 关联数组 $age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");$age['Peter']="35";
* 全局变量
	* $GLOBALS — 引用全局作用域中可用的全部变量， $GLOBALS[index] 的数组中存储了所有全局变量。变量的名字就是数组的键， 利用到关联数组
	* $_SERVER 这种超全局变量保存关于报头、路径和脚本位置的信息。
	* $_REQUEST 用于收集 HTML 表单提交的数据。
	* $_POST 广泛用于收集提交 method="post" 的 HTML 表单后的表单数据。$_POST 也常用于传递变量。
	* $_GET 也可用于收集提交 HTML 表单 (method="get") 之后的表单数据。

# Apache支持PHP
* vi /etc/apache2/httpd.conf，打开#loadmodule php5_module        libexec/apache2/libphp5.so
* cp /etc/php.ini.default /etc/php.ini
* apachectl restart

# [MACOSX 安装PHP扩展](http://xenojoshua.com/2012/01/mac-php-work-env/)

### memcache
* http://pecl.php.net/package/memcache
	* phpize
	* ./configure
	* make
	* make install
	
	