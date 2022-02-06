# Download Zabbix graph after test automatically

Retrieve graphs from Zabbix server (for older versions) after running an API load test with Gatling.

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt install python3
sudo apt install pip
sudo pip install webdriver-manager
sudo pip install selenium
unzip GetGraph.zip
sudo chmod 755 GetGraph/GetGraph.sh GetGraph/graphs.py
 ```

To configure a test, edit the Gatling command in GetGraph.sh for the relevant app or run your own performance tool instead of Gatling.

Script GetGraph.sh is executable with the parameters according to the app you want to test:

For app:
“WV” for Widevine.
“FP” for FairPlay.
“PR” for PlayReady.

Finally add the host which the app is running on as a parameter (Host ID on Zabbix server), Zabbix server username and password, Zabbix server URL.

Example:
```
cd GetGraph
./GetGraph.sh 'WV' 'winnie' 'username' 'password' 'http://ZabbixURL'
 ```
 
You can find the Zabbix performance graphs under Results folder with the end time and date of the relevant performance test.
