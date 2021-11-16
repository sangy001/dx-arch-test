FROM python:latest

RUN apt-get update \
    && apt-get install -y sshpass \
    && apt-get install -y expect \
    && apt-get install -y vim

RUN pip3 install requests && pip3 install PyVmomi && pip3 install ansible
ADD hosts /etc/ansible/hosts
ADD ansible.cfg /etc/ansible/ansible.cfg

WORKDIR /root