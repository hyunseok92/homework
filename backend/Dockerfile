# backend/Dockerfile

# 기본 이미지 설정
FROM continuumio/miniconda3:latest

# 환경 변수 설정
ENV PATH /opt/conda/bin:$PATH

# 필요한 패키지 설치
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev && \
    apt-get clean

# Python 환경 설정 및 패키지 설치
RUN conda install -y python=3.8 && \
    conda clean -ya

# MySQL client 라이브러리 설치
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# FastAPI 애플리케이션을 위한 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt /app/

RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# 나머지 애플리케이션 파일 복사
COPY . /app

# 포트 노출
EXPOSE 8000

# 컨테이너 시작 시 실행할 명령
CMD ["/opt/venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]