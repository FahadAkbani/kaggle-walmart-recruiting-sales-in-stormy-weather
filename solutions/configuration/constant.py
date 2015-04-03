import os
class Constant(object):

    class Filesystem(object):
        ROOT_FOLDER = '/' + '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[1:-3]) + '/'
        DATA_FOLDER = ROOT_FOLDER + 'Data/'
        INPUT_FOLDER = DATA_FOLDER + 'Input/'
        TRAIN_FILE = INPUT_FOLDER + 'train.csv'
        TEST_FILE = INPUT_FOLDER + 'test.csv'
        WEATHER_FILE = INPUT_FOLDER + 'weather.csv'
        STORE_STATION_ID_FILE = INPUT_FOLDER + 'key.csv'

    class DataColumns(object):
         
        class TrainRawData(object):
            DATE = 'date'
            STORE_NBR = 'store_nbr'
            ITEM_NBR = 'item_nbr'
            UNITS = 'units'
            KEYS = [DATE, STORE_NBR, ITEM_NBR, UNITS]

        class TestRawData(object):
            DATE = 'date'
            STORE_NBR = 'store_nbr'
            ITEM_NBR = 'item_nbr'
            KEYS = [DATE, STORE_NBR, ITEM_NBR]

        class WeatherRawData(object):
            STATION_NBR = 'station_nbr'
            DATE = 'date'
            TMAX = 'tmax'
            TMIN = 'tmin'
            TAVG = 'tavg'
            DEPART = 'depart'
            DEWPOINT = 'dewpoint'
            WETBULB = 'wetbulb'
            HEAT = 'heat'
            COOL = 'cool'
            SUNRISE = 'sunrise'
            SUNSET = 'sunset'
            CODESUM = 'codesum'
            SNOWFALL = 'snowfall'
            PRECIPTOTAL = 'preciptotal'
            STNPRESSURE = 'stnpressure'
            SEALEVEL = 'sealevel'
            RESULTSPEED = 'resultspeed'
            RESULTDIR = 'resultdir'
            AVGSPEED = 'avgspeed'

            KEYS = [STATION_NBR, DATE, TMAX, TMIN, TAVG, DEPART, DEWPOINT, WETBULB, HEAT,
                    COOL, SUNRISE, SUNSET, CODESUM, SNOWFALL, PRECIPTOTAL, STNPRESSURE,
                    SEALEVEL, RESULTSPEED, RESULTDIR, AVGSPEED]

        class StoreStationIdRawData(object):
             STORE_NBR = 'store_nbr'
             STATION_NBR = 'station_nbr'
             KEYS = [STORE_NBR, STATION_NBR]
