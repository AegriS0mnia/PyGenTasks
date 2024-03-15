def chunker(line):
    chunks = []
    while len(line) > 0:
        chunks.append(line[:chunk_size])
        line = line[chunk_size:]

    print(chunks)


line = input().split()
chunk_size = min(len(line), int(input()))

chunker(line)
