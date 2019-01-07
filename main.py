from request_thread import RequestThread

def main():
    sources = {}

    try:
        f = open('sources.txt')
    except OSError:
        print('Could not open file')
        exit()

    for line in f:
        title, link = line.split('-')
        sources[title] = link

    for source in sources:
        thread = RequestThread(sources[source])
        thread.start()

if __name__ == '__main__':
    main()