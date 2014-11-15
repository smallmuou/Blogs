# Asterisk 技术点
2014-11-07

* brew install apple-gcc-4.2
* ./configure CC=gcc-4.2
* define RONLY 0x1


Q:process_sdp: ignoring 'video' media offer because port number is zero

A:说明视频编码不支持，core show codecs video查看支持的视频编码（linphone默认只支持vp8）


# SIP.conf
* autocreatepeer=yes 允许自动创建节点
* context=xx，指定拨号规则（定义在extension.conf中）
* directmedia
* directrtpsetup
* canreinvite 重定向媒体流，在1.6.2后改为directmedia
	* yes - allow RTP media direct 
	* no - deny re-invites
	* nonat - allow reinvite when local, deny reinvite when NAT
	* update - use UPDATE instead of INVITE
	
* allow 允许编解码器
* allowguest 允许来电
* media_address 设定媒体流地址
* externip - 外网IP，与localnet配合用，当呼入的ip与localnet不在同一个网段，则用externip替换sdp中的ip
* localnet=192.168.2.0/255.255.255.0。。。可以有多个localnet（多网卡情况）
* nat
	* yes - asterisk 将忽视sdp中的ip和port，并单独回复给sender另外的ip和地址