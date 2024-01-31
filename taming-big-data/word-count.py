from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf = conf)

input = sc.textFile("book.txt")
words = input.flatMap(lambda x: x.split()) #can create many new elements from each one
word_counts = words.countByValue()

for word, count in word_counts.items():
    clean_word = word.encode('ascii', 'ignore')
    if (clean_word):
        print(clean_word.decode() + " " + str(count))
