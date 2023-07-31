# Author: Mingxuan, Liu
# Put this file under iNatLoc500 dataset root to correct the annotation

import json
# from PIL import Image
# import imagesize
import cv2


def dump_json(filename: str, in_data):
    if not filename.endswith('.json'):
        filename += '.json'

    with open(filename, 'w') as fbj:
        if isinstance(in_data, dict):
            json.dump(in_data, fbj, indent=4)
        elif isinstance(in_data, list):
            json.dump(in_data, fbj)
        else:
            raise TypeError(f"in_data has wrong data type {type(in_data)}")


def load_json(filename: str):
    if not filename.endswith('.json'):
        filename += '.json'
    with open(filename, 'r') as fp:
        return json.load(fp)


def dump_txt(filename: str, in_data: str):
    if not filename.endswith('.txt'):
        filename += '.txt'

    with open(filename, 'w') as fbj:
        fbj.write(in_data)


def load_txt(filename: str):
    if not filename.endswith('.txt'):
        filename += '.txt'
    with open(filename, 'r') as fbj:
        return fbj.read()


def get_real_image_size(file_path):
    # w, h = imagesize.get(file_path)
    # img = Image.open(open(file_path, 'rb'))
    # w = img.size[0]
    # h = img.size[1]
    img = cv2.imread(file_path)
    h, w, _ = img.shape
    return w, h


def txt2size(path, real_size=False):
    entries = []

    raw_t = load_txt(path)
    raw_t = raw_t.strip()
    raw_t = raw_t.split('\n')

    for lin in raw_t:
        lin = lin.strip()
        file_name = lin.split(',')[0]

        w, h = (
            get_real_image_size(file_name)
            if real_size else
            (int(lin.split(',')[-1]), int(lin.split(',')[-2]))
                )

        e = {'file_name': file_name, 'width': w, 'height': h}
        print(f"{file_name}: {w} x {h}")
        entries.append(e)
    return entries


def compare_image_sizes(og_inat, real_inat):
    assert len(og_inat) == len(real_inat)
    diff_record = []
    for entry1, entry2 in zip(og_inat, real_inat):
        assert entry1['file_name'] == entry2['file_name']
        if (entry1['width'] != entry2['width']) or (entry1['height'] != entry2['height']):
            diff_record.append(
                {
                    "file_name": entry1['file_name'],
                    "og_width": entry1['width'],
                    "og_height": entry1['height'],
                    "actual_width": entry2['width'],
                    "actual_height": entry2['height'],
                }
            )
    return diff_record, len(diff_record)


def dump_correction(filename, real_inat):
    if not filename.endswith('.txt'):
        filename += '.txt'
    with open(filename, 'w') as fbj:
        for entry in real_inat:
            fbj.write(f"{entry['file_name']},{entry['height']},{entry['width']}\n")


if __name__ == "__main__":
    path_splits = [
        {
            "original": "original_annotation/val/image_sizes.txt",
            "corrected": "original_annotation/val/val_image_sizes_corrected.txt",
            "different": "original_annotation/val/val_different_image_sizes.json"
        },
        {
            "original": "original_annotation/test/image_sizes.txt",
            "corrected": "original_annotation/test/test_image_sizes_corrected.txt",
            "different": "original_annotation/test/test_different_image_sizes.json"
        }
    ]

    for split in path_splits:
        og_inat = txt2size(split['original'], real_size=False)
        real_inat = txt2size(split['original'], real_size=True)

        diff_record, num_diff = compare_image_sizes(og_inat, real_inat)

        dump_json(split['different'], diff_record)
        print(f"Dumped the different annotation to {split['different']}")

        dump_correction(split['corrected'], real_inat)
        print(f"Dumped the corrected annotation to {split['corrected']}")

