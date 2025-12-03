FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

# install deps
RUN apt-get update -y && apt-get install -y git-core python3-pip libmagickwand-dev libraqm-dev

COPY . /root/waifu2x

WORKDIR /root/waifu2x

# install
RUN pip3 install -r requirements-torch.txt && \
    pip3 install -r requirements.txt


CMD ["python3", "-u", "rp_handler.py"]

