FROM nvidia/cuda:12.1.0-base-ubuntu20.04
RUN apt update
RUN apt install -y git python3 python3-pip wget
WORKDIR /transcribe
COPY transcribe.py /transcribe/
RUN pip install git+https://github.com/openai/whisper.git
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y ffmpeg
# RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends ffmpeg
RUN pip install git+https://github.com/pytube/pytube.git
RUN pip install googletrans==4.0.0-rc1
CMD ["python","transcribe.py"]
