from language_tools import LanguageHelper
import unittest

# We define the custom lexicon that we will use for our controlled tests
sample = ('car', 'cat', 'Cate', 'cater', 'care',
          'cot', 'cute', 'dare', 'date', 'dog', 'dodge',
          'coffee', 'pickle', 'grate', 'Rome', 'some', 'home')

rhymesWithDog = ('bog', 'cog', 'clog', 'fog', 'frog', 'hog', 'log')


class BasicTest(unittest.TestCase):
  
    # make sure that all the words in the lexicon are recognized
    def testContainment(self):
        helper = LanguageHelper(sample)
        for w in sample:
            self.assertTrue(w in helper)
  
    def testFailures(self):
        helper = LanguageHelper(sample)
        self.assertFalse('cate' in helper)     # only allowed when capitalized
        self.assertFalse('fox' in helper)      # word is not there
        self.assertFalse('cofee' in helper)    # mis-spell word is not there

    def testSuggestInsertion(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('pikle'), ['pickle'])
        self.assertEqual(helper.getSuggestions('ct'), ['cat','cot'])

    def testSuggestDeletion(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('gratle'), ['grate'])

    def testSugeestionsMany(self):
        helper = LanguageHelper(rhymesWithDog)
        self.assertEqual(helper.getSuggestions('rog'), ['bog','cog','fog','frog','hog','log'])

    def testSugeestionsCapitalization(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('Gate'), ['Cate', 'Date', 'Grate'])

    def testSuggestionsNone(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('blech'), [])

        
    def testSuggestionInvert(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('pcikle'), ['pickle'])
    def testSuggestionCaseSens(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('rome'), ['Rome', 'home', 'some'])
    def testSuggestionCaseSensRandomCap(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('soMe'), ['Rome', 'home', 'some'])
        


if __name__ == '__main__':
    unittest.main()
