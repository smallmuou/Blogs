#Opensips部署
2014-11-14
## Install

* download source code from [here](http://www.opensips.org/Downloads/Downloads)
* make menuconfig（option -enable mysql）
* apt-get install libcurl-devel
* apt-get install mysql-devel

* make all
* make install

## Config

* config /usr/local/etc/opensips/opensipsctlrc
	* DBENGINE
	* DBHOST
	* DBNAME
	* DBRWUSER
	* DBRWPW
	* DBROOTUSER
	
* config /usr/local/etc/opensips/opensips.cfg
	* listen=udp:112.124.57.23:5060 (112.124.57.23为服务器ip)
* opensipsdbctl create
* opensipsctl add user password


## log
* 在opensips.cfg中将log_facility =LOG_LOCAL0 的注释去掉
* touch /var/log/opensips.log
* vim /etc/rsyslog.conf, 末尾添加
	local0.*              /var/log/opensips.log
* /etc/init.d/rsysklogd restart