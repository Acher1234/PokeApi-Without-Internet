from ubuntu:20.04
COPY ./pokeapi ./pokeapi
ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt upgrade
RUN apt install -y gcc make python3 python3-pip curl nginx
WORKDIR /pokeapi
RUN alias python=python3
RUN make install
RUN python3 manage.py migrate --settings=config.local
RUN echo "from data.v2.build import build_all; build_all()" | python3 manage.py shell --settings=config.local
COPY ./nginx.conf /etc/nginx/nginx.conf
RUN /usr/sbin/nginx 
ENTRYPOINT ["python3", "manage.py", "runserver", "--settings=config.local"]


