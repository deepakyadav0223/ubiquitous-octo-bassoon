# Python program for face
# comparision


from __future__ import print_function, unicode_literals
from facepplib import FacePP, exceptions
import emoji

# define global variables
face_detect = ""
faceset_init= ""
face_search = ""
face_landmarks = ""
dense_facial_landmarks = ""
face_attri = ""
beauty_score_and_emotion_recognition = ""


# define face comparing function
def face_comparing(app, Image1, Image2):
    print()
    print('-' * 30)
    print('Comparing Photographs......')
    print('-' * 30)

    cmp_ = app.compare.get(image_url1=Image1,
                           image_url2=Image2)

    print('Photo1', '=', cmp_.image1)
    print('Photo2', '=', cmp_.image2)

    # Comparing Photos
    if cmp_.confidence > 70:
        print('Both photographs are of same person......')
    else:
        print('Both photographs are of two different persons......')

    # Driver Code


if __name__ == '__main__':

    # api details
    api_key = 'xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
    api_secret = 'TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'

    try:

        # create a logo of app by using iteration,
        # unicode and emoji module-------------
        for i in range(1, 6):

            for j in range(6, -i):
                print(" ", end=" ")

            for j in range(1, i):
                print('\U0001F600', end=" ")

            for j in range(i, 0, -1):
                print('\U0001F6A3', end=" ")

            for j in range(i, 1, -2):
                print('\U0001F62B', end=" ")

            print()

        print()

        # print name of the app--------
        print("\t\t\t" + "Photo Comparing App\n")

        for i in range(1, 6):

            for j in range(6, -i):
                print(" ", end=" ")

            for j in range(1, i):
                print(emoji.emojize(":princess:"), end=" ")

            for j in range(i, 0, -1):
                print('\U0001F610', end=" ")

            for j in range(i, 1, -2):
                print(emoji.emojize(":baby:"), end=" ")

            print()

        # call api
        app_ = FacePP(api_key=api_key,
                      api_secret=api_secret)
        funcs = [
            face_detect,
            faceset_init,
            face_search,
            face_landmarks,
            dense_facial_landmarks,
            face_attri,
            beauty_score_and_emotion_recognition
        ]
        # go to "https://postimages.org/" and upload your photo and get the direct link
        # Pair 1
        image1 = " directLink here"
        image2 = "direct link here"
        face_comparing(app_, image1, image2)



    except exceptions.BaseFacePPError as e:
        print('Error:', e)
