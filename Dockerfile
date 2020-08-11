FROM python:3.7-alpine
ADD https://raw.githubusercontent.com/naturkach/GL-DevOps-ProCamp/master/metrics /usr/bin/metrics
RUN apk add --update gcc libc-dev fortify-headers linux-headers && rm -rf /var/cache/apk/*
RUN pip3 install psutil
RUN chmod +x /usr/bin/metrics
ENTRYPOINT ["python3", "/usr/bin/metrics"]
