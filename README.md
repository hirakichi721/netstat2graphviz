# netstat2graphviz.py
  Drawing a graph according to the output of netstat.
  (*) netstat edited data are required.

# Input
  netstat edited data
  ```
    protocol,sourceip:sourceport,destip:destport
  ```
  InputSample
  ```
   tcp,10.0.0.1:514,10.0.0.2:10023
   tcp,0.0.0.0:514,*:*
   udp,10.0.0.1:10001,10.0.0.3:514
  ```

# Output
![outputSample](https://user-images.githubusercontent.com/9582252/120920419-a4dc7600-c6f9-11eb-81a4-6b8f3a938738.png)


# Pre-requirement
  1. pip install graphviz
  2. Install Graphviz for displaying.
     See here for more detailed.
     https://graphviz.org/download/

# Warning
  IP of * or 0.0.0.0(listed in exclideips)are ignored.
