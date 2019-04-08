import py_voicetext

DB_PATH = '/usr/vt/hikari/D44'
LICENSE_FILE = '/usr/vt/verify/verification.txt'

def main():
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

    # init py_voicetext
    z = py_voicetext.VT_LOADTTS_JPN(0, -1, DB_PATH, LICENSE_FILE)

    # generate a sample TTS wav
    ret_code = py_voicetext.VT_TextToFile_JPN(py_voicetext.VT_FILE_API_FMT_S16PCM_WAVE , "animal", "/tmp/1.wav", -1, -1, -1, -1, -1, -1, -1);
    if ret_code != py_voicetext.VT_FILE_API_SUCCESS:
        print('error')
        py_voicetext.VT_UNLOADTTS_JPN(-1)
        exit()

    print('done')


if __name__ == '__main__':
    main()
