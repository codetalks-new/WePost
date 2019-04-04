FROM redis:5-alpine
LABEL maintainer="codetalks@代码会说话"
WORKDIR /opt
ADD redis.master.conf redis.master.conf
ADD redis.replica.conf redis.replica.conf
ENTRYPOINT [ "redis-server" ]
