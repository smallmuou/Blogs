# SIP协议分析
2014-11-14

### [简介](http://www.ietf.org/rfc/rfc3261.txt)
* SIP(Session Initiation Protocol)是类似于HTTP的基于文本的协议

### 协议栈
* PJSIP
* ReSIProcate - 较稳定
* belle-sip（Linphone）
* SipDroid
* OPAL - 发展潜力
* VOCAL - 比较完善
* sipX - 兼容性好
* oSIP - 小巧而快速

### 抓包分析
###### Listen过程
* 呼叫方
![image](http://127.0.0.1/markdown/Listen A Shark.png)
* 被呼叫方
![image](http://127.0.0.1/markdown/Listen B Shark.png)
* 流程

![image](http://127.0.0.1/markdown/Listen.png)

###### Hangup过程
* 主动挂断方
![image](http://127.0.0.1/markdown/Hangup A Shark.png)
* 被挂掉方
![image](http://127.0.0.1/markdown/Hangup B Shark.png)
* 流程

![image](http://127.0.0.1/markdown/Hangup.png)

###### Not Register状态
* 呼叫方
![image](http://127.0.0.1/markdown/Not Register Shark.png)
* 流程

![image](http://127.0.0.1/markdown/Not Register.png)

###### Offline状态
* 呼叫方
![image](http://127.0.0.1/markdown/Offline Shark.png)
* 流程

![image](http://127.0.0.1/markdown/Offline.png)

###### Busy状态
* 呼叫方
![image](http://127.0.0.1/markdown/Busy A  Shark.png)
* 被呼叫方
![image](http://127.0.0.1/markdown/Busy B  Shark.png)
* 流程

![image](http://127.0.0.1/markdown/Busy.png)


