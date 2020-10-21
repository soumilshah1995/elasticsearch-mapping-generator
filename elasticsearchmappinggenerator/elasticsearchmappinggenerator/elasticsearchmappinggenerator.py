__AUTHOR__ = "soumil Nitin Shah"
__EMAIL__ = "shahsoumil519@gmail.com"


try:
    import os
    import json
    import sys
    print("All Modules loaded : {} ".format(sys.version))
except Exception as e:
    print("Some Module Missing :  {} ".format(e))


class ElasticMappingGenerator(object):

    def __init__(self, number_of_shards=1, number_of_replicas=0):
        self.number_of_shards=number_of_shards
        self.number_of_replicas=number_of_replicas

        self._index = {
            "number_of_shards":self.number_of_shards,
            "number_of_replicas":self.number_of_replicas
        }

        self._settings = {
            "index":self._index
        }

        self.mappers = {
            "settings":self._settings,
            "mappings":{
                'properties':{

                }
            }
        }

    def add_feilds(self,
                   feild_name=None,
                   type=None,
                   index=True,
                   keywords=True):

        if not feild_name.__contains__("."):
            if keywords:
                template = {
                    "properties" : {
                        "{}".format(feild_name):{
                            "type":type,
                            'index':index,

                            'fields':{
                                "keyword" : {
                                    "type" : "keyword",
                                    "ignore_above" : 256
                                }},
                        }
                    }
                }
            else:
                template = {
                    "properties" : {
                        "{}".format(feild_name):{
                            "type":type,
                            'index':index,
                        },
                    }
                }
            self.mappers['mappings']['properties'][feild_name] = template.get("properties").get("{}".format(feild_name))
        else:
            primary, child = feild_name.split(".")

            # Check if Parent Exists
            # if Parent Exists then append the child

            if(self.mappers.get('mappings').get('properties').get(primary) is None):
                self.mappers['mappings']['properties'][primary] = {
                    "properties":{
                    }
                }
            if keywords:
                self.mappers['mappings']['properties'][primary]['properties'][child] = {
                    "type":type,
                    'index':index,
                    'fields':{
                        "keyword" : {
                            "type" : "keyword",
                            "ignore_above" : 256
                        }
                    }
                }
            else:
                self.mappers['mappings']['properties'][primary]['properties'][child] = {
                    "type":type,
                    'index':index,
                }

    def complete_mappings(self):
        return self.mappers


# def main():
#     _helper = ElasticMappingGenerator(number_of_replicas=1,number_of_shards=20)
#     _helper.add_feilds(feild_name='name.first_name', type='text', index=True, keywords=False)
#     _helper.add_feilds(feild_name='name.last_name', type='text', index=True)
#     query = _helper.complete_mappings()
#     print(json.dumps(query, indent=3))
#
# if __name__ == '__main__':
#     main()
#
#



