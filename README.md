# wordle_help
Messing around with some ideas about wordle.

I didnt want to make something that would actually tell me the answer.  Seemed too much like cheating.  But wanted something that would partially guide?

Started with a dictionary list of words that are on most(all?) unix type systems.  Called Web2.  On Mac it is at /usr/share/dict.  One caution - it is from Websters Second dictionary.  But they had to use a version that has an elapsed copyright.  This dictionary is from 1934.  It has over 234k english words -  it will miss many.  (ie internet, blog, etc.)  However for this purpose it works fine.

create_list.py will take the web2 file and break it into a smaller file with a specfic letter length.  For instance in wordle all words are 5 letters long.  That is what the default letter is set to.

letter_count.py = basically makes a python dictionary file with the count of letters for all words in a list.  ie a=5000 would mean there were 5000 a's in a list.  The idea is we need a way to rank which letters are of significance in the list.  So when choosing letters - especially to start with we choose letters with high occurence.  

word_rank.py - will actually give you the top 10 highest ranked words.  It will also let you exclude/include letters.  An example of one of the highest ranked words would be "arise"  It has five letters that are very heavily used - thus identifiying if they are part of the Wordle would be very helpful and allow you to considerable shrink the list for the second word.

After you create your word list and letter_ count dictionary you can continue to use those.  You would just run word_rank.py each time.  Only running the others if you have another set of data to use.  