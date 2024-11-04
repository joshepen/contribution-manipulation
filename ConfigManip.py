import os
import subprocess
import datetime
import itertools
import time

START_TIMESTAMP = 1293991200
INPUT_FILENAME = "input.txt"
DUMMY_FILENAME = "dummy.txt"
SECONDS_IN_DAY = 60 * 60 * 24


def main():
    open(DUMMY_FILENAME, "w").close()

    data = processInputData(INPUT_FILENAME)
    commitAll(data)


def processInputData(filename):
    with open(filename, "r") as file:
        rawData = file.readlines()
        # Transpose data for easier processing
        rawData = [list(i) for i in zip(*rawData)]
        rawData = list(itertools.chain.from_iterable(rawData))

        # I don't do any error handling for this next line because
        # the code isn't gonna work if this fails.
        rawData = [int(num) for num in rawData]
        return rawData


def gitCommit(unixTimestamp: int):
    with open(DUMMY_FILENAME, "a") as file:
        file.write("a")
    dateStr = datetime.datetime.fromtimestamp(unixTimestamp).strftime("%m-%d-%Y")
    time.sleep(0.5)
    subprocess.run(["git", "add", DUMMY_FILENAME], shell=True)
    subprocess.run(
        [
            "git",
            "commit",
            "--date",
            '"' + str(unixTimestamp) + '"',
            "-m",
            '"%s"' % dateStr,
        ],
        shell=True,
    )


def commitAll(dailyCommits: list):
    for num in range(len(dailyCommits)):
        for i in range(dailyCommits[num]):
            gitCommit(START_TIMESTAMP + SECONDS_IN_DAY * num)


if __name__ == "__main__":
    main()
