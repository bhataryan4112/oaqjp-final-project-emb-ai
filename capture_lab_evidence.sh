#!/usr/bin/env bash
# Run in the Skills Network lab; every transcript contains actual command output.
set -euo pipefail
cd /home/project/final_project
mkdir -p evidence
capture() {
    local name="$1"
    local command="$2"
    {
        printf '%s $ %s\n' "$PWD" "$command"
        bash -o pipefail -c "$command"
    } 2>&1 | tee "evidence/$name"
}

# script preserves the actual interactive Python shell prompts and commands.
capture 2b_application_creation "printf '%s\n' 'from emotion_detection import emotion_detector' \"print(emotion_detector('I am really mad about this'))\" 'exit()' | script -q -e -c python3 /dev/null && python3 test_emotion_detection.py"
capture 3b_formatted_output_test "python3 -c \"from emotion_detection import emotion_detector; print(emotion_detector('I am really mad about this'))\""
capture 4b_packaging_test "python3 -c \"from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))\""
capture 5b_unit_testing_result 'python3 test_emotion_detection.py'
capture 8b_static_code_analysis 'python3 -m pylint --persistent=n server.py'
