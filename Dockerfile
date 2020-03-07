FROM python:3
ADD https://raw.githubusercontent.com/naturkach/GL-DevOps-ProCamp/master/metrics /usr/bin/metrics
RUN pip3 install psutil
RUN chmod +x /usr/bin/metrics
ENTRYPOINT ["python3", "/usr/bin/metrics"]  
