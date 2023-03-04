from SocialTravel.models import Post

for _ in range(0,1000):
    Post(carousel_caption_title = "Un carousel Title",
    carousel_caption_description ="Un carousel descrip",
    heading ="Mi viaje",
    description ="una description"
    ).save()



# Post(carousel_caption_title = "Un carousel Title",
#      carousel_caption_description ="Un carousel descrip",
#      heading ="Mi viaje",
#      description ="una description"
#      ).save()
# Post(carousel_caption_title = "Un carousel Title1",
#      carousel_caption_description ="Un carousel descrip1",
#      heading ="Mi viaje1",
#      description ="una description1"
#      ).save()
# Post(carousel_caption_title = "Un carousel Title2",
#      carousel_caption_description ="Un carousel descrip2",
#      heading ="Mi viaje2",
#      description ="una description2"
#      ).save()
# Post(carousel_caption_title = "Un carousel Title3",
#      carousel_caption_description ="Un carousel descrip3",
#      heading ="Mi viaje3",
#      description ="una description3"
#      ).save()