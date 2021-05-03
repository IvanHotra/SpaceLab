class Format:
    def __repr__(self):
        raise NotImplementedError

class FormatMP3:
    def __repr__(self):
        return 'It is a audio file'

class FormatMP4:
    def __repr__(self):
        return 'It is a video file'

class Player:
    def openFile(self,_format):
        if _format == 'MP3':
            return FormatMP3
        elif _format == 'MP4':
            return FormatMP4
        else:
            return Format

a = Player()
a.openFile('MP3')
a.openFile('.exe')