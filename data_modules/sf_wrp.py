def key():
    with open('./local_data/simfin') as f:
        content = f.read().splitlines()
    return content[0]
