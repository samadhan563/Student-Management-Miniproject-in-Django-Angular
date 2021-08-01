from deepface import DeepFace
result = DeepFace.verify('mimg2.jpeg', 'aimg.jpeg')
print(result['verified'])
if (result['verified']):
    print("matched")
# obj = DeepFace.analyze(img_path = "imga1.jpeg", actions = ['age', 'gender', 'race', 'emotion'])
# print(obj)
# else :
#     print("not matched")
# obj = DeepFace.analyze(img_path = "img2.jpg", actions = ['age', 'gender', 'race', 'emotion'])
# print(obj)
# resp_obj = DeepFace.verify("img1.jpg", "img2.jpg", model_name = "Ensemble")
# print(resp_obj)