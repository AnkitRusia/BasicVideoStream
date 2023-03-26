VIDEO_EXTENSION = set(("webm", "mp4"))
POSTER = "DefaultPoster.jpg"
POSTER_EXTENSION = ".png"

def get_extension(name: str) -> str:
    return name.split(".")[-1]

def get_name_without_extensoion(name: str) -> str:
    return "".join(name.split(".")[:-1])

def get_name_and_extension(name: str) -> str:
    *name, ext = name.split(".")
    return (".".join(name), ext)

def match_pattern_subsequence(filename: str, pattern: str) -> bool:
    pattern = pattern.replace(" ", "")
    def isSubSequence(string1, string2, m, n):
        # Base Cases
        if m == 0:
            return True
        if n == 0:
            return False
    
        # If last characters of two
        # strings are matching
        if string1[m-1] == string2[n-1]:
            return isSubSequence(string1, string2, m-1, n-1)
    
        # If last characters are not matching
        return isSubSequence(string1, string2, m, n-1)
    
    return isSubSequence(pattern.lower(), filename.lower(), len(pattern), len(filename))