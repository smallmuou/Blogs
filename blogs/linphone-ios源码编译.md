# Linphone-IOS源码编译
2014-11-20

## 下载源码包
<pre>git clone git://git.linphone.org/linphone-iphone.git --recursiv </pre>

## 安装依赖库
* Xcode - MacOSX系统自带
* coreutils - 是一个包含了多个类Unix所需的基本工具的软件包，如ls、mkdir、rm...
	<pre>
	sudo brew install coreutils </pre>
* autoconf,automake - Makefile自动生成工具
	<pre>
	sudo brew install automake </pre>
* libtool - 是一个通用库支持脚本，将使用动态库的复杂性隐藏在统一、可移植的接口中,包装了gcc或者其他的任何编译器，用户无需知道细节，只要告诉libtool说我需要要编译哪 些库即可,常见于autoconf/automake
	<pre>
	sudo brew install libtool </pre>
* intltool -  提取的各种源文件翻译(.xml.in, .glade, .desktop.in, .server.in, .oaf.in)的字符串
	<pre>
	sudo brew install intltool </pre>
* wget - 下载工具
* pkgconfig - 是一个提供从源代码中编译软件时查询已安装的库时使用的统一接口的计算机软件.输出已安装包的版本信息，链接器参数，编译器参数
	<pre>
	例子: gcc -o test test.c $(pkg-config --libs --cflags libpng) </pre>
* cmake - 自动构建工具类似于make
	<pre>
	sudo brew install cmake </pre>
* gmake - GNU Make，linux下的make
	<pre>
	http://mirror.bjtu.edu.cn/gnu/make/ 下载自己编译 </pre>
* yasm - 重写nasm
	<pre>
	sudo brew install yasm </pre>
* nasm - 80x86的汇编器
	<pre>
	sudo brew install nasm </pre>
* grep - 字符查找工具
* doxygen - 文档生成工具
	<pre>
	sudo brew install doxygen </pre>
* ImageMagick - 是一套功能强大、稳定而且开源的工具集和开发包，可以用来读、写和处理超过89种基本格式的图片文件，包括流行的TIFF、JPEG、GIF、 PNG、PDF以及PhotoCD等格式
	<pre>
	sudo brew install ImageMagick </pre>
* optipng - PNG 图像优化工具
	<pre>
	下载自己编译
	wget http://prdownloads.sourceforge.net/optipng/optipng-0.7.5.tar.gz?download </pre>
* antlr3 - 是一个语言识别工具，Another Tool forLanguage Recognition 的缩写
* gas-preprosessor.pl - ffmpeg编译需要
	<pre>
	wget --no-check-certificate https://raw.github.com/yuvi/gas-preprocessor/master/gas-preprocessor.pl
	sudo mv gas-preprocessor.pl /usr/local/bin/.
	sudo chmod +x /usr/local/bin/gas-preprocessor.pl </pre>
* link
	<pre>
	sudo ln -n /usr/local/bin/glibtoolize /usr/local/bin/libtoolize
	sudo ln -s  /usr/bin/strings /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/usr/bin/strings </pre>