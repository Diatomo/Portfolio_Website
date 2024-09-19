

import os
from pydub import AudioSegment
from app import app

class Synthclips:

    def __init__(self):
        self.directory_path = os.path.join(app.static_folder, 'synth_club_clips')
        self.audioclips = os.listdir(self.directory_path)
        self.audioclips.sort()
        self.audioclips = self.sort_clips()


        self.months = {
            '01': 'January',
            '02': 'February',
            '03': 'March',
            '04': 'April',
            '05': 'May',
            '06': 'June',
            '07': 'July',
            '08': 'August',
            '09': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December'
        }


    def get_section_idxs(self):
        section_indices = []
        current_section = self.audioclips[0][0:4]
        for i in range(len(self.audioclips)):
            section = self.audioclips[i][0:4]
            if (section != current_section):
                current_section = self.audioclips[i][0:4]
                section_indices.append(i)
        section_indices.append(len(self.audioclips))
        return section_indices

    def sort_clips(self):
        section_indices = self.get_section_idxs()
        temp = []
        for i in range(len(section_indices)-1,-1,-1):
            if (i != 0):
                temp.append(self.audioclips[section_indices[i-1]:section_indices[i]])
            else:
                temp.append(self.audioclips[0:section_indices[i]])


        flatten = []
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                flatten.append(temp[i][j])

        return flatten


    def format_sections(self):
        sections = []
        sectionTemp = []

        for clip in self.audioclips:
            section = clip[0:6]
            year = clip[0:2]
            month = clip[2:4]
            day = clip[4:6]
            sectionLabel = self.months[month] + ' - '+ day + ' - ' + '20' + year
            if section not in sectionTemp:
                sectionTemp.append(section)
                entry = {}
                entry['section'] = section
                entry['label'] = sectionLabel
                sections.append(entry)
        return sections

    def format_clips(self):
        result = []
        for clip in self.audioclips:
            temp = {}
            temp['section'] = clip[0:6]
            temp['label'] = clip[7:-14]
            temp['audio'] = clip

            audio = AudioSegment.from_file(self.directory_path + '/' + clip)
            duration_ms = len(audio)
            duration_seconds = duration_ms // 1000
            minutes = duration_seconds // 60
            seconds = duration_seconds % 60

            if (len(str(seconds)) <= 1):
                seconds = str(seconds) + '0'
            temp['length'] = str(minutes) + ':' + str(seconds)

            result.append(temp)
        return result
