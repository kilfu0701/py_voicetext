OSNAME:=$(shell uname -s | sed 's/_.*//')

COMPILER =
# to get a list of available compilers run
# python swig-python-setup.py build_ext --help-compiler
# no changes necessary on Linux and MacOS
# change compiler to mingw32 on MinGW
ifeq ($(OSNAME),MINGW32)
	COMPILER = --compiler=mingw32
endif

all: py_voicetext

py_voicetext_wrap.cxx: clean py_voicetext.i
	swig -DNDEBUG -c++ -python py_voicetext.i

py_voicetext: py_voicetext_wrap.cxx
	python setup.py build_ext --inplace $(COMPILER)

realclean: clean

clean: mostlyclean
	rm -f _py_voicetext.so _py_voicetext.dylib _py_voicetext.dll
	rm -f py_voicetext.py py_voicetext.pyc

mostlyclean:
	rm -f swig-worked
	rm -f py_voicetext_wrap.cxx py_voicetext_wrap.c
	rm -rf build/

test:
	LD_LIBRARY_PATH=. python test.py

.PHONY: all clean mostlyclean realclean test
