import subprocess
import time

from selenium import webdriver

usrname = ""
psword = ""
# 记录程序运行时间
start_time = time.time()
f0 = open('./ctn.log', 'a')
print(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(start_time)), file=f0, flush=True)
print("程序开始运行", file=f0, flush=True)
f0.close()

url4 = "http://1.2.3.4/"
url5 = "http://detectportal.firefox.com/"
url = "https://portalnew3.dhu.edu.cn/portalcloud/page/2/PC/chn/Login.html"  # 东华大学认证界面
url2 = "https://portalnew2.dhu.edu.cn/portalcloud/page/2/PC/chn/Login.html?switchip=10.10.90.2&ip=10.199.218.56&url=http://nmcheck.gnome.org/&wlanacname=Bras_M6K_DH"
url3 = "https://portalnew2.dhu.edu.cn/portalcloud/page/2/PC/chn/Login.html"
test_url = "202.108.22.5"  # 百度ip地址，用于检测是否能连到外网
net_gate = "10.199.160.1"
# url1 = "https://portalnew3.dhu.edu.cn/portalcloud/page/2/PC/chn/Login.html?switchip=10.10.90.2&ip=10.199.218.56
# &url=http://detectportal.firefox.com/success.txt&wlanacname=Bras_M6K_DH"
while True:
    # 每12个小时记录一次网络状态
    end_time = time.time()
    temp = end_time - start_time
    if temp > 43200:
        f1 = open('./ctn.log', 'a')
        print(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(end_time)), file=f1, flush=True)
        print("网络正常", file=f1, flush=True)
        f1.close()
        start_time = end_time

    p = subprocess.Popen([r'./ping.sh', test_url], close_fds=True, stdout=subprocess.PIPE)
    result = p.stdout.read()

    if result == b'1\n':
        p2 = subprocess.Popen([r'./pinggate.sh', net_gate], close_fds=True, stdout=subprocess.PIPE)
        result2 = p2.stdout.read()
        if result2 == b'0\n':  # ping net gate fail, not 3 packets receive
            f2 = open('./ctn.log', 'a')
            print(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())), file=f2, flush=True)
            print('failed to ping network gate', file=f2, flush=True)  # failed to ping network gate
            os.system('echo %s | sudo -S %s' % ('622', 'sudo service network-manager restart'))  # restart network
            time.sleep(10)
            p3 = subprocess.Popen([r'./pinggate.sh', net_gate], close_fds=True, stdout=subprocess.PIPE)
            result3 = p3.stdout.read()
            if result3 == b'0\n':  # ping net gate fail, not 3 packets receive
                f3 = open('./ctn.log', 'a')
                print(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())), file=f3, flush=True)
                print('restart did not work', file=f3, flush=True)
            else:
                f4 = open('./ctn.log', 'a')
                print(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())), file=f4, flush=True)
                print('restart did work', file=f4, flush=True)
        else:
            # print('无法ping通')
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            driver = webdriver.Firefox(firefox_options=options)
            # driver = webdriver.Firefox()
            driver.get(url4)
            driver.maximize_window()
            driver.find_element_by_name("username").clear()
            driver.find_element_by_name("username").send_keys(usrname)
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys(psword)
            driver.find_element_by_id("mobilelogin_submit").click()

            # 测试外网是否连接成功
            p1 = subprocess.Popen([r'./ping.sh', test_url], close_fds=True, stdout=subprocess.PIPE)
            result1 = p1.stdout.read()
            if result1 == b'1\n':
                status = "认证失败"
            else:
                status = "认证成功"
            f = open('./ctn.log', 'a')
            print(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())), file=f, flush=True)
            print(status, file=f, flush=True)  # 记录某个时间点连接失败，差不多是断网并且认证失败的时间点
            f.close()
            driver.quit()
