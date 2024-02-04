# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1
from movies import movies
def first(mov):
    mo = input()
    for i in mov:
        if i["name"] == x and i["imdb"] > 5.5:
            print(True)
first(movies)

#2
def second(mlist = []):
    for i in movies:
        if i["imdb"] > 5.5:
            mlist.append(i)
    return mlist
print(second())

#3
def third(cname = input()):
    mlist = []
    for i in movies:
        if i["category"] == cname:
            mlist.append(i["name"])
    return mlist
print(third())

#4
def fourth(movies):
    score = 0
    nmov = len(movies)
    for i in movies:
        score +=i["imdb"]
    if nmov > 0:
        return score / nmov
    else:
        return 0
print(fourth(movies))

#5
def fifth(cname = input()):
    score = 0
    nmov = 0
    for i in movies:
        if i["category"] == cname:
            score = score + i["imdb"]
            nmov+=1 
    if nmov > 0:
        return score / nmov
    else:
        return 0
print(fifth())
