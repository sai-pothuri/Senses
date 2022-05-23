#!/bin/sh
# file_name = "sample-0.wav"
# FILE_NAME="sample-0.wav"
ID=$(curl -L -X POST https://asr.api.speechmatics.com/v2/jobs/ -H "Authorization: Bearer PTgWU9BUtvgVZGOn85GFwp0dJIc80HgP" -F data_file=@$FILE_NAME -F config='{"type": "transcription","transcription_config": { "operating_point":"enhanced", "language": "en" }}' | jq '.id' | tr -d '"')
sleep 30
TEXT=$(curl -L -X GET "https://asr.api.speechmatics.com/v2/jobs/$ID/transcript?format=txt" -H "Authorization: Bearer PTgWU9BUtvgVZGOn85GFwp0dJIc80HgP")
echo $TEXT