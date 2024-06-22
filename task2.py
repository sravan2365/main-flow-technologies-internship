import pandas as pd

# Load the CSV file into a DataFrame
file_path = '/mnt/data/customers-100.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
df.head()
Result
   Index      Customer Id First Name Last Name  \
0      1  DD37Cf93aecA6Dc     Sheryl    Baxter   
1      2  1Ef7b82A4CAAD10    Preston    Lozano   
2      3  6F94879bDAfE5a6        Roy     Berry   
3      4  5Cef8BFA16c5e3c      Linda     Olsen   
4      5  053d585Ab6b3159     Joanna    Bender   

                           Company               City  \
0                  Rasmussen Group       East Leonard   
1                      Vega-Gentry  East Jimmychester   
2                    Murillo-Perry      Isabelborough   
3  Dominguez, Mcmillan and Donovan         Bensonview   
4         Martin, Lang and Andrade     West Priscilla   

                      Country                 Phone 1                Phone 2  \
0                       Chile            229.077.5154       397.884.0519x718   
1                    Djibouti              5153435776       686-620-1820x944   
2         Antigua and Barbuda         +1-539-402-0259    (496)978-3969x58947   
3          Dominican Republic  001-808-617-6467x12895        +1-813-324-8756   
4  Slovakia (Slovak Republic)  001-234-203-0635x76146  001-199-446-3860x3486   

                         Email Subscription Date                      Website  
0     zunigavanessa@smith.info        2020-08-24   http://www.stephenson.com/  
1              vmata@colon.com        2021-04-23        http://www.hobbs.com/  
2          beckycarr@hogan.com        2020-03-25     http://www.lawrence.com/  
3  stanleyblackwell@benson.org        2020-06-02   http://www.good-lyons.com/  
4      colinalvarado@miles.net        2021-04-17  https://goodwin-ingram.com