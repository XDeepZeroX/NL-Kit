from algorithms import replace_time, tokenization, summ_purchase
import unittest

    
class TestTokenizationMethod(unittest.TestCase):
    def test_tokenization1(self):
        s = 'hello world ! How are you ?'
        self.assertEqual(tokenization(s), ['hello world !', 'How are you ?'])

    def test_tokenization2(self):
        s = '''
        hello world ! How are you ?
        , i.e.
        '''
        self.assertEqual(tokenization(s), ['hello world !', 'How are you ?', ', i.e.'])

    def test_tokenization3(self):
        s = 'Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. He paid a lot for it!'
    
        self.assertEqual(tokenization(s),
                         ['Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e.', 'He paid a lot for it!'])
    def test_tokenization4(self):
        s = 'Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it!'
    
        self.assertEqual(tokenization(s), ['Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it!'])


    def test_tokenization5(self):
        s = 'Mr. Smith bought cheapsite.com for 1.5 million dollars, i <space> e <space>  he paid a lot for it!'

        self.assertEqual(tokenization(s), [s])


    def test_tokenization7(self):
        s = '''
    Разделить текст на предложения и т.п. Тест...
    Mr.A. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it! Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't.
    "Как дела ?" -- поинтересовалась Алиса.
            '''

        self.assertEqual(tokenization(s), ['Разделить текст на предложения и т.п.',
                                       'Тест...',
                                       'Mr.A. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it!',
                                       'Did he mind?',
                                       "Adam Jones Jr. thinks he didn't.",
                                       "In any case, this isn't true...",
                                       "Well, with a probability of .9 it isn't.",
                                       '"Как дела ?" -- поинтересовалась Алиса.'])

class TestReplaceTimeMethod(unittest.TestCase):
    def test_base(self):
        s = 'Найти время в фразе и заменить его на (TBD) Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю. PS. С отношением 25:50 всё нормально!'
        self.assertEqual(replace_time(s), 'Найти время в фразе и заменить его на (TBD) Уважаемые! Если вы к (TBD) не вернёте чемодан, то уже в (TBD) я за себя не отвечаю. PS. С отношением 25:50 всё нормально!')
    
    def test2(self):
        arr = ['00:00', '10:00', '1:00', '01:00', '00:00:00', '01:01:01', '1:00:00']
        s = ' '.join(arr)
        self.assertEqual(replace_time(s), ' '.join(['(TBD)'] * len(arr)))
    
    def test3(self):
        arr = ['25:00', '100:10', '10:70', '001:00', '31:00:00', '10:01:90', '10:99:00']
        s = ' '.join(arr)
        self.assertEqual(replace_time(s), s)

class TestSummPurchaseMethod(unittest.TestCase):
    def test_base(self):
        tests = [
            {'input': 'Посчитать сумму закупки Было закуплено 12 единиц техники по 410.37 рублей.', 'output': 4_924.44 },
            {'input': 'Было закуплено 51.5 ящиков мандаринов по 1004.15 рубля.', 'output': 51_713.725 },
            {'input': 'Были закуплено 2 танка т-34 по 20 000 000.12 рублей. ', 'output': 40_000_000.24 },
            {'input': 'Были закуплено 4 танка т-34 по 20_000_000,10 рублей. ', 'output': 80_000_000.4 },
        ]
        for test in tests: 
            self.assertEqual(summ_purchase(test['input']), test['output'])
    
if __name__ == '__main__':
    unittest.main()

