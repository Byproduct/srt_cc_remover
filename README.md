# .srt CC remover
English subtitles are sometimes only available as the "CC" versions that include descriptions such as (LOUD EXPLOSION) to help hearing-impaired viewers. 

However, many viewers prefer English subtitles with English audio (e.g. second-language speakers), but have nothing wrong with their ears. For them, CCs are unnecessary and distracting.

I didn't find any software to easily remove CCs from subtitles, so I wrote my own. It removes lines that are fully inside brackets or parentheses (most common way to write CCs), and rebuilds the .srt file accordingly.

Made with Python 3.10.0 and tested only in Windows. It will perhaps run on other systems as well. If not, send me a message or a pull request and we can sort it out. :)

Usage of this program is hopefully self-explanatory.

![screenshot](https://github.com/Byproduct/srt_cc_remover/blob/main/screenshots/ccremover1.png)

![screenshot](https://github.com/Byproduct/srt_cc_remover/blob/main/screenshots/ccremover2.png)

![screenshot](https://github.com/Byproduct/srt_cc_remover/blob/main/screenshots/ccremover3.png)
