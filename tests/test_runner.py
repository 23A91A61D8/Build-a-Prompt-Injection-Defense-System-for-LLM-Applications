import os
from middleware.detector import ThreatDetector


detector = ThreatDetector()


def test_malicious_prompts():

    file_path = os.path.join("tests", "malicious_prompts.txt")

    with open(file_path, "r") as f:
        prompts = f.readlines()

    total = len(prompts)
    detected = 0

    for prompt in prompts:

        threat = detector.analyze(prompt.strip())

        if threat:
            detected += 1

    print("\nMalicious Prompt Test")
    print("----------------------")
    print("Total Attacks:", total)
    print("Detected Attacks:", detected)

    detection_rate = (detected / total) * 100
    print("Detection Rate: {:.2f}%".format(detection_rate))


def test_benign_prompts():

    file_path = os.path.join("tests", "benign_prompts.txt")

    with open(file_path, "r") as f:
        prompts = f.readlines()

    total = len(prompts)
    false_positives = 0

    for prompt in prompts:

        threat = detector.analyze(prompt.strip())

        if threat:
            false_positives += 1

    print("\nBenign Prompt Test")
    print("----------------------")
    print("Total Prompts:", total)
    print("False Positives:", false_positives)

    false_positive_rate = (false_positives / total) * 100
    print("False Positive Rate: {:.2f}%".format(false_positive_rate))


if __name__ == "__main__":

    test_malicious_prompts()
    test_benign_prompts()