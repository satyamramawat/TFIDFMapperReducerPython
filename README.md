# TF-IDF Calucaltion via Hadoop Mapper Reducer

## 1) I/O mechanism of the code

Stage 1 Mapper Input -> Raw Data
Stage 1 Reducer Output -> TF

Stage 2 Mapper Input -> Takes input as output of 1 stage MapReduce Job.
Stage 2 Reducer Ouput -> IDF 

Stage 3 Mapper Input -> Takes input as output of 2nd stage MapReduce Job.
Stage 3 Mapper Output -> TF-IDF (TF x IDF)

## 2) How code will work

TF-IDF Calculation has been done into three stages whereas, 

1st Stage:
Mapper(Input): RAW DATA 
Reducer(Output): Will generate a Text file like part-0000.txt which has data in format{(word, document id), Word count in Document}

2nd Stage:
Mapper(Input): Will take input of 1st stage Output {(word, document id), Word count in Document}
Reducer(Output): Will generate a Text file like part-0000.txt which has data in format{(word, document id), (word count in document, words in doc)}

3rd Stage:
Mapper(Input): Will take input of 2nd stage Output {(word, document id), (word count in document, words in doc)}
Reducer(Output): Will generate a Text file like part-0000.txt which has final tf-idf data in format {(word, doc_id), tf-idf}

## 3) Test on Local

- Clone the Repo
- Go to terminal
- Type Command `cat <AnyTextFile> | python MapperPhaseOne.py | python ReducerPhaseOne.py`
  
## 4) Run on HDFS 

`hadoop jar ../libexec/share/hadoop/tools/lib/hadoop-*streaming*.jar \ 
-file /Users/satyamramawat/Desktop/Hadoop/python/mapper.py \
-mapper /Users/satyamramawat/Desktop/Hadoop/python/mapper.py \
-file /Users/satyamramawat/Desktop/Hadoop/python/reducer.py  \
-reducer /Users/satyamramawat/Desktop/Hadoop/python/reducer.py  \
-input /python/test.txt/ \
-output /wordout `

**IMPORTANT NOTE**
- Kindly have Latest Hadoop Streaming JAR which has version more then 3.x.x, older version does not support -file extension.

Author - Satyam Ramawat
