# CTN-SiHE
a set of scripts for automatic authentication to DHU internet. Ubuntu/selenium/firefox

针对东华大学有线校园网下Ubuntu+火狐浏览器开发（无线网还没测试过），脚本能够在检测到无法连接到外网的时候自动打开浏览器进行认证。

使用说明：
环境部署：
1.把geckodriver这个驱动放到/usr/local/bin/目录下。
2.安装selenium包到稍后要运行脚本的python里。比如你要用ubuntu自带的python3来运行，假设环境变量是python3，那就用对应的pip3 install selenium。

操作步骤：
1.在ctn.py里先把usrname和psword填上自己的用户名和密码，保存。
2.在当前目录打开终端，输入nohup python3 ctn.py &，脚本就会在后台运行了。如果要关闭，杀死该进程即可：kill -9 pid。pid是该进程的id，如果忘记了，输入ps aux | grep ctn.py，可以查看。

ctn.log文件保存的是脚本运行记录，可以看到某个时间认证失败或者成功。
ping.sh文件是ctn.py要调用的脚本。

以下是设置开机自启的部署方法：
由于python程序里调用了selenium包，运行第三方库需要环境变量都已设置好，所以开机自启的时间点不能超前于环境变量的设置。所以得把运行脚本的命令设置在~/.profile文件里的最后。（参考https://blog.csdn.net/abc_12366/article/details/87552848）
在最后添加：
cd /home/usrname/Documents/CTN-SiHE/
sh ctn.sh
cd的路径是程序文件夹存放的目录，建议放在Documents下。usrname是用户名，记得改。

改完重启即可。注意权限。

2021/1/16更新：
最近服务器搬迁，遇到Firefox无法跳转到认证界面的情况，把URL更改为 http://1.2.3.4/ 即可。

2021/6.7更新：
似乎是因为Firefox自身的问题，退出浏览器以后后台进程依旧保留。这导致脚本每天晚上登录校园网打开的浏览器并没有真正地被关闭，长期以往积累的后台进程越来越多，占用大量的内存，影响服务器日常使用。下面这条命令是用来杀死当前后台进程中所有的名字带有firefox的进程，望妥善使用。为避免误伤，没有写进自动脚本。
ps -ef | grep firefox | grep -v grep | awk '{print $2}' | xargs kill -9

2021/7.23更新：
由于近期校园网频繁发生断开内网的情况，脚本更新了内网断开时自动重启网络的命令。
请在开头输入sudo的密码。
