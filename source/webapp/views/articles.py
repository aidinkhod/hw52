import random
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'article_create.html')
    print(request.POST)
    context = {
        'name': request.POST.get('name'),
        'age': random.randint(1, 10),
        'happiness_level': random.randint(1, 100),
        'fullness_level': random.randint(1, 100),
        'play': request.POST.get('play')
    }
    # if request.POST.get('play'):
    #     return Cat.play_cat(random.randint(1,100))
    return render(request, 'article.html', context=context)

class Cat:
    play = 0
    sleep =0
    feed = 0
    happiness = 0
    fullness = 0

    def play_cat(self, x: int):
        self.play += x
        if self.play:
            self.happiness += 15
            self.fullness -= 10

    def sleep_cat(self, j: int):
        self.sleep += j
        if self.sleep:
            self.play -= 5

    def feed_cat(self, y: int):
        self.feed += y
        if self.feed:
            self.fullness += 15
            self.happiness += 5

    def happiness_cat(self, z: int):
        self.happiness += z

    def fullness_cat(self, k: int):
        self.fullness += k
        if self.fullness > 100:
            self.happiness -= 30