# py_voicetext

A python wrapper library for voicetext.

## Install SWIG
```sh
cd /tmp
wget http://prdownloads.sourceforge.net/swig/swig-3.0.12.tar.gz
tar zxvf swig-3.0.12.tar.gz
cd swig-3.0.12
./configure && make
make install
```

## Build & Install

### Step1: build from source
- make sure the configs for your own in Makefile.
```sh
./build.sh
```

### Step2: Run a Test
- please change license file path for your own PC.
```sh
make test
```

### Step3: Install packages
```sh
python setup.py install
```

## Usage
```python
import py_voicetext

# see library details
help(py_voicetext)

# get load code
infoval = py_voicetext.new_intp()
py_voicetext.VT_GetTTSInfo_JPN(py_voicetext.VT_LOAD_SUCCESS_CODE, None, infoval, 4)
print('infoval = ', py_voicetext.intp_value(infoval))

# get VT_MAX_CHANNEL
py_voicetext.VT_GetTTSInfo_JPN(py_voicetext.VT_MAX_CHANNEL, None, infoval, 4)
print('VT_MAX_CHANNEL = ', py_voicetext.intp_value(infoval))

# VT_SAMPLING_FREQUENCY
py_voicetext.VT_GetTTSInfo_JPN(py_voicetext.VT_SAMPLING_FREQUENCY, None, infoval, 4)
print('VT_SAMPLING_FREQUENCY = ', py_voicetext.intp_value(infoval))

# load tts
DB_PATH = '/usr/vt/hikari/D44'
LICENSE_FILE = '/usr/vt/verify/verification.txt'
py_voicetext.VT_LOADTTS_JPN(0, -1, DB_PATH, LICENSE_FILE)

# generate a sample TTS wav
ret_code = py_voicetext.VT_TextToFile_JPN(
    py_voicetext.VT_FILE_API_FMT_S16PCM_WAVE,
    "animal",
    "/tmp/1.wav",
    -1, -1, -1, -1, -1, -1, -1
)
if ret_code != py_voicetext.VT_FILE_API_SUCCESS:
    print('error')
    py_voicetext.VT_UNLOADTTS_JPN(-1)
    exit()

# shutdown tts
py_voicetext.VT_UNLOADTTS_JPN(-1)
```

## Known Issues:

- Now VT_GetTTSInfo_JPN( ... ) support `(int *)` only.


## Author
kilfu0701 (kilfu0701@gmail.com)

## License
MIT
