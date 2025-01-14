FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app 

RUN apt-get update && apt-get install -y iputils-ping

RUN echo 'ctf_user:x:1000:1000:,,,:/home/ctf_user:/bin/bash\nctf_user2:x:1001:1001:flag={code_injection_vuln}:/home/ctf_user2:/bin/bash' >> /etc/passwd

EXPOSE 5000

CMD ["python3", "app.py"]