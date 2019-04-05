import py_voicetext

DB_PATH = '/usr/vt/hikari/D44'
LICENSE_FILE = '/usr/vt/verify/verification.txt'

def main():
    ## TODO: fix error bug
    #infoval = 0
    #py_voicetext.VT_GetTTSInfo_JPN(py_voicetext.VT_LOAD_SUCCESS_CODE, None, infoval, 4)

    # init py_voicetext
    z = py_voicetext.VT_LOADTTS_JPN(0, -1, DB_PATH, LICENSE_FILE)

    # generate a sample TTS wav
    ret_code = py_voicetext.VT_TextToFile_JPN(py_voicetext.VT_FILE_API_FMT_S16PCM_WAVE , "animal", "/tmp/1.wav", -1, -1, -1, -1, -1, -1, -1)
    if ret_code != py_voicetext.VT_FILE_API_SUCCESS:
        print('error')
        py_voicetext.VT_UNLOADTTS_JPN(-1)
        exit()

    print('done')


if __name__ == '__main__':
    main()
