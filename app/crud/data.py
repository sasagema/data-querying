from sqlalchemy.orm import Session
from app.model import models


def insert_data(db: Session):
    user1 = models.User(username="tom22", name="Tom", email="tom22@email.com")
    user2 = models.User(username="jerry33", name="Jerry", email="jerry33@email.com")
    post1 = models.Post(title="Beware: A cheese crisis looms", content="A collapse in fungi diversity threatens Camembert, brie, and other famous French cheeses.", status="published", user=user2)
    post2 = models.Post(title="Post2 Title", content="Post2 Content", status="draft", user=user1)
    # post3 = models.Post(title="Post3 Title", content="Post3 Content", status="published",user=user2)
    # post4 = models.Post(title="Post4 Title", content="Post4 Content", status="draft",user=user2)
    comment1 = models.Comment(content="You can buy a tofu.", user=user1, post=post1)
    comment2 = models.Comment(content="Tofu is not a cheese!", user=user2, post=post1)
    comment3 = models.Comment(content="Whatewer, I don't eat cheese.", user=user1, post=post1)
    comment4 = models.Comment(content="Comment4 Content", user=user2, post=post2)
    comment5 = models.Comment(content="Comment5 Content", user=user1, post=post2)
    comment6 = models.Comment(content="Comment6 Content", user=user2, post=post2)
    tag1 = models.Tag(name="important")
    tag2 = models.Tag(name="cheese")
    # tag2 = models.Tag(name="dog")
    post1.comments.append(comment1)
    post1.comments.append(comment2)
    post1.comments.append(comment3)
    post1.tags.append(tag1)
    post1.tags.append(tag2)

    post2.comments.append(comment4)
    post2.comments.append(comment5)
    post2.comments.append(comment6)
    post2.tags.append(tag1)
    
     
    db.add(post1)
    db.add(post2)
    db.commit()
    return "ok"