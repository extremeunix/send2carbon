send2carbon
===========

A script to send metrics to carbon


# Usage
* -H \<carbon server hostname\>
* -p \<carbon server port\>
* -m \<your.metric.name\>
* -v \<metric value\>
* -t \<metric time\> Unix Timestamp [default: UTC now] 

# Example
./send2carbon.py -H 10.1.1.1 -p 2003 -m 'server1.apache.4xx' -v '200'

./send2carbon.py -H 10.1.1.1 -p 2003 -m 'server1.apache.4xx' -v '200' -t 1382582174
