import nltk
import os
import sys
from sys import path
'''The NLTK corpus is a massive dump of all kinds of natural language data sets that are definitely worth taking a look at.
Almost all of the files in the NLTK corpus follow the same rules for accessing them by using the NLTK module, but nothing is magical about them.
These files are plain text files for the most part, some are XML and some are other formats, but they are all accessible by you manually, or via
the module and Python. Let's talk about viewing them manually.
Depending on your installation, your nltk_data directory might be hiding in a multitude of locations. To figure out where it is, head to your Python directory,
 where the NLTK module is.'''

print(nltk.__file__)  # Displays the output of the nltk location file!
if sys.platform.startswith('win'):
    # Common locations on Windows:
    path += [
        str(r'C:\nltk_data'), str(r'D:\nltk_data'), str(r'E:\nltk_data'),
        os.path.join(sys.prefix, str('nltk_data')),
        os.path.join(sys.prefix, str('lib'), str('nltk_data')),
        os.path.join(os.environ.get(str('APPDATA'), str('C:\\')), str('nltk_data'))
    ]
else:
    # Common locations on UNIX & OS X:
    path += [
        str('/usr/share/nltk_data'),
        str('/usr/local/share/nltk_data'),
        str('/usr/lib/nltk_data'),
        str('/usr/local/lib/nltk_data')
    ]


from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
sample = gutenberg.raw("bible-kjv.txt")
took_nized = sent_tokenize(sample)
print(took_nized[0:5])

# You can open the Modile and You can look at the Data from the Natural Language Kit tool, So that you can
# Use other data in other Programs .

