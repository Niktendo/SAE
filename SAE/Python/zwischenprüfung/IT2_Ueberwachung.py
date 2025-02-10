def deleteOldFiles():
    while getTotalFileSize() >= 1000000000:
        deleteFileVyName(getOldestFileName())