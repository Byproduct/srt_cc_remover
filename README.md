# .srt CC remover
English subtitles are sometimes only available as the "CC" versions that include descriptions such as (LOUD EXPLOSION) to help hearing-impaired viewers. 

However, many viewers prefer English subtitles with English audio (e.g. second-language speakers), but have nothing wrong with their ears. For them, CCs are unnecessary and distracting.

This little program removes lines that are fully inside brackets or parentheses (most common way to write CCs), and rebuilds the .srt file accordingly.

Made with Python 3.10.0 and tested only in Windows. It will perhaps run on other systems as well. If not, send me a message or a pull request and we can sort it out. :)

Usage this program is hopefully straight-forward. Open a single file or place multiple files in the "input" folder inside this program folder. "Cleaned" files will appear in the "output" folder.

&nbsp;
![screenshot](https://github.com/Byproduct/srt_cc_remover/blob/main/screenshots/ccremover1.png)
Main screen

&nbsp;
![screenshot](https://github.com/Byproduct/srt_cc_remover/blob/main/screenshots/ccremover2.png)
Cleaning one file

&nbsp;
![screenshot](https://github.com/Byproduct/srt_cc_remover/blob/main/screenshots/ccremover3.png)
Cleaning a folder
