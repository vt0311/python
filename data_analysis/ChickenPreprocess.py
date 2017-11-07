import pandas as pd

def main():
    filename = 'd:/temp/chicken_data/bbq.csv'
    bbq_table = pd.DataFrame.from_csv(filename, encoding='CP949', index_col=0, header=0)

    

if __name__ == '__main__':
     main()


