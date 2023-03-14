class Stats():
    #отслеживает статистику
    def __init__(self):
        #инициализирует статистику
        self.reset_stats()
        self.run_game = True
        with open('python_game\highscore.txt', 'r') as f:
            self.high_score = int(f.readline())


    def reset_stats(self):
        self.mans_health = 3
        self.score = 0