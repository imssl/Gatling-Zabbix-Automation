from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import sys, time, os

os.mkdir("Results/"+sys.argv[8])
folder="Results/"+sys.argv[8]
serverurl=sys.argv[7]

#set chromedriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
driver.set_window_size(1920, 1080, driver.window_handles[0])
driver.implicitly_wait(1)

#maximize browser
driver.maximize_window()

driver.get(serverurl+"/zabbix");

sername = driver.find_element_by_id("name")
password = driver.find_element_by_id("password")

username.send_keys(sys.argv[5])
password.send_keys(sys.argv[6])

driver.find_element_by_name("enter").click()

#launch URL
driver.get(serverurl+"/zabbix/zabbix.php?name=&ip=&dns=&port=&status=-1&evaltype=0&tags%5B0%5D%5Btag%5D=&tags%5B0%5D%5Boperator%5D=0&tags%5B0%5D%5Bvalue%5D=&maintenance_status=1&filter_name=&filter_show_counter=0&filter_custom_time=0&sort=name&sortorder=ASC&show_suppressed=0&action=host.view");
driver.implicitly_wait(10)
time.sleep(3)

if sys.argv[4] == "PR":

   #Select Host
   select = Select(driver.find_element_by_name('hostid'))
   select.select_by_visible_text(sys.argv[3]);

   ###################################################################################################
   #Select Graph
   select = Select(driver.find_element_by_name('graphid'))
   select.select_by_visible_text("cpu %");

   #Select Time Period
   begin = driver.find_element_by_id("from")
   end = driver.find_element_by_id("to")

   begin.clear();
   end.clear();

   begin.send_keys(sys.argv[1])
   end.send_keys(sys.argv[2])

   driver.implicitly_wait(10)
   driver.find_element_by_name("apply").click()
   driver.implicitly_wait(100)
   time.sleep(2)

   path=folder+'/Cpu utilization.png'

   #open file in write and binary mode
   with open(path, 'wb') as file:

   #identify image to be captured
      l = driver.find_element_by_xpath('//*[@id="graph_full"]')

   #write file
      file.write(l.screenshot_as_png)
   driver.implicitly_wait(10)

   ###################################################################################################
   #Select Graph
   select = Select(driver.find_element_by_name('graphid'))
   select.select_by_visible_text("CPU processes");

   #Select Time Period
   begin = driver.find_element_by_id("from")
   end = driver.find_element_by_id("to")

   begin.clear();
   end.clear();

   begin.send_keys(sys.argv[1])
   end.send_keys(sys.argv[2])

   driver.implicitly_wait(10)
   driver.find_element_by_name("apply").click()
   driver.implicitly_wait(100)
   time.sleep(2)

   path=folder+'/Cpu processes.png'

   #open file in write and binary mode
   with open(path, 'wb') as file:

   #identify image to be captured
      l = driver.find_element_by_xpath('//*[@id="graph_full"]')

   #write file
      file.write(l.screenshot_as_png)
   driver.implicitly_wait(10)

   ###################################################################################################
   #Select Graph
   select = Select(driver.find_element_by_name('graphid'))
   select.select_by_visible_text("process memory usage (w3wp, lsass)");

   #Select Time Period
   begin = driver.find_element_by_id("from")
   end = driver.find_element_by_id("to")

   begin.clear();
   end.clear();

   begin.send_keys(sys.argv[1])
   end.send_keys(sys.argv[2])

   driver.implicitly_wait(10)
   driver.find_element_by_name("apply").click()
   driver.implicitly_wait(100)
   time.sleep(2)

   path=folder+'/process memory usage.png'

   #open file in write and binary mode
   with open(path, 'wb') as file:

   #identify image to be captured
      l = driver.find_element_by_xpath('//*[@id="graph_full"]')

   #write file
      file.write(l.screenshot_as_png)
   driver.implicitly_wait(10)

   ###################################################################################################
   #Select Graph
   select = Select(driver.find_element_by_name('graphid'))
   select.select_by_visible_text("Memory usage");

   #Select Time Period
   begin = driver.find_element_by_id("from")
   end = driver.find_element_by_id("to")

   begin.clear();
   end.clear();

   begin.send_keys(sys.argv[1])
   end.send_keys(sys.argv[2])

   driver.implicitly_wait(10)
   driver.find_element_by_name("apply").click()
   driver.implicitly_wait(100)
   time.sleep(2)

   path=folder+'/memory usage.png'

   #open file in write and binary mode
   with open(path, 'wb') as file:

   #identify image to be captured
      l = driver.find_element_by_xpath('//*[@id="graph_full"]')

   #write file
      file.write(l.screenshot_as_png)
   driver.implicitly_wait(10)


   #close browser
   driver.quit()

