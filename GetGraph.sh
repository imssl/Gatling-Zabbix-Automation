#Widevine Tests
comment="https,176rps,3d,endurance";
if [ $1 == "WV" ]
then
        timedatectl set-timezone Europe/Tallinn;
        echo "PC date set to Tallinn, arrange according to your Zabbix server timezone";
        sleep 1;
        date1=$(date '+%Y-%m-%d %H:%M:%S');
        echo "Test started.";
        sleep 1;
        sudo JAVA_OPTS="-Drps=176 -Dduration=259200 -Dhost=https://10.0.6.96" /home/bigone/gatling_3.6.1/bin/gatling.sh -s drm.WV_open_model_dynamic -rd "$comment";
        sleep 60;
        date2=$(date '+%Y-%m-%d %H:%M:%S');
        echo "Test ended";
        sleep 1;
        echo "Retrieving performance graphs from Zabbix server";
        python3 graphs.py "$date1" "$date2" $2 $1 $3 $4 $5 "$comment";
fi

#FairPlay Tests
if [ $1 == "FP" ]
then
        timedatectl set-timezone Europe/Tallinn;
        echo "PC date set to Tallinn, arrange according to your Zabbix server timezone";
        sleep 1;
        date1=$(date '+%Y-%m-%d %H:%M:%S');
        echo "Test started.";
        sleep 1;
        sudo JAVA_OPTS="-Drps=180 -Dduration=3600 -Dhost=https://10.0.5.79" /home/bigone/gatling_3.6.1/bin/gatling.sh -s drm.FP_open_model_dynamic -rd "$comment";
        sleep 60;
        date2=$(date '+%Y-%m-%d %H:%M:%S');
        echo "Test ended";
        sleep 1;
        echo "Retrieving performance graphs from Zabbix server";
        python3 graphs.py "$date1" "$date2" $2 $1 $3 $4 $5 "$comment";
fi

#PlayReady Tests
if [ $1 == "PR" ]
then
        timedatectl set-timezone Europe/Tallinn;
        echo "PC date set to Tallinn, arrange according to your Zabbix server timezone";
        sleep 1;
        date1=$(date '+%Y-%m-%d %H:%M:%S');
        echo "Test started.";
        sleep 1;
        sudo JAVA_OPTS="-Drps=110 -Dduration=180 -Dhost=https://10.0.5.145" /home/bigone/gatling_3.6.1/bin/gatling.sh -s drm.PR_open_model_dynamic -rd "$comment";
        sleep 60;
        date2=$(date '+%Y-%m-%d %H:%M:%S');
        echo "Test ended";
        sleep 1;
        echo "Retrieving performance graphs from Zabbix server";
        python3 graphs.py "$date1" "$date2" $2 $1 $3 $4 $5 "$comment";
fi

