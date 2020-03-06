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

virtual total 16712351744

virtual used 9190146048

virtual free 1391624192

virtual shared 287655116

swap total 0

swap used 0


swap free 0
