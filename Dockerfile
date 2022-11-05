FROM continuumio/miniconda3:4.12.0

COPY environment-exact.txt .
RUN conda install --file environment-exact.txt

RUN useradd --create-home --shell /bin/bash panel-user
USER panel-user
WORKDIR /home/panel-user
