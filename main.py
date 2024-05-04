import sys

def get_videos():
    pass

def upload_details():
    pass

def upload_videos():
    pass

def mark_videos():
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
