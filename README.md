

### records package 

The records package is a module developed to retrieve biodiversity data from GBIF 

#### Installation

```bash
git clone https://github.com/kuratanp/records.git
cd records
pip install .
```


#### Usage

```python

## import the record package
import records

## create instance by entering query (e.g. Bombus) and a range of years as integers (e.g. between 1950 and 1955)
rec = Records(q="Bombus", interval=(1950, 1955))


## access all of the returned records as a dataframe
rec.df 

## see the shape to see how many records there are)
rec.df.shape

```

