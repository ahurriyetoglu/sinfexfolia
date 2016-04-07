from pynlpl.formats import folia

tweets_doc = folia.Document(id="tweetlist1")
tweets_doc.declare(folia.Event, "https://raw.githubusercontent.com/ahurriyetoglu/sinfexfolia/master/sinfex-event.foliaset.xml")
tweets_doc.declare(folia.Entity, "https://raw.githubusercontent.com/ahurriyetoglu/sinfexfolia/master/sinfex-entities.foliaset.xml")

textbody = tweets_doc.append(folia.Text)

for tw in tweets_df.text.values[:250]:
    tweet = folia.Event(tweets_doc, cls='tweet',generate_id_in=textbody)
    for t in tw.split():
        tweet.append(folia.Word, text=t) #,space=space)
    #tweet.append(folia.Word, text="",space=space)
    textbody.append(tweet)

tweets_doc.save("tst.folia.xml")
