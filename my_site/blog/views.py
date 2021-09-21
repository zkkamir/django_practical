from datetime import date
from django.shortcuts import render


all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "max.png",
        "author": "Max",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit, amet  adipisicing elit. Veniam, optio aut temporibus nemo nihil, nisi deleniti velit quis ex ratione tempore harum numquam, quia ut modi asperiores? Ex, ipsam temporibus?",
        "content": """
            Lorem ipsum dolor sit, amet  adipisicing elit. Veniam,
            optio aut temporibus nemo nihil, nisi deleniti velit
            quis ex ratione tempore harum numquam, quia ut modi
            asperiores? Ex, ipsam temporibus?

            Lorem ipsum dolor sit, amet  adipisicing elit. Veniam,
            optio aut temporibus nemo nihil, nisi deleniti velit
            quis ex ratione tempore harum numquam, quia ut modi
            asperiores? Ex, ipsam temporibus?

            Lorem ipsum dolor sit, amet  adipisicing elit. Veniam,
            optio aut temporibus nemo nihil, nisi deleniti velit
            quis ex ratione tempore harum numquam, quia ut modi
            asperiores? Ex, ipsam temporibus?
            """
    },
    {
        "slug": "jungle",
        "image": "max.png",
        "author": "Max",
        "date": date(2021, 2, 1),
        "title": "jungle",
        "excerpt": "jungle Lorem ipsum dolor sit, amet  adipisicing elit. Veniam, optio aut temporibus nemo nihil, nisi deleniti velit quis ex ratione tempore harum numquam, quia ut modi asperiores? Ex, ipsam temporibus?",
        "content": """
            Lorem ipsum dolor sit, amet  adipisicing elit. Veniam,
            optio aut temporibus nemo nihil, nisi deleniti velit
            quis ex ratione tempore harum numquam, quia ut modi
            asperiores? Ex, ipsam temporibus?

            Lorem ipsum dolor sit, amet  adipisicing elit. Veniam,
            optio aut temporibus nemo nihil, nisi deleniti velit
            quis ex ratione tempore harum numquam, quia ut modi
            asperiores? Ex, ipsam temporibus?

            Lorem ipsum dolor sit, amet  adipisicing elit. Veniam,
            optio aut temporibus nemo nihil, nisi deleniti velit
            quis ex ratione tempore harum numquam, quia ut modi
            asperiores? Ex, ipsam temporibus?
            """
    },
    {
        "slug": "sea",
        "image": "max.png",
        "author": "Max",
        "date": date(2021, 5, 14),
        "title": "sea",
        "excerpt": "Lorem sea ipsum dolor sit, amet  adipisicing elit. Veniam, optio aut temporibus nemo nihil, nisi deleniti velit quis ex ratione tempore harum numquam, quia ut modi asperiores? Ex, ipsam temporibus?",
        "content": """
            Lorem ipsum dolor sit, amet  adipisicing elit. Veniam,
            optio aut temporibus nemo nihil, nisi deleniti velit
            quis ex ratione tempore harum numquam, quia ut modi
            asperiores? Ex, ipsam temporibus?

            Lorem ipsum dolor sit, amet  adipisicing elit. Veniam,
            optio aut temporibus nemo nihil, nisi deleniti velit
            quis ex ratione tempore harum numquam, quia ut modi
            asperiores? Ex, ipsam temporibus?

            Lorem ipsum dolor sit, amet  adipisicing elit. Veniam,
            optio aut temporibus nemo nihil, nisi deleniti velit
            quis ex ratione tempore harum numquam, quia ut modi
            asperiores? Ex, ipsam temporibus?
            """
    }
]


def starting_page(request):
    sorted_posts = sorted(all_posts, key=lambda x: x["date"])
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", context={
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
