import os
# PTgWU9BUtvgVZGOn85GFwp0dJIc80HgP
def speech_api(file_name):
    cmd = "FILE_NAME=" + file_name + " bash speech_api.sh > blackhole.log"
    # print(cmd)
    os.system(cmd)
    with open("blackhole.log") as f:
        text=f.readline()
    # print(text)
    return text
# speech_api("sample-0.wav")