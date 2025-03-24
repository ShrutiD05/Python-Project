import os
import cv2
import pickle
import numpy as np
import face_recognition

def saveEncodings(encs, names, fname="encodings.pickle"):
    data = [{"name": nm, "encoding": enc} for (nm, enc) in zip(names, encs)]
    with open(fname, "wb") as f:
        pickle.dump(data, f)
    print(f"[INFO] Encodings saved to {fname}")

def readEncodingsPickle(fname):
    with open(fname, "rb") as f:
        data = pickle.load(f)
    encodings = [d["encoding"] for d in data]
    names = [d["name"] for d in data]
    return encodings, names

def createEncodings(image):
    face_locations = face_recognition.face_locations(image)
    known_encodings = face_recognition.face_encodings(image, known_face_locations=face_locations)
    print(f"[INFO] Detected {len(face_locations)} faces.")
    return known_encodings, face_locations

def compareFaceEncodings(unknown_encoding, known_encodings, known_names):
    if not known_encodings:
        return False, "Unknown", float("inf")

    matches = face_recognition.compare_faces(known_encodings, unknown_encoding, tolerance=0.5)
    face_distances = face_recognition.face_distance(known_encodings, unknown_encoding)

    best_match_index = np.argmin(face_distances)
    distance = face_distances[best_match_index]

    if matches[best_match_index]:
        return True, known_names[best_match_index], distance
    else:
        return False, "Unknown", distance

def saveImageToDirectory(image, name, imageName):
    path = os.path.join("output", name)
    os.makedirs(path, exist_ok=True)
    cv2.imwrite(os.path.join(path, imageName), image)

def processKnownPeopleImages(path="People", saveLocation="known_encodings.pickle"):
    known_encodings = []
    known_names = []
    for img in os.listdir(path):
        imgPath = os.path.join(path, img)
        image = cv2.imread(imgPath)
        if image is None:
            print(f"[WARNING] Could not read image {imgPath}. Skipping.")
            continue
        name = os.path.splitext(img)[0]
        encs, locs = createEncodings(image)
        for enc in encs:
            known_encodings.append(enc)
            known_names.append(name)
    saveEncodings(known_encodings, known_names, saveLocation)

def processDatasetImages(path="Dataset", saveLocation="dataset_encodings.pickle"):
    people_encodings, names = readEncodingsPickle("known_encodings.pickle")
    for img in os.listdir(path):
        imgPath = os.path.join(path, img)
        image = cv2.imread(imgPath)
        if image is None:
            print(f"[WARNING] Could not read image {imgPath}. Skipping.")
            continue
        print(f"[INFO] Processing image {imgPath} with shape {image.shape}")

        orig = image.copy()
        encs, locs = createEncodings(image)
        
        knownFlag = False
        for i, loc in enumerate(locs):
            top, right, bottom, left = loc
            unknown_encoding = encs[i]
            acceptBool, duplicateName, distance = compareFaceEncodings(unknown_encoding, people_encodings, names)
            saveImageToDirectory(orig, duplicateName if acceptBool else "Unknown", img)
            cv2.rectangle(image, (left, top), (right, bottom), color=(255, 0, 0), thickness=2)
            knownFlag = True
        
        if not knownFlag:
            saveImageToDirectory(orig, "Unknown", img)
        
        cv2.imshow("Image", image)
        cv2.waitKey(10)
        cv2.destroyAllWindows()

def main():
    processKnownPeopleImages()
    processDatasetImages()
    print("Completed")

if __name__ == "__main__":
    main()
