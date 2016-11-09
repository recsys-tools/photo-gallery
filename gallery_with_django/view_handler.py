import os


def get_context_gallery(path, page_id):
    num_images_display = 60

    if page_id is None:
        page_id = 0
    else:
        page_id = int(page_id)

    file_list = []

    for filename in os.listdir(path):

        if '.JPG' in filename.upper() or '.JPEG' in filename.upper():
            file_list.append(filename)

    file_list = sorted(file_list)

    num_files = len(file_list)
    num_pages = num_files / num_images_display

    if num_files % num_images_display > 0:
        num_pages += 1

    if page_id == 0:
        prev_page = 0
    else:
        prev_page = page_id - 1

    next_page = page_id + 1

    current_start = page_id * num_images_display
    current_end = (next_page * num_images_display) - 1

    if current_end >= len(file_list):
        current_end = len(file_list)
        next_page = page_id

    image_data_list = file_list[current_start:current_end]

    image_data_list = sorted(image_data_list)

    context = {
        'num_pages': num_pages,
        'current_page': page_id + 1,
        'local_path': path,
        'image_data_list': image_data_list,
        'current': page_id,
        'next': next_page,
        'prev': prev_page
    }

    return context


def delete(dst_dir, files):
    for filename in files:
        file_path = os.path.join(dst_dir, filename)

        if os.path.exists(file_path):
            os.remove(file_path)
