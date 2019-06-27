FROM jenkins/jenkins:lts
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
COPY ./jenkins /var/jenkins_home
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
USER root
RUN apt-get update && apt-get install
RUN apt-get install -y libopenmpi-dev openmpi-bin mpich git pkg-config gcc nano make autoconf
Run apt-get install -y libglib2.0 libglib2.0-dev libjansson4 libjansson-dev
USER jenkins
WORKDIR /var/jenkins_home
