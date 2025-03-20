import pluginutils
from pluginutils import MongoQueryHelper

query = MongoQueryHelper().set(name="John", age=30).unset("old_field").inc(age=1).build_update()
print(query)