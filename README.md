# cybersecurity-projects

## Credit to https://www.youtube.com/watch?v=xuNuy8n8u-Y

- Dive into Network Traffic visualization using the Python programming language, Wireshark and Google Maps. This tutorial covers the implementation steps needed to take a file of network traffic and convert it into a visual presentation using Google Maps.

### Steps:

1. I added the libraries dpkt, pygeoip, and socket and the GeoLiteCity database
2. pulled the file from wireshark, by stopping the capture, selecting specified packets and saving in a pcap/tcpdump file format
3. Pull the pcap file into the project and read the file using the function main(). It is also responsible for the styling format when we pull up the map later
4. Looped over the captured packets and extracted the IPs from the pcap file using plotIP(pcap).
5. Then used the source and destination IP data to geo-locate it using the retKML().
6. I then ran the main() function and copied the printed information to the terminal. I took that information and pasted into a file and formatted it for XML.
7. (FYI)I attempted to convert that XML file to KML on the website mygeodata.cloud, however was unsuccessful and ended up using the XML data and format to plot the source/destination IP data to the map on the same website using their mapping utility.

### Summmary:

- I wanted to build a python project today and use some of the network analysis tools I've been using in my cybersecurity courses.
- This was an easy project to build outside of the KML file formatting. I ended up using
  mygeodata.cloud to input the XML file I created (output.xml) and got a similar representation of the packets captured in Wireshark

  ![Alt text](<Screen Shot 2023-08-07 at 4.29.14 PM.png>)

### What to work on afterwards:

- I would like to get better at parsing information out of one file format and writing it into another file
- I would also like to explore if Wireshark has this built in functionality with the help from external geo-location databases
