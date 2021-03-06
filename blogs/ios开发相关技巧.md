# iOS开发相关技巧
2013-10-1

#### 工程目录结构

* AppDelegate
	* AppDelegate.h
	* AppDelegate.m
	* main.m
* Foundation
* Vendors
* Controllers
* Models
* Views
* Resources

#### 第三方库

|| *Year* || *Temperature (low)* || *Temperature (high)* ||
|| 1900 || -10 || 25 ||
|| 1910 || -15 || 30 ||
|| 1920 || -10 || 32 ||


||名称||用途||地址
||
CocoaLumberjack|日志打印|https://github.com/CocoaLumberjack/CocoaLumberjack
CocoaHTTPServer|HTTP服务器|https://github.com/robbiehanson/CocoaHTTPServer
TMCache|Disk&Memory Cache管理|https://github.com/tumblr/TMCache
StreamKit|音频流播放|https://github.com/tumtumtum/StreamingKit
CocoaAsyncSocket|Socket封装|https://github.com/robbiehanson/CocoaAsyncSocket
SVProgressHUD|提示HUD|https://github.com/TransitApp/SVProgressHUD
JSONKit|JSON解析库|https://github.com/johnezang/JSONKit
KxMenu|下拉菜单|https://github.com/kolyvan/kxmenu
EGORefreshTableHeaderView|下拉刷新
MWPhotoBrowser|图片浏览器|https://github.com/mwaterfall/MWPhotoBrowser
AFNetworking|HTTP封装|https://github.com/AFNetworking/AFNetworking
GPUImage|图像处理|https://github.com/BradLarson/GPUImage
fmdb|sqlite封装|https://github.com/ccgus/fmdb
ASIHTTPRequest|HTTP封装|https://github.com/pokeb/asi-http-request
SDWebImage|支持web image的显示及cache|https://github.com/rs/SDWebImage
SVPullToRefresh|下拉刷新|https://github.com/samvermette/SVPullToRefresh
cocos2d|游戏引擎|https://github.com/cocos2d/cocos2d-iphone
OpenUDID|UDID|https://github.com/ylechelle/OpenUDID
InAppSettingsKit|设置|https://github.com/futuretap/InAppSettingsKit


#### 代码片段


* 获取系统可用内存
<pre><code>
- (natural_t)getFreeMemory {
    mach_port_t host_port;
    mach_msg_type_number_t host_size;
    vm_size_t pagesize;
    host_port = mach_host_self();
    host_size = sizeof(vm_statistics_data_t) / sizeof(integer_t);
    host_page_size(host_port, &pagesize);
    vm_statistics_data_t vm_stat;
    if (host_statistics(host_port, HOST_VM_INFO, (host_info_t)&vm_stat, &host_size) != KERN_SUCCESS) {
        return 0;
    }
    
    /* Stats in bytes */
    natural_t mem_free = vm_stat.free_count * pagesize;
    return mem_free;
}
</code></pre>