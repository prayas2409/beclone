FROM lambci/lambda:build-python3.7

WORKDIR /online_assessment
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
