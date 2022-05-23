import os
# PTgWU9BUtvgVZGOn85GFwp0dJIc80HgP
def speech_api(file_name):
    cmd = "FILE_NAME=" + file_name + " bash speech_api.sh > blackhole.log"
    # print(cmd)
    os.system(cmd)
    with open("blackhole.log") as f:
        text=f.readline()
    # print(text)
    if text[0]=='{':
        return False
    return text
# speech_api("sample-0.mp3")

def htr_api(file_name):
    cmd = "FILE_NAME=" + file_name + " bash htr_api.sh > blackhole.log"
    os.system(cmd)
    with open("blackhole.log") as f:
        text=f.readline()
        # print(text)
    return text
