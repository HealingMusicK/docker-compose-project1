# Docker-compose-study1
print "Hello World" by using nginx &amp; http server (golang) 
//
Docker-compose기법을 이용하여 nginx와 http server를 동시에 container로 구동
http와 nginx는 서로 linked되어 있고, nginx가 host와 80:80으로 포트포워딩 되어 있으므로,
최종적으로 http://localhost:80 을 통해 접근 가능.
