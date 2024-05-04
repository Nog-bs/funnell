import sys

def get_videos():
    """
    Gets the videos from a specific directory.
    Should be looking for videos that have not been added previously.

    :return: list of strings that represent the videos to be uploaded
    """
    pass

def upload_details(videos):
    """
    For the given videos we will prompt the user to enter the details needed to be sent to YouTube.

    :param videos: list of strings that represent the videos to be uploaded
    :return: a list of dictionaries that represent the details needed to be sent to YouTube
    """
    pass

def upload_videos():
    """
    WORK IN PROGRESS...
    """
    pass

def mark_videos():
    """
    Takes the previously uploaded videos and marks them in the directory.

    :param videos: list of strings that represent the videos to be uploaded
    """
    pass

def main():
    """ Drives the program """
    videos_path = get_videos()
    videos_to_upload = upload_details(videos_path)
    try:
        upload_videos(videos_to_upload)
    except:
        print("Seems like there was an issue: {}", file=sys.stderr)
        return
    mark_videos(videos_to_upload)
    print("Videos uploaded to Youtube, keep on dancing!")


if __name__ == '__main__':
    main()
