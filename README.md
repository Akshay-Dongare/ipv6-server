# ipv6-server
Self Host your website using HTML and ipv6. Use your laptop as host to display your HTML website to the internet using IPV6 protocol. Each device has a unique IPV6 address (correlated to device's MAC address) which makes it possible to host and share websites over the internet without the need of port forwarding like in ipv4!

## Steps

1. Run the following command to start the IPv6 server on your machine:

```shell
python ./ipv6server.py
```
to start the ipv6 server on your machine. You will now be able to access your website from the internet until your laptop/host is hosting the website using ipv6 serrver.
   
2. To test the server and website, from another device on another network, try to access the website you hosted using the ipv6 address (since we have not registered a Domain Name on any Domain Name Server (DNS), we won't be able to access our website with a name.
3. To find the address of your website run
```shell
ipconfig
```
on `Windows` and
```shell
ifconfig
```
on `Linux` and `Mac`.
4. Enter the address in browser using this format 
```
http://[YOUR_IPV6_ADDRESS]/
```

###  Example: 
```
http://[2405:201:1012:1c24:f521:9ce6:d8aa:b10c]/
```
