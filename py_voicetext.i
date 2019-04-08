%module py_voicetext

// Make mylib_wrap.cxx include this header:
%{
#include "/usr/vt/hikari/D44/inc/vt_jpn.h"
%}

%include "cpointer.i"

%pointer_functions(int, intp);

//%typemap(in) (void *value) {
//        $1 = (void *) $input;
//};

%typemap(in) int {
        $1 = PyInt_AsLong($input);
}

%typemap(in) HWND {
        $1 = PyLong_AsLong($input);
}

// Make SWIG look into this header:
%include "/usr/vt/hikari/D44/inc/vt_jpn.h"
