FROM czentye/matplotlib-minimal:3.1.2

RUN pip3 install -v --no-cache-dir Flask
CMD /usr/local/bin/python server.py
