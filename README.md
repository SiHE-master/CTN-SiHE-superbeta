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
