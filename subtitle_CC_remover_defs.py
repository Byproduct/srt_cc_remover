import os


# list all files in the input directory that have the .srt extension (case insensitive)
def list_input_directory():
    return [x for x in os.listdir('input') if x.lower().endswith('.srt')]


# remove CC lines from a file, returning tuple: a new file and removed CCs
def remove_cc_lines(input_file):
    CClines = []
    cleaned_text = []

    try:
        with open(input_file) as f:
            for line in f:
                line = line.rstrip()
                if len(line) > 2 and line.startswith(("[", "(")) and line.endswith(("]", ")")):
                    CClines.append(line)
                else:
                    cleaned_text.append(line)
    except:
        pass

    return cleaned_text, CClines


# rebuild subtitle file, discarding sections that are empty after removed CCs.
def rebuild_subtitles(input_text):
    rebuilt_index = 1
    subtitles = []

    for i in range(len(input_text)):
        # find timestamps (e.g. 00:00:05,380 --> 00:00:08,508)
        if re.search("\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d", input_text[i]):
            # after a timestamp is found, add lines to content until empty line is found
            # (empty line separates subtitles in .srt)
            j = i + 1
            subtitle_content = []
            if j < len(input_text) - 1:
                while input_text[j]:
                    subtitle_content.append(input_text[j])
                    j = j + 1
                    # break at the end of file to avoid index OOB
                    if j == len(input_text):
                        break
                if subtitle_content:
                    subtitle = {
                        "index": rebuilt_index,
                        "timestamp": input_text[i],
                        "content": subtitle_content
                    }
                    subtitles.append(subtitle)
                    rebuilt_index = rebuilt_index + 1

    rebuilt_text = []
    for subtitle in subtitles:
        rebuilt_text.append(str(subtitle["index"]))
        rebuilt_text.append(subtitle["timestamp"])
        for line in subtitle["content"]:
            rebuilt_text.append(line)
        rebuilt_text.append("\n")

    return rebuilt_text


def clean_single_file(input_file):
    report = "Couldn't process file (error or cancelled by user)."
    if input_file:
        cleaned_text, CClines = remove_cc_lines(input_file)
        report = "opened file: \n" + input_file + "\n"

        # if no CC lines found in file, do nothing
        if not CClines:
            report = report + "\nNo CC lines detected in this file."
            return report

        # if CC lines found, rebuild file
        else:
            output_file = 'output/' + os.path.basename(input_file)
            rebuilt_text = rebuild_subtitles(cleaned_text)
            try:
                f = open(output_file, "w")
                for line in rebuilt_text:
                    if "\n" in line:
                        f.write(line)
                    if "\n" not in line:
                        f.write(line + "\n")
                f.close()
                report = report + "\nNew file written in output folder."
                report = report + "\nDetected and cleaned " + str(len(CClines)) + " CC lines:\n\n"
                for line in CClines:
                    report = report + line + "\n"
            except:
                report = report + "\nUnable to write output file " + output_file
    return report


def clean_multiple_files(input_files):
    report = ""
    if len(input_files) == 0:
        report = "No subtitle files found in the input folder."
        return report
    else:
        for filename in input_files:
            cleaned_text, CClines = remove_cc_lines("input/" + filename)
            if not CClines:
                report = report + "\n" + str(filename) + ": \nno CC lines detected.\n"
            if CClines:
                rebuilt_text = rebuild_subtitles(cleaned_text)
                report = report + "\n" + str(filename) + ": \n" + str(len(CClines)) + " CC lines removed.\n"
                try:
                    output_file = 'output/' + os.path.basename(filename)
                    f = open(output_file, "w")
                    for line in rebuilt_text:
                        if "\n" in line:
                            f.write(line)
                        if "\n" not in line:
                            f.write(line + "\n")
                    f.close()
                except:
                    report = report + "\nUnable to write output file " + output_file

    return report