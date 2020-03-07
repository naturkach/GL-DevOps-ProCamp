# GL-DevOps-ProCamp
task by GL DevOps ProCamp

Metrics collection script
use: Python3
     psutil lib


The script should accept a single parameter to specify which metrics set to print:

cpu - prints CPU metrics
mem - prints RAM metrics

CPU Metrics

$ ./metrics cpu


Sample output:
<pre>
system.cpu.idle 97.9
system.cpu.user 1.0
system.cpu.guest 0.0
system.cpu.iowait 0.0
system.cpu.stolen 0.0
system.cpu.system 1.0
</pre>


Memory Metrics

$ ./metrics mem


Sample output:

<pre>
virtual total 6235820032
virtual used 4509483008
virtual free 1018150912
virtual shared 193212416
swap total 2147479552
swap used 1740783616
swap free 406695936
</pre>

<hr>
<b>Docker</b>

*download Dockerfile 
 <pre>wget https://raw.githubusercontent.com/naturkach/GL-DevOps-ProCamp/master/Dockerfile</pre>

*and build container:
<pre>$ sudo docker build -t metricsapp .</pre>

*run container:
<pre>
sudo docker run metricsapp mem -rm
sudo docker run metricsapp cpu -rm
</pre>
