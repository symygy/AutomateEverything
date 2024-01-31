from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    station_id = fields[0]
    entry_type = fields[2]
    temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0
    return (station_id, entry_type, temperature)

lines = sc.textFile("1800.csv") # data set with minimum temperatures in a year
parsed_lines = lines.map(parseLine)
min_temps = parsed_lines.filter(lambda x: "TMIN" in x[1]) # filter remove data from my rdd
max_temps = parsed_lines.filter(lambda x: "TMAX" in x[1]) # filter remove data from my rdd
station_temps_min = min_temps.map(lambda x: (x[0], x[2]))
station_temps_max = max_temps.map(lambda x: (x[0], x[2]))
min_temps = station_temps_min.reduceByKey(lambda x, y: min(x, y))
max_temps = station_temps_max.reduceByKey(lambda x, y: max(x, y))
results = min_temps.collect()

for result in results:
    print(result[0] + "\t{:.2f}F".format(result[1]))
