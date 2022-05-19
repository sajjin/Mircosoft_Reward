FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install firefox
RUN apt-get -y install python3-pip
RUN apt-get -y install wget
RUN apt-get -y install curl
RUN pip3 install keyboard
RUN apt-get install -y kmod kbd
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt -y install ./google-chrome-stable_current_amd64.deb
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
RUN install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
RUN sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge-dev.list'
RUN rm microsoft.gpg
RUN apt update
RUN apt -y install microsoft-edge-stable

COPY main_docker.py ~/app/main.py
COPY dictionary.json ~/app/dictionary.json
COPY dictionary.txt ~/app/dictionary.txt
COPY counter_timer.txt ~/app/counter_timer.txt

CMD ["python3", "~/app/main.py"]