elif sys.argv[4] == "FP" or "WV":

   #Select Host
   select.select_by_visible_text(sys.argv[3]);
   select.select_by_visible_text('Graphs');

   ###################################################################################################
   #Select Graph
   select = Select(driver.find_element_by_name('graphid'))
   select.select_by_visible_text("Available memory");

   #Select Time Period
   begin = driver.find_element_by_id("from")
   end = driver.find_element_by_id("to")

   begin.clear();
   end.clear();

   begin.send_keys(sys.argv[1])
   end.send_keys(sys.argv[2])

   driver.implicitly_wait(10)
   driver.find_element_by_name("apply").click()
   driver.implicitly_wait(100)
   time.sleep(2)

   path=folder+'/Available memory.png'

   #open file in write and binary mode
   with open(path, 'wb') as file:

   #identify image to be captured
      l = driver.find_element_by_xpath('//*[@id="graph_full"]')

   #write file
      file.write(l.screenshot_as_png)
   driver.implicitly_wait(10)


   ###################################################################################################
   #Select Graph
   select = Select(driver.find_element_by_name('graphid'))
   select.select_by_visible_text("CPU utilization");

   #Select Time Period
   begin = driver.find_element_by_id("from")
   end = driver.find_element_by_id("to")

   begin.clear();
   end.clear();

   begin.send_keys(sys.argv[1])
   end.send_keys(sys.argv[2])

   driver.implicitly_wait(10)
   driver.find_element_by_name("apply").click()
   driver.implicitly_wait(100)
   time.sleep(2)

   path=folder+'/CPU utilization.png'

   #open file in write and binary mode
   with open(path, 'wb') as file:

   #identify image to be captured
      l = driver.find_element_by_xpath('//*[@id="graph_full"]')

   #write file
      file.write(l.screenshot_as_png)
   driver.implicitly_wait(10)

   ###################################################################################################
   #Select Graph
   select = Select(driver.find_element_by_name('graphid'))
   select.select_by_visible_text("memory process rss [mono] normal (Taavi)");

   #Select Time Period
   begin = driver.find_element_by_id("from")
   end = driver.find_element_by_id("to")

   begin.clear();
   end.clear();

   begin.send_keys(sys.argv[1])
   end.send_keys(sys.argv[2])

   driver.implicitly_wait(10)
   driver.find_element_by_name("apply").click()
   driver.implicitly_wait(100)
   time.sleep(2)

   path=folder+'/memory real.png'

   #open file in write and binary mode
   with open(path, 'wb') as file:

   #identify image to be captured
      l = driver.find_element_by_xpath('//*[@id="graph_full"]')

   #write file
      file.write(l.screenshot_as_png)
   driver.implicitly_wait(10)

   ###################################################################################################
   #Select Graph
   select = Select(driver.find_element_by_name('graphid'))
   select.select_by_visible_text("memory process [mono, nginx] normal");

   #Select Time Period
   begin = driver.find_element_by_id("from")
   end = driver.find_element_by_id("to")

   begin.clear();
   end.clear();

   begin.send_keys(sys.argv[1])
   end.send_keys(sys.argv[2])

   driver.implicitly_wait(10)
   driver.find_element_by_name("apply").click()
   driver.implicitly_wait(100)
   time.sleep(2)

   path=folder+'/memory virtual mono nginx.png'

   #open file in write and binary mode
   with open(path, 'wb') as file:

   #identify image to be captured
      l = driver.find_element_by_xpath('//*[@id="graph_full"]')

   #write file
      file.write(l.screenshot_as_png)
   driver.implicitly_wait(10)

   ###################################################################################################
   #Select Graph
   select = Select(driver.find_element_by_name('graphid'))
   select.select_by_visible_text("memory process [mono] normal (Taavi)");

   #Select Time Period
   begin = driver.find_element_by_id("from")
   end = driver.find_element_by_id("to")

   begin.clear();
   end.clear();

   begin.send_keys(sys.argv[1])
   end.send_keys(sys.argv[2])

   driver.implicitly_wait(10)
   driver.find_element_by_name("apply").click()
   driver.implicitly_wait(100)
   time.sleep(2)

   path=folder+'/memory virtual mono.png'

   #open file in write and binary mode
   with open(path, 'wb') as file:

   #identify image to be captured
      l = driver.find_element_by_xpath('//*[@id="graph_full"]')

   #write file
      file.write(l.screenshot_as_png)
   driver.implicitly_wait(10)


   #close browser
   driver.quit()

else:
   print("Please enter correct app version: WW, FP, PR")
