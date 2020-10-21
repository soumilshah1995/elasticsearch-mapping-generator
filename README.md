----------------------------------------
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)]
---------------------------


# Elastic Search Mapping Generator   

#### what is Elastic Search Mapping Generator  ?
* For the past few months, i have been working on elastic search. I notice that it's hard to generate dynamic Query for elastic search it would be great if we had a class that can generate these complex queries. that's the reason I published an open-source library on PyPI that can generate these queries for you 
* Link :  https://pypi.org/project/elasticsearchquerygenerator/
* Similar approach i wanted to create something that can generate elastic search mapping as well 


## documentation :
* UML Diagram 

![image](https://user-images.githubusercontent.com/39345855/96673304-36969f00-1334-11eb-8a2f-8a7d32762d9d.png)

#### Constructor: 
    * number_of_shards: default shards is 1 
    * number_of_replicas: default is 0 
    
 
##### add_feilds(feild_name=None,type=None,index=True,keywords=True):

* This is main method which does most of work for you 

#### type:
* Type can be text for full text search see link for more details https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-types.html

#### index : Default value is  True
* The index option controls whether field values are indexed. It accepts true or false and defaults to true. Fields that are not indexed are not queryable. https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-index.html

#### keywords : Default value is  True
* Read more https://www.elastic.co/guide/en/elasticsearch/reference/current/keyword.html
* if you dont want keywords set this to False


## Installation

```bash
pip install elasticsearchmappinggenerator
```
## Usage

### Schema
```json

{
    "first_name":"Soumil  ",
    "last_name":"Shah"
}

```

```python
from elasticsearchmappinggenerator.elasticsearchmappinggenerator import ElasticMappingGenerator
import json

def main():
    _helper = ElasticMappingGenerator(number_of_replicas=1,number_of_shards=20)
    _helper.add_feilds(feild_name='first_name', type='text', index=True, keywords=False)
    _helper.add_feilds(feild_name='last_name', type='text', index=True)
    query = _helper.complete_mappings()
    print(json.dumps(query, indent=3))
    
if __name__ == '__main__':
    main()

```
### Output :
```json
{
   "settings": {
      "index": {
         "number_of_shards": 20,
         "number_of_replicas": 1
      }
   },
   "mappings": {
      "properties": {
         "name": {
            "properties": {
               "first_name": {
                  "type": "text",
                  "index": true
               },
               "last_name": {
                  "type": "text",
                  "index": true,
                  "fields": {
                     "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                     }
                  }
               }
            }
         }
      }
   }
}

```

### Generating Nested Schema 
```json

   {   
        "name":
            {
                "first_name":"Soumil  ",
                "last_name":"Shah"
                
            }
   
    }
```

```python

def main():
    _helper = ElasticMappingGenerator(number_of_replicas=1,number_of_shards=20)
    _helper.add_feilds(feild_name='name.first_name', type='text', index=True, keywords=False)
    _helper.add_feilds(feild_name='name.last_name', type='text', index=True)
    query = _helper.complete_mappings()
    print(json.dumps(query, indent=3))
    
if __name__ == '__main__':
    main()

```

#### output 
```json
{
   "settings": {
      "index": {
         "number_of_shards": 20,
         "number_of_replicas": 1
      }
   },
   "mappings": {
      "properties": {
         "name": {
            "properties": {
               "first_name": {
                  "type": "text",
                  "index": true
               },
               "last_name": {
                  "type": "text",
                  "index": true,
                  "fields": {
                     "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                     }
                  }
               }
            }
         }
      }
   }
}

```

##### i would be adding more examples and making it better and better 

## Authors

## Soumil Nitin Shah 

* Excellent experience of building scalable and high-performance Software Applications combining distinctive skill sets in Internet of Things (IoT), Machine Learning and Full Stack Web Development in Python.

Bachelor in Electronic Engineering |
Masters in Electrical Engineering | 
Master in Computer Engineering |

* Website : https://soumilshah.herokuapp.com
* Github: https://github.com/soumilshah1995
* Linkedin: https://www.linkedin.com/in/shah-soumil/
* Blog: https://soumilshah1995.blogspot.com/
* Youtube : https://www.youtube.com/channel/UC_eOodxvwS_H7x2uLQa-svw?view_as=subscriber
* Facebook Page : https://www.facebook.com/soumilshah1995/
* Email : shahsoumil519@gmail.com


[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/soumilshah1995)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
