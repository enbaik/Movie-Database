import csv
import re
with open('movies.csv', 'rt', encoding = 'utf-8') as movies:
    reader = csv.reader(movies)

    with open('processed_movies.csv', 'w', encoding = 'utf-8') as processedFile:
        writer = csv.writer(processedFile)
    
        next(reader)
        genres = set()

        for line in reader:
            genre = line[2].split("|")
            size = len(genre)
            for i in range (0,len(genre)):
                genres.add(genre[i])

        genres = sorted(genres,reverse = True)
        genreCheck = []
        movies.seek(0)
        columns = next(reader)
        columns.append('year')

        for i in range(0,len(genres)):
            addg = genres.pop()
            genreCheck.append(addg)
            columns.append(addg)

        writer.writerow(columns)

        for line in reader:
            # seperates year into new column
            title = line[1]
            regex = re.compile(r'\((\d+)\)')
            temp = regex.search(title)
            if temp is not None:
                year = regex.search(title).group(1)
                year = int(year)
            else:
                year = 'Not Found';
            

            newline = [0] * (4 + len(genreCheck))
            genre = line[2].split("|")

            newline[0] = line[0]
            newline[1] = line[1]
            newline[2] = line[2]
            newline[3] = year

            for j in range (0,len(genre)):
                    for k in range (0,len(genreCheck)):
                        if genre[j] == genreCheck[k]:
                            newline[k + 4] = 1

            writer.writerow(newline)