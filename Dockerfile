FROM python:3
ADD https://raw.githubusercontent.com/naturkach/GL-DevOps-ProCamp/master/metrics.py /usr/bin/metrics.py
RUN pip3 install psutil
RUN chmod +x /usr/bin/metrics.py
CMD python3 /usr/bin/metrics.py
