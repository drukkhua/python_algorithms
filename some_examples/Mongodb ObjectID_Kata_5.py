'''
Original kata from the CodeWars: https://www.codewars.com/kata/52fefe6cb0091856db00030e/
MongoDB is a noSQL database which uses the concept of a document, rather than a table as in SQL. Its popularity is growing.

As in any database, you can create, read, update, and delete elements. But in constrast to SQL, when you create an element,
a new field _id is created. This field is unique and contains some information about the time the element was created,
id of the process that created it, and so on. More information can be found in the MongoDB documentation (which you have to read
in order to implement this Kata).

So let us implement the following helper which will have 2 methods:

one which verifies that the string is a valid Mongo ID string, and
one which finds the timestamp from a MongoID string
Note:

If you take a close look at a Codewars URL, you will notice each kata's id (the XXX in http://www.codewars.com/dojo/katas/XXX/train/javascript)
is really similar to MongoDB's ids, which brings us to the conjecture that this is the database powering Codewars.
'''

from datetime import datetime
import re

class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        return isinstance(s, str) and bool(re.match(r'[0-9a-f]{24}$', s))
    
    @classmethod
    def get_timestamp(cls, s):
        return cls.is_valid(s) and datetime.fromtimestamp(int(s[:8], 16))
