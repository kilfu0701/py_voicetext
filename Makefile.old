build:
	swig -Wall -c++ -python py_voicetext.i
	g++ -fPIC -Wall -Wextra -shared py_voicetext_wrap.cxx -o _py_voicetext.so -L. /usr/vt/hikari/D44/bin/libvt_jpn.so -I/usr/include/python2.7/ -lpython2.7 -lm -lpthread -D_REENTRANT -O2

run:
	LD_LIBRARY_PATH=. python test.py

clean:
	rm -f py_voicetext.pyc py_voicetext.py py_voicetext_wrap.cxx
