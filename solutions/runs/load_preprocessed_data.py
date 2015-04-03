from solutions.core.preprocess_data.preprocess_data_01_only_load_training import PreprocessData01OnlyLoadTraining

def main():
    print 'Started Loading'
    processDataTool = PreprocessData01OnlyLoadTraining()
    train, test = processDataTool.preprocess() 
    print 'Training'
    print train.head()
    print '' 
    print 'Test'
    print test.head()
    print 'Finished Loading'

if __name__ == "__main__":
    main()
